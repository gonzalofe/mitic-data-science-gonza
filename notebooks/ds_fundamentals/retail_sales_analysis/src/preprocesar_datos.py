import numpy as np

def cargar_datos(ruta_archivo):
    # Carga los datos del archivo CSV utilizando NumPy
    datos = np.genfromtxt(ruta_archivo, delimiter=',', skip_header=1)
    return datos

# Preprocesamiento de datos

def verificar_datos_faltantes(datos):
    # Devuelve True si hay valores faltantes, False si no
    return np.isnan(datos).any()

def rellenar_nan_con_media(datos):
    #Calcula la media por columnas ignorando nan
    medias = np.nanmean(datos, axis=0)
    #Rellena con media los datos vacíos
    datos_relleno = np.where(np.isnan(datos), medias, datos)
    return datos_relleno

# Función combinada para preprocesar datos
def preprocesar_datos(ruta_archivo):
    # 1. Cargar los datos
    datos = cargar_datos(ruta_archivo)
    
    # 2. Verificar si hay datos faltantes
    if verificar_datos_faltantes(datos):
        print("Se encontraron valores faltantes. Procediendo a limpiar los datos...")
        datos_relleno = rellenar_nan_con_media(datos)
    return datos_relleno

