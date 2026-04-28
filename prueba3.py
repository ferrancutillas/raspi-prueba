import os
import shutil

ruta_desordenada = "/home/ferran/Descargas"

extensiones = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archivos comprimidos": [".zip", ".rar", ".tar", ".gz", ".7z"],
}

# Variable para verificar si se han encontrado archivos en la carpeta desordenada
archivos_encontrados = False

# Recorre cada archivo en la carpeta desordenada
for archivo in os.listdir(ruta_desordenada):
    #Separa el nombre del archivo y su extensión
    nombre, extension = os.path.splitext(archivo)

    #Si la ruta es un archivo, cambia el valor de archivos_encontrados a True
    if os.path.isfile(os.path.join(ruta_desordenada, archivo)):
         archivos_encontrados = True  
   
    # Separa la categoría de la extension de extensiones y recorre las extensiones de cada categoría
    for extension_categoria, extension_lista in extensiones.items():
        
        # Si la extensión del archivo coincide con alguna de las extensiones de la categoría almacena la plantilla de la ruta correcta.
        if extension.lower() in extension_lista:
            ruta_correcta = os.path.join(ruta_desordenada, extension_categoria)

            # Si la ruta no existe aún la crea
            if not os.path.exists(ruta_correcta):
                os.makedirs(ruta_correcta)

            # Mueve el archivo de la ruta desordenada a la ruta correcta e imprime un mensaje indicando que el archivo ha sido movido
            shutil.move(os.path.join(ruta_desordenada, archivo), os.path.join(ruta_correcta, archivo))
            print(f"Archivo '{archivo}' movido a '{ruta_correcta}'")

# Si no se han encotrado archivo lo muestra por consola
if not archivos_encontrados:
    print("No se han encontrado archivos en la carpeta desordenada.")