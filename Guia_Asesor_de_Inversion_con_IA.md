

# **Guía paso a paso: Asesor de Inversión con IA** 

Proyecto de aula · Mercado de Capitales (640804) · Administración de Negocios Internacionales · UNIPAZ · Semestre B-2026 · Docente: Omar Guerrero Avilés 

## **¿Qué van a construir?** 

En parejas, van a crear la página web de una firma asesora de inversión, con ayuda de Gemini. La página: 

- presenta a los dos integrantes como asesores financieros, con una foto profesional hecha con IA; 

- hace 5 preguntas al usuario y le dice su perfil de inversionista (conservador, moderado o arriesgado); 

- muestra las acciones más populares de Colombia con **precios reales que se actualizan solos** cada día hábil; 

- simula cuánto tendrá el usuario, cuánto debe invertir, en cuánto tiempo llega a su meta o cuánto debe ahorrar al mes. 

#### **Antes de empezar, tengan a la mano** 

- `☐` Una cuenta de Google por persona (para usar Gemini). 

- `☐` Una cuenta gratuita de GitHub por pareja: github.com. 

- `☐` Una foto de cada integrante: de frente, con buena luz, sin gafas oscuras ni gorra. 

- `☐` El archivo **Prompts_Asesor_de_Inversion.txt** , que trae los dos prompts que van a usar. 

## **La ruta en 6 pasos** 

|**Paso**|**Qué hacen**|**Herramienta**|**Tiempo**|
|---|---|---|---|
|1|Convertir sus fotos en retratos profesionales|Gemini|20 min|
|2|Escoger las 8 acciones y verificar sus códigos|Yahoo Finance y bvc.com.co|30 min|
|3|Crear el aplicativo con el prompt|Gemini con Canvas|40 min|
|4|Subir los archivos|GitHub|20 min|
|5|Publicar y traer los datos reales|GitHub|15 min|
|6|Probar y corregir|Navegador y celular|30 min|



Asesor de Inversión con IA · Mercado de Capitales · UNIPAZ 

Página 1 

## **Paso 1. Fotos profesionales con IA** 

Cada integrante convierte su propia foto en un retrato tipo documento, vestido como asesor financiero, sin que cambie su cara. La edición de fotos de Gemini se puede usar en la versión gratuita (Xataka). 

1. Entren a gemini.google.com (o a la app de Gemini) y abran un chat nuevo. 

2. Adjunten su foto con el botón **+** . 

3. Copien el **Prompt 1** del archivo de prompts, escojan la ropa que prefieran en la regla 3 y envíenlo. 

4. Comparen el resultado con la foto original usando la lista de abajo. 

5. Si algo cambió, escriban: _“Cambiaste [el rasgo]. Vuelve a intentarlo conservando mi rostro exactamente igual al original.”_ 

6. Descarguen la imagen y guárdenla como **foto1.jpg** (integrante 1) y **foto2.jpg** (integrante 2), en minúsculas. 

#### **¿La foto quedó bien?** 

- `☐` Es claramente la misma persona: forma de la cara, ojos, nariz, boca y cejas iguales. 

- `☐` Mismo tono de piel; se conservan lunares, pecas o cicatrices. 

- `☐` La piel se ve natural, con textura; no se ve plástica ni brillante. 

- `☐` Fondo gris liso, de los hombros hacia arriba, mirando a la cámara. 

#### **Importante** 

La página y el repositorio serán públicos: cualquier persona con el enlace verá las fotos. Cada integrante debe estar de acuerdo. Si alguien prefiere no publicar su foto, no la suba: el aplicativo mostrará sus iniciales en un círculo. 

**Prompt 1: foto profesional (también está en el archivo de prompts)** 

```
Edita la foto que adjunto para convertirla en un retrato profesional tipo documento de un
asesor financiero. Reglas obligatorias:
```

`1. Es la misma persona. No cambies la forma de la cara, los ojos, la nariz, la boca, las orejas, las cejas, el tono de piel, la edad aparente, los lunares, las pecas ni las cicatrices. No adelgaces ni "embellezcas" el rostro.` 

`2. Encuadre tipo documento: de los hombros hacia arriba, de frente, mirada a la cámara, expresión natural y amable, cabeza centrada.` 

