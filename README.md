# Clasificación Básica de Calidad del Vino

## 📋 Descripción del Proyecto
Este proyecto tiene como objetivo **clasificar la calidad del vino** utilizando diferentes técnicas de clasificación supervisada. Los datos provienen de características físico-químicas de vinos tintos y blancos, y la calidad se ha dividido en **buena** y **mala** a partir de un umbral predefinido.

El código se encuentra implementado en un **notebook de Jupyter**, utilizando librerías comunes en **Python** como `scikit-learn`, `pandas`, y `matplotlib`.

---

## ⚙️ Técnicas Implementadas

### **1. Preprocesamiento de Datos**
- Carga y exploración del dataset.
- Clasificación binaria de la variable objetivo:
  - **1**: Buena calidad (≥ 6 en la columna `quality`).
  - **0**: Mala calidad.
- Escalado de características numéricas mediante **StandardScaler**.

### **2. Modelos Utilizados**
Se implementaron los siguientes modelos de clasificación:
- **Regresión Logística**.
- **K-Nearest Neighbors (KNN)**.
- **Random Forest Classifier** (Optimizado con GridSearchCV).

### **3. Evaluación de Modelos**
Las métricas utilizadas para evaluar los modelos incluyen:
- **Accuracy**.
- **Precision, Recall, y F1-Score**.
- **Matriz de Confusión**.
- **Curva ROC y AUC**.

Se comparan los resultados para identificar el mejor modelo basado en rendimiento.

---

## 📊 Resultados Obtenidos
Los resultados del análisis y los modelos entrenados mostraron lo siguiente:

1. **Regresión Logística**
   - Accuracy: **74.3%**
   - Buen equilibrio entre precisión y recall.

2. **KNN**
   - Accuracy: **72.6%**
   - Menor rendimiento general, especialmente para la clase **mala calidad**.

3. **Random Forest Classifier**
   - Accuracy: **75.4%**
   - Mejor rendimiento general.
   - AUC: **0.82**.
   - **Random Forest** es seleccionado como el mejor modelo después de optimización con GridSearchCV.

**Visualizaciones Generadas:**
- **Comparación de modelos** (barras de accuracy).
- **Matrices de Confusión**.
- **Curvas ROC-AUC**.

---

## 📂 **Estructura del Proyecto**

```plaintext
mitic-data-science-gonza/
│
├── notebooks/
│   ├── machine_learning/
│   │   ├── regresion/
│   │   │   ├── clasificacion_basica.ipynb    # Notebook principal del análisis
│
├── data/                                     # Datos utilizados en el proyecto (opcional)
│   ├── winequality-red.csv                   # Datos de vino tinto
│   ├── winequality-white.csv                 # Datos de vino blanco
│
├── results/                                  # Resultados y visualizaciones generadas
│   ├── confusion_matrix.png                  # Visualización de matriz de confusión
│   ├── roc_curve.png                         # Visualización de la curva ROC
│   ├── comparison_accuracy.png               # Comparación de accuracy entre modelos
│
├── requirements.txt                          # Dependencias del proyecto
└── README.md                                 # Documentación principal del proyecto


---

🚀 Ejecución del Proyecto
Requisitos Previos
Python 3.8 o superior.
Librerías necesarias:
pandas, numpy, matplotlib, seaborn, scikit-learn.
Instalación de Dependencias
Ejecuta el siguiente comando para instalar todas las dependencias necesarias:

bash
Copiar código
pip install -r requirements.txt
Clonar y Ejecutar el Proyecto
Clonar el repositorio:
bash
Copiar código
git clone https://github.com/gonzalofe/mitic-data-science-gonza.git
cd mitic-data-science-gonza
Abrir y ejecutar el notebook:
bash
Copiar código
jupyter notebook notebooks/machine_learning/regresion/clasificacion_basica.ipynb
Ejecutar las celdas paso a paso:
Cargar los datos desde los archivos CSV.
Preprocesar las características y dividir en entrenamiento/prueba.
Entrenar modelos de clasificación (Logistic Regression, KNN y Random Forest).
Evaluar los modelos con métricas clave (Accuracy, Recall, Precision, F1-Score).
Visualizar resultados como matriz de confusión y curva ROC.
📊 Resultados
Las visualizaciones y resultados clave generados se almacenarán en la carpeta results/, incluidos:

Matriz de Confusión: confusion_matrix.png
Curva ROC: roc_curve.png
Comparación de Accuracy: comparison_accuracy.png
