# 🚀 Pipeline de Ingesta y Limpieza de Datos en Data set de Deteccion de fraude bancario (ETL)
# url del dataset https://www.kaggle.com/datasets/nafiulislam490/bank-transaction-fraud-detection-dataset/data

Conjunto de datos para la detección de fraude en transacciones bancarias
Un conjunto de datos bancarios sintéticos a gran escala que simula 1.000.000 de transacciones financieras reales
en 10 países, diseñado para la detección de fraudes y el análisis de riesgos financieros.

Descripción general del conjunto de datos
Filas: 1.000.000
Columnas: 26
Tasa de fraude: ~5,5% (clasificación desequilibrada realista)
Periodo de tiempo: 2020 - 2024

Descripción de las columnas
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
* **Scikit-Learn:** Estandarización de variables numéricas (`StandardScaler`).
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
│   ├── transform.py          # Módulo de limpieza y escalado (StandardScaler)
│   └── load.py               # Módulo de carga (Exportación a Parquet)
│
├── venv/                     # Entorno virtual de Python
├── main.py                   # Script orquestador principal
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Documentación del proyecto