`3. Ropa formal de asesor financiero: [saco azul oscuro con camisa blanca / saco gris con blusa blanca] (sin corbata llamativa ni accesorios grandes).` 

`4. Fondo liso gris claro, uniforme, sin objetos.` 

`5. Iluminación suave de estudio, sin sombras duras.` 

`6. Aspecto de fotografía real tomada con cámara: textura natural de la piel con poros, sin suavizado, sin efecto plástico, sin brillo artificial, sin maquillaje añadido, sin cambios de color de ojos ni de cabello.` 

`7. Formato cuadrado. Que no se note que la imagen fue editada con IA.` 

```
Si el resultado cambia algún rasgo de mi cara, vuelve a intentarlo conservando el rostro
exactamente como en la foto original.
```

Asesor de Inversión con IA · Mercado de Capitales · UNIPAZ 

Página 2 

## **Paso 2. Escoger las 8 acciones** 

El aplicativo mostrará 8 acciones colombianas. Seis son fijas, las más negociadas o las que más impulsaron el índice MSCI Colcap en el primer semestre de 2026. Ecopetrol concentró cerca de una tercera parte del volumen diario negociado, seguida por Preferencial Cibest, Cibest e ISA; Ecopetrol subió 30,2 %, ISA 19,6 %, Éxito 14,5 % y Preferencial Aval 13,4 % en ese semestre (El Tiempo, 9 de agosto de 2026). Las otras dos las escoge cada pareja entre las acciones que se negocian en la BVC. 

|**Acción**|**Nemotécnico BVC**|**Código en Yahoo Finance**|**Sector**|
|---|---|---|---|
|Ecopetrol|ECOPETROL|ECOPETROL.CL (verificado)|Petróleo y gas|
|Grupo Cibest, preferencial|PFCIBEST|PFCIBEST.CL (verificado)|Financiero|
|Grupo Cibest, ordinaria|CIBEST|Verificar|Financiero|
|ISA|Verificar en bvc.com.co|Verificar|Energía e infraestructura|
|Grupo Éxito|Verificar en bvc.com.co|Verificar|Comercio|
|Grupo Aval, preferencial|Verificar en bvc.com.co|Verificar|Financiero|
|Libre elección 1||||
|Libre elección 2||||



Grupo Cibest es la matriz de Bancolombia y cotiza en la BVC desde el 19 de mayo de 2025 con los nemotécnicos CIBEST y PFCIBEST (Valora Analitik). Por eso su historial con ese nombre puede ser menor a 3 años. 

### **Cómo encontrar el código de Yahoo Finance** 

1. Entren a finance.yahoo.com y busquen el nombre de la empresa. 

2. Escojan el resultado que termina en **.CL** y que dice **BVC** y **COP** . Ejemplo: **ECOPETROL.CL** . 

3. Comparen el precio con el de bvc.com.co: debe ser casi igual. 

4. Completen la tabla con el código, el nombre, el nemotécnico y el sector de las 8 acciones. La van a pegar en el Prompt 2. 

## **Paso 3. Crear el aplicativo con Gemini** 

1. Abran el archivo de prompts y copien el **Prompt 2** en un documento aparte. 

2. Reemplacen todo lo que está entre [CORCHETES]: nombre de la firma, eslogan, sus nombres y frases, la tabla de acciones del paso 2, la tasa de un CDT a 360 días que hayan consultado en un banco y la inflación anual publicada por el DANE. 

3. En Gemini, abran un chat nuevo, activen **Canvas** debajo de la barra de mensajes, peguen el prompt y envíenlo (Google: Canvas). 

4. En la vista previa verán un aviso amarillo de **datos de ejemplo** y las iniciales en lugar de las fotos. Es normal: los datos reales y las fotos aparecen cuando se publique en el paso 5. 

5. Si Gemini muestra un solo archivo, escriban: _“Ahora muéstrame completo el archivo actualizar_datos.py”_ . 

6. Guarden cada archivo con su nombre exacto: **index.html** y **actualizar_datos.py** . En el Bloc de notas: _Guardar como_ → Tipo: _Todos los archivos_ → Codificación: _UTF-8_ . 

