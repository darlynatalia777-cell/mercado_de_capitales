#!/usr/bin/env python3
"""Descarga precios de acciones colombianas y genera datos.json para la aplicación."""

from __future__ import annotations

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import yfinance as yf


# Tickers Yahoo Finance propuestos; verifique disponibilidad y cámbielos si su equipo valida otros.
ACCIONES = [
    {"ticker": "ECOPETROL.CL", "nombre": "Ecopetrol", "nemotecnico": "ECOPETROL", "sector": "Petróleo y gas"},
    {"ticker": "PFBCOLOM.CL", "nombre": "Grupo Cibest (preferencial)", "nemotecnico": "PFBCOLOM", "sector": "Financiero"},
    {"ticker": "BCOLOMBIA.CL", "nombre": "Grupo Cibest", "nemotecnico": "BCOLOMBIA", "sector": "Financiero"},
    {"ticker": "ISA.CL", "nombre": "Interconexión Eléctrica", "nemotecnico": "ISA", "sector": "Energía e infraestructura"},
    {"ticker": "GRUPOSURA.CL", "nombre": "Grupo SURA", "nemotecnico": "GRUPOSURA", "sector": "Financiero"},
    {"ticker": "GRUPOARGOS.CL", "nombre": "Grupo Argos", "nemotecnico": "GRUPOARGOS", "sector": "Materiales e infraestructura"},
    {"ticker": "CEMARGOS.CL", "nombre": "Cementos Argos", "nemotecnico": "CEMARGOS", "sector": "Materiales"},
    {"ticker": "CELSIA.CL", "nombre": "Celsia", "nemotecnico": "CELSIA", "sector": "Energía"},
]

DESTINO = Path(__file__).with_name("datos.json")
FUENTE = "Yahoo Finance (yfinance); rentabilidades con precio ajustado por dividendos"


def numero(valor: object, campo: str) -> float:
    """Convierte a número finito o informa un dato ausente/inválido."""
    resultado = float(valor)
    if not math.isfinite(resultado):
        raise ValueError(f"{campo} no es un número finito")
    return resultado


def preparar_historial(frame: pd.DataFrame, ticker: str) -> pd.DataFrame:
    if frame.empty:
        raise ValueError("Yahoo Finance no devolvió precios")
    frame = frame.copy()
    frame.index = pd.to_datetime(frame.index)
    if frame.index.tz is not None:
        frame.index = frame.index.tz_localize(None)
    frame = frame.sort_index()
    for column in ("Close", "Adj Close", "Dividends"):
        if column not in frame.columns:
            if column == "Dividends":
                frame[column] = 0.0
            else:
                raise ValueError(f"Falta la columna {column}")
    frame = frame.dropna(subset=["Close", "Adj Close"])
    frame = frame[(frame["Close"] > 0) & (frame["Adj Close"] > 0)]
    if frame.empty:
        raise ValueError("No hay cierres válidos")
    return frame


