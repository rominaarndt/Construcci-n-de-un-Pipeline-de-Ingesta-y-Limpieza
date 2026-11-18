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
│
├── data/
│   ├── raw/                  # Datos originales de entrada (CSV)
│   └── processed/            # Datos limpios y procesados (Parquet)
│
├── src/
│   ├── __init__.py           # Inicializador del módulo
│   ├── extract.py            # Módulo de extracción (Lectura con Pandas)
│   ├── transform.py          # Módulo de limpieza y escalado 
│   └── load.py               # Módulo de carga (Exportación a Parquet)
│
├── venv/                     # Entorno virtual de Python
├── main.py                   # Script orquestador principal
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Documentación del proyecto

# Normalizacion 
#Se normalizaron los encabezados a formato snake_case para consistencia en el pipeline. Para el manejo de nulos, se descartaron filas sin identificador clave por representar menos del 1% del total, se imputaron variables numéricas con su mediana para mitigar el impacto de valores extremos, y se asignó 'Desconocido' a las variables categóricas para no perder observaciones."

# Módulo de Limpieza y Transformación de Datos (transform.py)
El script implementa un pipeline de preprocesamiento robusto diseñado para garantizar la integridad, estandarización y calidad de los datos antes de su carga analítica. A continuación se detallan las funciones principales y los criterios aplicados:
⚙️ Módulo de Limpieza y Transformación de Datos (transform.py)El script implementa un pipeline de preprocesamiento robusto diseñado para garantizar la integridad, estandarización y calidad de los datos antes de su carga analítica. A continuación se detallan las funciones principales y los criterios aplicados:
📋 Funciones y Lógica de Transformación1. normalize_column_names(df)Estandariza los nombres de las columnas del DataFrame para asegurar un formato uniforme y evitar errores en consultas o uniones posteriores.
Limpieza de espacios y mayúsculas: Convierte todos los caracteres a minúsculas y elimina espacios iniciales/finales (strip y lower).Reemplazo de separadores: Sustituye los espacios en blanco por guiones bajos (_).
Filtrado de caracteres especiales: Utiliza expresiones regulares (r"[^\w_]") para eliminar símbolos extraños, tildes o puntuación no deseada.2. handle_missing_values(df)Aplica estrategias específicas de tratamiento de valores nulos (missing values) diferenciando entre tipos de datos numéricos y categóricos:Integridad Referencial: Filtra y elimina los registros que carecen de un identificador esencial (id_cliente).
Imputación Numérica: Rellena los valores nulos en columnas numéricas utilizando la mediana (median()) para mitigar el impacto de posibles valores atípicos (outliers).Imputación Categórica: Maneja los nulos en columnas de tipo objeto o categóricas rellenándolos con el texto "Desconocido", añadiendo previamente la categoría si el DataFrame utiliza tipos categóricos estrictos (pd.CategoricalDtype).
3. transform_data(df)Función orquestadora que ejecuta la secuencia completa de preparación de datos:Eliminación de Duplicados: Detecta y descarta filas repetidas, registrando métricas del total de registros depurados.Secuencia de Limpieza: Ejecuta de forma encadenada la normalización de columnas y el tratamiento de nulos.Optimización de Memoria: Convierte de forma masiva las columnas de tipo objeto a tipo category para optimizar el consumo de memoria en datasets de gran volumen.

# 💾 Módulo de Carga y Exportación (load.py)
La etapa final del pipeline ETL se encarga de persistir el conjunto de datos limpio, validado y transformado en un formato optimizado para consultas analíticas de alto rendimiento.
⚙️ Características de la Carga a Parquet
Almacenamiento Columnar: A diferencia de formatos orientados a filas (como CSV), Parquet organiza los datos por columnas, lo que permite lecturas ultrarrápidas y escaneos eficientes en herramientas de Business Intelligence (Power BI, Tableau) y análisis de datos en Python.

Compresión Eficiente: Reduce significativamente el espacio en disco manteniendo la integridad y el tipado estricto de las columnas (como fechas, enteros y categorías).

Preservación del Esquema: Evita la re-inferencia de tipos de datos en lecturas posteriores al almacenar metadatos integrados.