Asesor de Inversión con IA · Mercado de Capitales · UNIPAZ 

Página 3 

#### **Si algo sale mal, no empiecen de cero: pidan la corrección** 

- _“Al hacer clic en [botón] pasa [lo que pasa] y debería pasar [lo esperado]. Corrige solo eso y entrégame el archivo completo.”_ 

- _“Verifica que con capital de 1.000.000, rentabilidad de 10 %, 5 años y sin aportes, el resultado sea $ 1.610.510.”_ 

- _“Revisa que todo se vea bien en un celular de 360 px de ancho.”_ 

- Anoten cada prompt de corrección en su bitácora: qué pidieron, qué falló y cómo quedó. 

**Prompt 2: aplicativo completo (cópienlo del archivo de prompts, no de este PDF)** 

```
Actúa como desarrollador web experto y como profesor de Mercado de Capitales. Construye un
aplicativo web académico llamado "[NOMBRE DE LA FIRMA] Asesores de Inversión", hecho por
estudiantes de Administración de Negocios Internacionales de UNIPAZ (Barrancabermeja,
Colombia). Debe mostrar las acciones más populares de Colombia con datos reales y
actualizados y permitir simular inversiones.
ENTREGA EXACTAMENTE 3 ARCHIVOS, cada uno completo y en un bloque separado:
  A) index.html                         (el aplicativo)
  B) actualizar_datos.py                (descarga los datos reales y crea datos.json)
  C) .github/workflows/actualizar.yml   (usa EXACTAMENTE el contenido de abajo)
```

```
-------------------------------------------------------------------------------------
ARCHIVO A — index.html
-------------------------------------------------------------------------------------
Requisitos técnicos
- Un solo archivo con HTML, CSS y JavaScript puro. Sin servidor ni inicio de sesión.
- Única librería externa permitida: Chart.js por CDN (gráficos).
```

- `<html lang="es-CO">. Todo el texto en español de Colombia. - Responsive: debe verse bien en celular (360 px) y en computador. - Colores: azul marino #16234F, verde #2E9E5B, azul claro #D7E3FA, fondo blanco. Títulos en Georgia; texto en Calibri, Arial o sans-serif. - Formatos: pesos como "$ 1.234.567" y porcentajes como "12,5 %" (usa Intl.NumberFormat('es-CO')). - Al inicio del script, un objeto CONFIG con todo lo editable y comentado en español: nombres de la firma y de los asesores, preguntas del perfil, tasa CDT e inflación por defecto. - Código comentado en español, sección por sección. Datos - Al abrir, carga "datos.json" (misma carpeta) con fetch y la opción cache: "no-store". - Si datos.json no existe o falla, muestra un aviso amarillo visible: "DATOS DE EJEMPLO — NO SON REALES. Los datos reales aparecen cuando se publique en GitHub." y usa 3 acciones de ejemplo con nombres ficticios ("Acción Ejemplo A, B, C"). - Siempre muestra debajo de la tabla: "Fuente: [fuente del JSON] · Datos al [fecha]". Secciones (en este orden) 1. Encabezado: nombre de la firma, eslogan "[ESLOGAN]" y el aviso: "Herramienta académica. No constituye asesoría ni recomendación profesional de inversión." 2. "Su equipo asesor": dos tarjetas con foto redonda (foto1.jpg y foto2.jpg), nombre, cargo "Asesor(a) financiero(a)" y una línea de presentación: - [NOMBRE INTEGRANTE 1] — [frase corta] - [NOMBRE INTEGRANTE 2] — [frase corta] Si una foto no carga (por ejemplo, en la vista previa), muestra un círculo azul marino con las iniciales. Debajo, en letra pequeña: "Estudiantes de Administración de Negocios Internacionales — UNIPAZ". 3. "Conozcamos su perfil": 5 preguntas de una en una, con barra de progreso. Cada opción` 

Asesor de Inversión con IA · Mercado de Capitales · UNIPAZ 

Página 4 

```
   vale de 1 a 4 puntos en el orden escrito:
```

- `1) ¿En cuánto tiempo necesitará el dinero? Menos de 1 año / 1 a 3 años / 3 a 5 años / Más de 5 años` 

