# Proyecto 1: Clasificación en Machine Learning

Este repositorio contiene el trabajo realizado como parte del **Proyecto 1** del curso de Ciencia de Datos en MITIC. El objetivo principal fue aplicar técnicas de clasificación para analizar un conjunto de datos, generar modelos predictivos y evaluar su desempeño utilizando métricas clave.

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Objetivos](#objetivos)
3. [Descripción del Conjunto de Datos](#descripción-del-conjunto-de-datos)
4. [Estrategia de Análisis](#estrategia-de-análisis)
5. [Resultados](#resultados)
6. [Visualizaciones Clave](#visualizaciones-clave)
7. [Conclusiones](#conclusiones)
8. [Cómo Ejecutar el Proyecto](#cómo-ejecutar-el-proyecto)

---

## Introducción
En este proyecto, se implementaron y compararon diferentes modelos de clasificación utilizando bibliotecas como `scikit-learn`. Los modelos fueron evaluados con métricas de rendimiento estándar, como **Accuracy**, **Precision**, **Recall**, **F1-Score** y **ROC-AUC**, para seleccionar el mejor modelo basado en el desempeño general.

---

## Objetivos
- Aplicar técnicas de preprocesamiento de datos, como codificación de variables categóricas y escalado.
- Entrenar y evaluar múltiples modelos de clasificación.
- Comparar los modelos utilizando métricas clave.
- Identificar el modelo más adecuado y analizar sus características más importantes.

---

## Descripción del Conjunto de Datos
El conjunto de datos contiene información sobre:
- **Características categóricas**: Género, Categoría de Producto.
- **Características numéricas**: Edad, Cantidad, Precio por Unidad.
- **Objetivo**: Clasificar elementos en múltiples clases según el contexto del problema.

El dataset fue dividido en un 80% para entrenamiento y un 20% para pruebas.

---

## Estrategia de Análisis
1. **Preprocesamiento**:
   - Codificación de variables categóricas mediante `OneHotEncoder`.
   - Escalado de variables numéricas mediante `StandardScaler`.

2. **Modelos Entrenados**:
   - **Regresión Logística**
   - **K-Nearest Neighbors**
   - **Árbol de Decisión**
   - **Random Forest**

3. **Métricas Evaluadas**:
   - **Accuracy**
   - **Precision**
   - **Recall**
   - **F1-Score**
   - **ROC-AUC**

4. **Evaluación**:
   - Se utilizaron curvas ROC para comparar el desempeño multiclase.
   - Se analizaron las matrices de confusión para identificar errores comunes.

---

## Resultados
- **Modelo con mejor desempeño**: Random Forest
- **Métricas del mejor modelo**:
  - **Accuracy**: 99.5%
  - **ROC-AUC**: 100%
  - **Precision**: 99.7%
  - **Recall**: 99.2%

Consulta las visualizaciones clave en la sección de [Visualizaciones Clave](#visualizaciones-clave).

---

## Visualizaciones Clave
1. **Curvas ROC**: Comparación de los modelos evaluados.
2. **Matriz de Confusión**: Desempeño del modelo Random Forest.
3. **Importancia de Características**: Factores más relevantes para el modelo Random Forest.

---

## Conclusiones
- El modelo **Random Forest** demostró ser el más robusto, obteniendo una precisión del 99.7% y un área bajo la curva ROC (AUC) del 100%.
- La **Edad** y el **Precio por Unidad** fueron las características más importantes según el análisis de importancia de características.
- El análisis resaltó la importancia de un preprocesamiento adecuado y una evaluación detallada de las métricas.

---

## Cómo Ejecutar el Proyecto
1. Clonar este repositorio:
   ```bash
   git clone https://github.com/gonzalofe/mitic-data-science-gonza.git
   cd mitic-data-science-gonza/notebooks/machine_learning/Clasificación/Proyecto1
```
2. Instalar las dependencias necesarias:

    ```bash
    conda activate mitic-data-science-setiembre-2024
    pip install -r requirements.txt
```
Ejecutar el notebook:

Abrir proyecto_1_parte_final.ipynb con Jupyter Notebook o Jupyter Lab.
Correr todas las celdas para reproducir el análisis.
## Créditos
Este proyecto fue desarrollado por Gonzalo Ferreira como parte del curso de Ciencia de Datos en MITIC.

# Licencia
Este proyecto está licenciado bajo los términos de la MIT License. Consulta el archivo LICENSE para más detalles.