def actualizar_accion(datos: dict[str, str]) -> dict[str, object]:
    ticker = datos["ticker"]
    frame = preparar_historial(
        yf.Ticker(ticker).history(period="3y", auto_adjust=False),
        ticker,
    )
    ultimo_dia = frame.index[-1]
    ultimo_close = numero(frame["Close"].iloc[-1], "Close")
    ultimo_adj = numero(frame["Adj Close"].iloc[-1], "Adj Close")
    if len(frame) < 2:
        raise ValueError("Se requieren al menos dos precios diarios")

    anterior_close = numero(frame["Close"].iloc[-2], "Close anterior")
    variacion_dia = (ultimo_close / anterior_close - 1) * 100

    hace_un_ano = ultimo_dia - pd.Timedelta(days=365)
    indice_un_ano = (frame.index - hace_un_ano).to_series().abs().idxmin()
    adj_un_ano = numero(frame.loc[indice_un_ano, "Adj Close"], "Adj Close de hace un año")
    rentabilidad_un_ano = (ultimo_adj / adj_un_ano - 1) * 100

    primer_adj = numero(frame["Adj Close"].iloc[0], "Primer Adj Close")
    anos = (ultimo_dia - frame.index[0]).days / 365.2425
    if anos <= 0:
        raise ValueError("El historial no cubre un periodo positivo")
    rentabilidad_anual = ((ultimo_adj / primer_adj) ** (1 / anos) - 1) * 100

    desde_un_ano = frame.loc[frame.index >= hace_un_ano]
    log_returns = (desde_un_ano["Adj Close"] / desde_un_ano["Adj Close"].shift(1)).apply(
        lambda value: math.log(value) if pd.notna(value) and value > 0 else float("nan")
    ).dropna()
    if len(log_returns) < 2:
        raise ValueError("No hay rendimientos diarios suficientes para estimar volatilidad")
    volatilidad = float(log_returns.std(ddof=1) * math.sqrt(252) * 100)

    adjusted_last_year = desde_un_ano["Adj Close"]
    drawdown = adjusted_last_year / adjusted_last_year.cummax() - 1
    max_drawdown = float(drawdown.min() * 100)
    dividends = pd.to_numeric(frame["Dividends"], errors="coerce").fillna(0)
    dividends_year = float(dividends.loc[dividends.index >= hace_un_ano].sum())
    dividend_yield = dividends_year / ultimo_close * 100

    monthly_close = frame["Close"].groupby(frame.index.to_period("M")).last().tail(36)
    history = [
        {"mes": str(month), "cierre": round(numero(close, "Cierre mensual"), 2)}
        for month, close in monthly_close.items()
    ]

    def redondear(value: float) -> float:
        return round(numero(value, "indicador"), 2)

    return {
        "ticker": ticker,
        "nombre": datos["nombre"],
        "nemotecnico": datos["nemotecnico"],
        "sector": datos["sector"],
        "moneda": "COP",
        "precio": round(ultimo_close, 2),
        "fecha": ultimo_dia.strftime("%Y-%m-%d"),
        "variacion_dia_pct": redondear(variacion_dia),
        "rent_1a_pct": redondear(rentabilidad_un_ano),
        "rent_anual_3a_pct": redondear(rentabilidad_anual),
        "volatilidad_anual_pct": redondear(volatilidad),
        "caida_maxima_1a_pct": redondear(max_drawdown),
        "dividendo_rend_pct": redondear(dividend_yield),
        "historico": history,
    }


def descargar_trm() -> dict[str, object] | None:
    try:
        frame = yf.Ticker("USDCOP=X").history(period="1mo", auto_adjust=False)
        if frame.empty or "Close" not in frame:
            return None
        cierres = frame["Close"].dropna()
        if cierres.empty:
            return None
        fecha = pd.Timestamp(cierres.index[-1])
        return {"valor": round(numero(cierres.iloc[-1], "TRM"), 2), "fecha": fecha.strftime("%Y-%m-%d")}
    except Exception as error:
        print(f"Aviso: no se pudo descargar la TRM: {error}", file=sys.stderr)
        return None


def main() -> None:
    acciones = []
    errores = []
    for datos in ACCIONES:
        try:
            accion = actualizar_accion(datos)
            acciones.append(accion)
            print(f"Actualizada: {datos['ticker']} ({accion['fecha']})")
        except Exception as error:  # Cada ticker es independiente; registrar y continuar con los demás.
            motivo = f"{type(error).__name__}: {error}"
            errores.append({"ticker": datos["ticker"], "motivo": motivo})
            print(f"Error en {datos['ticker']}: {motivo}", file=sys.stderr)

    if not acciones:
        print("Aviso: ninguna acción se actualizó; se conserva el datos.json anterior.")
        print("Resumen: 0 acciones actualizadas; fallidas: " + (", ".join(item["ticker"] for item in errores) or "ninguna"))
        return

    documento = {
        "actualizado": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "fuente": FUENTE,
        "trm": descargar_trm(),
        "acciones": acciones,
        "errores": errores,
    }
    temporal = DESTINO.with_suffix(".json.tmp")
    try:
        temporal.write_text(json.dumps(documento, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        temporal.replace(DESTINO)
    except Exception as error:
        try:
            temporal.unlink(missing_ok=True)
        except OSError:
            pass
        print(f"Aviso: no fue posible guardar datos.json: {error}", file=sys.stderr)
        return

    fallidas = ", ".join(item["ticker"] for item in errores) or "ninguna"
    print(f"Resumen: {len(acciones)} acciones actualizadas; fallidas: {fallidas}")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        # La actualización automatizada debe terminar sin propagar un error de ejecución.
        print(f"Aviso: actualización interrumpida; se conserva el datos.json anterior: {error}", file=sys.stderr)