- `2) Si su inversión cae 20 % en un mes, ¿qué hace? Retiro todo / Retiro una parte / Espero / Invierto más` 

- `3) ¿Qué ha invertido antes? Nada / CDT o ahorro / Fondos de inversión / Acciones` 

- `4) ¿Tiene ahorros para emergencias de 3 a 6 meses? No / Menos de 3 meses / Sí, 3 a 6 meses / Sí, más de 6 meses` 

- `5) ¿Qué busca? Proteger mi dinero / Un poco más que un CDT / Crecer / Crecer al máximo Puntaje 5–9 = Conservador, 10–15 = Moderado, 16–20 = Arriesgado. Muestra el perfil con una explicación de 3 líneas en lenguaje sencillo. Al perfil Conservador agrégale: "Para su perfil, las acciones deberían ser una parte` 

```
   pequeña de su dinero; considere primero CDT, TES o fondos de renta fija."
```

```
4. "Acciones más populares de Colombia": tabla (en celular, tarjetas) con: nombre,
   nemotécnico, sector, precio actual, variación del día, rentabilidad 1 año,
   rentabilidad anual promedio 3 años, volatilidad anual, caída máxima en 1 año,
   rendimiento por dividendo y nivel de riesgo. Nivel de riesgo según la volatilidad:
   menos de 20 % = Bajo, 20 % a 35 % = Medio, más de 35 % = Alto. Variaciones positivas
   en verde y negativas en rojo. Al tocar una acción, muestra su gráfico de línea mensual
   de los últimos 3 años. Marca con una etiqueta "Acorde a su perfil" las acciones cuyo
   riesgo encaja: Conservador = Bajo; Moderado = Bajo o Medio; Arriesgado = todas.
```

```
   Si ninguna encaja, muestra: "Ninguna de estas acciones tiene riesgo bajo; para su
   perfil conviene priorizar instrumentos de renta fija."
   Muestra la TRM del JSON si existe.
```

`5. "Simulador de inversión":` 

- `a) Qué invertir: una acción, o una canasta de varias acciones con pesos iguales` 

- `(casillas de selección).` 

- `b) Rentabilidad base (r, efectiva anual): selector entre "Promedio anual 3 años" (por defecto), "Último año" o "Personalizada" (el usuario la escribe). En una canasta: r y la volatilidad = promedio simple de las acciones elegidas.` 

- `c) Cuatro modos en pestañas:` 

`1. ¿Cuánto tendré?           Datos: capital inicial, aporte mensual (opcional), años.` 

`2. ¿Cuánto debo invertir hoy? Datos: meta, años, aporte mensual (opcional).` 

`3. ¿En cuánto tiempo llego?  Datos: capital inicial, meta, aporte mensual (opcional).` 

`4. ¿Cuánto debo ahorrar al mes? Datos: capital inicial, meta, años.` 

- `d) Fórmulas (aportes al final de cada mes):` 

- `i = (1 + r)^(1/12) − 1 VF = C·(1 + r)^n + A·[((1 + i)^(12n) − 1) / i] Capital necesario: C = (Meta − A·[((1 + i)^(12n) − 1) / i]) / (1 + r)^n Aporte necesario: A = (Meta − C·(1 + r)^n) · i / ((1 + i)^(12n) − 1) Tiempo: simula mes a mes hasta alcanzar la meta (máximo 100 años) y reporta años y meses.` 

```
      Si i = 0, usa la suma simple de aportes. Si r ≤ 0 o la meta no se alcanza en 100
      años, muéstralo con un mensaje claro en lugar de un error. Si el capital
      necesario da negativo, muestra $ 0 y explica que los aportes bastan.
```

- `e) Escenarios: pesimista = r − σ/√n, esperado = r, optimista = r + σ/√n` 

- `(σ = volatilidad anual, n = años). Muestra los tres resultados y explica en una línea que es un rango aproximado, no una garantía.` 

