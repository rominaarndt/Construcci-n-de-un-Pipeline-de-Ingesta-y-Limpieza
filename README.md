# 🚀 Pipeline de Ingesta y Limpieza de Datos en Data set de Deteccion de fraude bancario (ETL)
# url del dataset https://www.kaggle.com/datasets/nafiulislam490/bank-transaction-fraud-detection-dataset/data

# Conjunto de datos para la detección de fraude en transacciones bancarias
Un conjunto de datos bancarios sintéticos a gran escala que simula 1.000.000 de transacciones financieras reales
en 10 países, diseñado para la detección de fraudes y el análisis de riesgos financieros.

# Descripción general del conjunto de datos
Filas: 1.000.000
Columnas: 26
Tasa de fraude: ~5,5% (clasificación desequilibrada realista)
Periodo de tiempo: 2020 - 2024

# Descripción de las columnas
Columna	Descripción
ID de transacción: identificador único de transacción
ID del cliente: identificador único de cliente
fecha_de_transacción: Fecha de la transacción
tiempo_de_transacción: Hora de la transacción
hora_del_día: Hora (0–23)
es_fin_de_semana: 1 si es fin de semana, 0 si es día laborable
es_transacción_nocturna: 1 si es entre las 10 PM y las 6 AM
país: País del cliente
ciudad: Ciudad del cliente
categoría_comercio: Tipo de comercio (supermercado, electrónica, etc.)
método_de_pago: Tarjeta de crédito, tarjeta de débito, móvil, etc.
tipo_de_dispositivo: Terminal móvil, de escritorio, cajero automático y punto de venta.
edad_del_cliente: Edad del cliente
puntaje_de_crédito: Puntuación crediticia (300–850)
edad_de_la_cuenta_años: Cuánto tiempo lleva existiendo la cuenta.
saldo_de_cuenta: Saldo de la cuenta corriente
importe_de_transacción: Importe de la transacción
num_transacciones_anteriores: Total de transacciones anteriores
frecuencia_de_transacciones_mensual: Transacciones promedio por mes
distancia_desde_casa_km: Distancia desde la ubicación del domicilio del cliente
tiempo_desde_la_última_transacción_horas: Horas transcurridas desde la última transacción
es_internacional: 1 si se trata de una transacción internacional
intentos fallidos: Intentos fallidos de inicio de sesión/transacción
pin_changed_recently: 1 si el PIN cambió recientemente
es_fraude	Objetivo: 1 = Fraude, 0 = Legítimo
tipo_de_fraude: Tipo de fraude (phishing, clonación de tarjetas, etc.)

Este repositorio contiene un pipeline ETL modular desarrollado en Python. Su objetivo es automatizar la lectura de un dataset crudo, aplicar procesos de limpieza, estandarización de variables y exportar los datos optimizados para análisis o modelos de Machine Learning.

---

## 🛠️ Tecnologías y Librerías Utilizadas
* **Python 3.11+**
* **Pandas:** Procesamiento y manipulación de estructuras tabulares.
* **PyArrow:** Exportación e importación eficiente en formato columnar Parquet.

---

## 📂 Estructura del Proyecto

Construcci-n-de-un-Pipeline-de-Ingesta-y-Limpieza/

├── data/
│   ├── raw/
│   │   └── dataset.csv
│   └── processed/
│       └── dataset_procesado.parquet
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── main.py
├── requirements.txt
└── README.md

Cómo ejecutar el pipeline

1-Clonar el repositorio y entrar en la carpeta del proyecto:

Bash
git clone <URL_DEL_REPOSITORIO>
cd Construcci-n-de-un-Pipeline-de-Ingesta-y-Limpieza

2-Crear y activar un entorno virtual (recomendado) e instalar dependencias:

python -m venv venv
# En Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# En Linux / macOS:
source venv/bin/activate

pip install -r requirements.txt

3-Ejecutar el pipeline completo:

python main.py
Esto leerá data/raw/dataset.csv, ejecutará la limpieza y generará data/processed/dataset_procesado.parquet.

· Descripción de las etapas

src/extract.py (extract_data): Carga el archivo CSV de origen (data/raw/dataset.csv) en un DataFrame de pandas aplicando un diccionario dtypes optimizado a las columnas del dataset e informa la cantidad de filas y columnas cargadas.

src/transform.py (clean_data): Realiza una copia defensiva del DataFrame, normaliza los nombres de las columnas a formato snake_case (minúsculas, sin espacios ni caracteres especiales), imputa los valores faltantes en columnas numéricas y categóricas, elimina filas duplicadas exactas y muestra un resumen de la limpieza.

src/load.py (save_to_parquet): Crea automáticamente el directorio de destino si no existe (os.makedirs(..., exist_ok=True)) y guarda el DataFrame limpio en data/processed/dataset_procesado.parquet sin incluir el índice (index=False).

main.py (main): Orquesta el flujo completo conectando extract_data, clean_data y save_to_parquet con las rutas de entrada y salida definidas.

Justificación técnica

¿Por qué exportar a formato Parquet?
Compresión columnar: Parquet almacena los datos por columnas en lugar de por filas, lo que agrupa valores similares y logra una compresión mucho más eficiente que el CSV tradicional.

Lectura más rápida: Permite leer únicamente las columnas necesarias y aprovecha metadatos y codificación por bloque, acelerando los tiempos de carga frente a parsear texto plano en CSV.

Menor peso para Machine Learning: Reduce el espacio en disco y acelera la iteración en flujos de entrenamiento o experimentación con grandes volúmenes de registros.

Criterio para tratar nulos y optimizar memoria

Optimización de tipos en la ingesta (dtypes): Se asignan tipos ajustados en extract_data (como float32, int32/int16/int8 y category para variables categóricas como fraud_type) en lugar de depender siempre de tipos por defecto de mayor tamaño (float64, int64, object), reduciendo el consumo de memoria RAM desde la lectura.

Imputación de valores nulos:

En columnas numéricas, los nulos se completan con la mediana (median()), ya que es más robusta frente a valores atípicos (outliers) o distribuciones asimétricas que la media.

En columnas categóricas (incluyendo object y category), los nulos se imputan con "Desconocido" (añadiendo previamente la categoría si el tipo es CategoricalDtype) para conservar las filas sin perder información ni romper el tipo categórico.

Eliminación de duplicados: 

Se aplica drop_duplicates() para evitar registros repetidos que puedan sesgar estadísticas descriptivas o entrenamientos posteriores.



