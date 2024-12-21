import pandas as pd
import numpy as np

def calculate_na_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the number of non-missing values, missing values, and the percentage of missing values
    for each column in a DataFrame, and return them as a sorted DataFrame.

    Parameters:
    ----------
    df : pd.DataFrame
        The DataFrame for which to calculate NA statistics.

    Returns:
    -------
    pd.DataFrame
        A DataFrame with columns representing:
        - 'datos sin NAs en q': Number of non-missing values for each column
        - 'Na en q': Number of missing values for each column
        - 'Na en %': Percentage of missing values for each column, sorted in descending order.
    """
    qsna = df.shape[0] - df.isnull().sum(axis=0)
    qna = df.isnull().sum(axis=0)
    ppna = np.round(100 * (df.isnull().sum(axis=0) / df.shape[0]), 2)
    aux = {'datos sin NAs en q': qsna, 'Na en q': qna, 'Na en %': ppna}
    na = pd.DataFrame(data=aux)
    return na.sort_values(by='Na en %', ascending=False)

def detect_outliers_iqr(df):
    """
    Detecta valores atípicos en las columnas numéricas de un DataFrame usando el método IQR.

    Args:
        df (pd.DataFrame): DataFrame a analizar.

    Returns:
        dict: Diccionario con el nombre de las columnas como claves y las filas con valores atípicos como valores.
    """
    # Seleccionar solo columnas numéricas
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    if numeric_columns.empty:
        raise ValueError("El DataFrame no contiene columnas numéricas.")

    outliers = {}
    
    # Iterar sobre las columnas numéricas
    for column in numeric_columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        print(f"Columna: {column}, Límite inferior: {lower_bound}, Límite superior: {upper_bound}")
        
        # Filtrar las filas que contienen valores atípicos
        outlier_rows = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
        outliers[column] = outlier_rows

    return outliers