- `f) Muestra además: total aportado, ganancia estimada, cuántas acciones enteras se compran hoy con el capital inicial al precio actual (en una canasta, por acción) y el dinero sobrante; comparación con un CDT (tasa efectiva anual editable, por defecto [__ %]) y rentabilidad real frente a la inflación (editable, por defecto [__ %]): r_real = (1 + r) / (1 + inflación) − 1. g) Gráfico de línea año por año: escenario pesimista, esperado, optimista y total aportado.` 

- `h) Frase fija: "Rentabilidades pasadas no garantizan rentabilidades futuras."` 

`6. Botones "Imprimir o guardar en PDF" (window.print, con estilos de impresión limpios que incluyan las fotos del equipo y el resultado) y "Volver a empezar".` 

`7. Pie de página: "Proyecto de aula — Mercado de Capitales — UNIPAZ — [FECHA]".` 

Asesor de Inversión con IA · Mercado de Capitales · UNIPAZ 

Página 5 

```
-------------------------------------------------------------------------------------
ARCHIVO B — actualizar_datos.py
```

```
-------------------------------------------------------------------------------------
Script de Python 3.12 que usa yfinance y pandas para crear datos.json con datos reales.
```

```
Acciones (ticker de Yahoo Finance verificado por el equipo, nombre, nemotécnico BVC, sector):
[PEGAR AQUÍ LA TABLA DE 8 ACCIONES DEL PASO 2, por ejemplo:
 ECOPETROL.CL | Ecopetrol | ECOPETROL | Petróleo y gas
 ...]
```

```
Para cada acción:
```

- `Descarga 3 años de precios diarios con yf.Ticker(t).history(period="3y", auto_adjust=False) (columnas Close, Adj Close y Dividends). - precio = último Close; fecha = fecha de ese cierre (AAAA-MM-DD).` 

- `variacion_dia_pct = último Close / Close anterior − 1.` 

- `rent_1a_pct = Adj Close último / Adj Close de hace 1 año (fecha más cercana) − 1.` 

- `rent_anual_3a_pct = (Adj Close último / Adj Close primero)^(1 / años transcurridos) − 1, calculando los años con las fechas reales.` 

- `volatilidad_anual_pct = desviación estándar de los rendimientos logarítmicos diarios del último año (con Adj Close) × raíz de 252. - caida_maxima_1a_pct = mayor caída desde un máximo previo en el último año (negativa). - dividendo_rend_pct = suma de Dividends de los últimos 365 días / precio. - historico = último Close de cada mes de los 3 años: [{"mes": "AAAA-MM", "cierre": n}]. - Todos los porcentajes en por ciento (12.5 significa 12,5 %), redondeados a 2 decimales. TRM: intenta descargar "USDCOP=X" y guarda el último cierre y su fecha; si falla, usa null.` 

- `Robustez (muy importante) - Si una acción falla o no trae datos, no detengas el script: regístrala en una lista "errores" con el ticker y el motivo, y sigue con las demás.` 

- `Si TODAS fallan, no sobrescribas datos.json (conserva el anterior) e imprime un aviso. - El script siempre debe terminar sin error (código de salida 0).` 

- `Imprime al final un resumen: cuántas acciones se actualizaron y cuáles fallaron.` 

```
Estructura exacta de datos.json:
{
  "actualizado": "AAAA-MM-DDTHH:MM:SSZ",
```

```
  "fuente": "Yahoo Finance (yfinance); rentabilidades con precio ajustado por dividendos",
  "trm": {"valor": 0, "fecha": "AAAA-MM-DD"},
  "acciones": [
    {"ticker": "", "nombre": "", "nemotecnico": "", "sector": "", "moneda": "COP",
     "precio": 0, "fecha": "", "variacion_dia_pct": 0, "rent_1a_pct": 0,
     "rent_anual_3a_pct": 0, "volatilidad_anual_pct": 0, "caida_maxima_1a_pct": 0,
     "dividendo_rend_pct": 0, "historico": [{"mes": "AAAA-MM", "cierre": 0}]}
  ],
  "errores": [{"ticker": "", "motivo": ""}]
}
Guarda el JSON con ensure_ascii=False e indent=2.
```

```
-------------------------------------------------------------------------------------
ARCHIVO C — .github/workflows/actualizar.yml  (copia este contenido sin cambios)
-------------------------------------------------------------------------------------
name: Actualizar datos y publicar
```

```
on:
  push:
    branches: [main]
  schedule:
    - cron: "0 22 * * 1-5"   # 5:00 p. m. hora de Colombia, de lunes a viernes
  workflow_dispatch:
```

Asesor de Inversión con IA · Mercado de Capitales · UNIPAZ 

Página 6 

```
permissions:
  contents: write
  pages: write
  id-token: write
concurrency:
  group: pages
  cancel-in-progress: false
jobs:
  actualizar-y-publicar:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Instalar librerías
        run: pip install --upgrade yfinance pandas
      - name: Descargar datos reales
        run: python actualizar_datos.py
      - name: Guardar datos.json en el repositorio
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add datos.json
          git diff --staged --quiet || git commit -m "Actualiza datos de acciones"
          git push || echo "No se pudo guardar datos.json; se publica igual"
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: .
      - id: deployment
        uses: actions/deploy-pages@v4
```

```
AL TERMINAR
```

```
-------------------------------------------------------------------------------------
Entrega los 3 archivos completos, cada uno en su propio bloque. Después, fuera del código,
explica en máximo 10 líneas, para alguien que no programa, cómo funciona el aplicativo y
dónde se cambian los nombres, las preguntas y las tasas de CDT e inflación.
```

Asesor de Inversión con IA · Mercado de Capitales · UNIPAZ 

Página 7 

## **Paso 4. Subir los archivos a GitHub** 

1. En github.com, pulsen **New** , nombren el repositorio **asesor-inversion** , marquen **Public** y pulsen **Create repository** . 

2. Pulsen **Add file → Upload files** , arrastren **index.html** , **actualizar_datos.py** , **foto1.jpg** y **foto2.jpg** y pulsen **Commit changes** . 

3. Pulsen **Add file → Create new file** . En el nombre escriban exactamente **.github/workflows/actualizar.yml** (cada “/” crea una carpeta). 

4. Peguen el contenido del recuadro de abajo (es el archivo C del Prompt 2) y pulsen **Commit changes** . 

|**Archivo**|**Para qué sirve**|
|---|---|
|index.html|El aplicativo que ve el usuario|
|actualizar_datos.py|Descarga los precios reales y crea datos.json|
|foto1.jpg y foto2.jpg|Las fotos de los asesores|
|.github/workflows/actualizar.yml|Ordena a GitHub actualizar los datos y publicar la página|
|datos.json|No lo suben ustedes: GitHub lo crea solo en el paso 5|



### **Contenido de .github/workflows/actualizar.yml** 

```
name: Actualizar datos y publicar
on:
  push:
    branches: [main]
  schedule:
    - cron: "0 22 * * 1-5"   # 5:00 p. m. hora de Colombia, de lunes a viernes
  workflow_dispatch:
permissions:
  contents: write
  pages: write
  id-token: write
concurrency:
  group: pages
  cancel-in-progress: false
jobs:
  actualizar-y-publicar:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Instalar librerías
        run: pip install --upgrade yfinance pandas
      - name: Descargar datos reales
        run: python actualizar_datos.py
      - name: Guardar datos.json en el repositorio
        run: |
          git config user.name "github-actions[bot]"
```

Asesor de Inversión con IA · Mercado de Capitales · UNIPAZ 

Página 8 

```
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add datos.json
          git diff --staged --quiet || git commit -m "Actualiza datos de acciones"
          git push || echo "No se pudo guardar datos.json; se publica igual"
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: .
      - id: deployment
        uses: actions/deploy-pages@v4
```

## **Paso 5. Publicar y traer los datos reales** 

1. En el repositorio, vayan a **Settings → Pages** . En _Build and deployment_ , en _Source_ , escojan **GitHub Actions** (GitHub Docs). 

2. Vayan a la pestaña **Actions** , escojan **Actualizar datos y publicar** y pulsen **Run workflow → Run workflow** . 

3. Esperen 2 a 4 minutos hasta ver el chulo verde. Abran la ejecución: arriba aparece el enlace de su página, del tipo **https://usuario.github.io/asesor-inversion/** . 

4. Abran el enlace. Ya deben verse las fotos y los precios reales, con la fecha de los datos. 

#### **Actualización automática** 

Desde ahora, GitHub descarga precios nuevos de lunes a viernes a las 5:00 p. m. (hora de Colombia) y vuelve a publicar la página sin que hagan nada. También publica cada vez que suban un archivo nuevo. 

## **Paso 6. Probar y corregir** 

- `☐` La página abre desde el celular y se ve completa. 

- `☐` Aparecen las dos fotos, los nombres y el aviso académico. 

- `☐` No aparece el aviso amarillo y la fecha de los datos es la del último día hábil. 

- `☐` El precio de Ecopetrol es casi igual al de bvc.com.co. 

- `☐` Perfil: respondiendo siempre la primera opción sale Conservador; siempre la última, Arriesgado. 

- `☐` Al tocar una acción aparece su gráfico de 3 años. 

- `☐` El botón de imprimir genera un PDF limpio con las fotos y el resultado. 

**Prueba del simulador con rentabilidad personalizada de 10 % efectiva anual (aportes al final de cada** 

**mes):** 

|**Modo**|**Datos**|**Resultado esperado**|
|---|---|---|
|¿Cuánto tendré?|Capital 1.000.000 · 5 años · sin aportes|$ 1.610.510|
|¿Cuánto tendré?|Capital 1.000.000 · 5 años · aporte 100.000 al mes|$ 9.266.633|
|¿Cuánto debo invertir hoy?|Meta 5.000.000 · 5 años · sin aportes|$ 3.104.607|
|¿En cuánto tiempo llego?|Capital 1.000.000 · meta 2.000.000 · sin aportes|7 años y 4 meses|
|¿Cuánto debo ahorrar al mes?|Capital 1.000.000 · meta 10.000.000 · 5 años|$ 109.579 al mes|



Una diferencia de pocos pesos por redondeo es aceptable. Si la diferencia es grande, pidan la corrección a Gemini con estos mismos datos. 

Asesor de Inversión con IA · Mercado de Capitales · UNIPAZ 

Página 9 

### **Si algo falla** 

|**Problema**|**Solución**|
|---|---|
|En Actions aparece una X roja en<br>“Descargar datos reales”|Abran la ejecución, copien el mensaje de error y péguenlo en Gemini:_“Este es_<br>_el error de GitHub Actions al ejecutar actualizar_datos.py: [error]. Corrige el_<br>_script.”_|
|La X roja está en “deploy-pages” o<br>“configure-pages”|Revisen que en Settings → Pages el Source sea**GitHub Actions**y vuelvan a<br>ejecutar.|
|Falta una acción en la tabla|El código de Yahoo está mal. Abran datos.json en el repositorio y miren la lista<br>“errores”.|
|No salen las fotos|Los nombres deben ser exactamente foto1.jpg y foto2.jpg (no .jpeg ni<br>mayúsculas).|
|La página no muestra el último cambio|Esperen a que termine la ejecución en Actions y recarguen con Ctrl + F5.|
|Yahoo Finance no responde ese día|Ejecuten de nuevo más tarde. La página conserva los últimos datos y muestra<br>su fecha.|



## **Qué entregan** 

|**Entregable**|**Detalle**|
|---|---|
|Enlace de la página|La dirección de GitHub Pages, funcionando|
|Enlace del repositorio|Con los archivos y datos.json actualizado|
|Bitácora de prompts|Cada prompt usado, qué falló y cómo lo corrigieron|
|Sustentación de 7 minutos|Demostración en vivo, el riesgo y la rentabilidad de una acción, y un escenario del<br>simulador|



## **Fuentes** 

- <u>El Tiempo (9 de agosto de 2026): acciones que lideraron la Bolsa en el primer semestre de 2026</u> 

- <u>Valora Analitik: Grupo Cibest comienza a cotizar en la BVC</u> 

- <u>Xataka: cómo editar fotos gratis en Google Gemini</u> 

- <u>Google: Gemini Canvas</u> 

- <u>GitHub Docs: fuente de publicación de GitHub Pages</u> 

- <u>Bolsa de Valores de Colombia</u> y Yahoo Finance: precios y códigos de las acciones 

Asesor de Inversión con IA · Mercado de Capitales · UNIPAZ 

Página 10 

