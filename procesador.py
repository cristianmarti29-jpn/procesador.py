import os
from datetime import datetime

def filtrar_archivo(ruta_origen, ruta_destino, palabra_clave):
    """
    Lee un archivo de texto o log línea por línea, filtra las líneas
    que contienen la palabra clave y genera un reporte estructurado.
    """
    if not os.path.exists(ruta_origen):
        raise FileNotFoundError(f"El archivo de origen no existe en: {ruta_origen}")

    coincidencias = 0

    # Uso de 'with' para asegurar el cierre correcto de los archivos
    with open(ruta_origen, 'r', encoding='utf-8') as archivo_in:
        with open(ruta_destino, 'w', encoding='utf-8') as archivo_out:
            
            # Escribir encabezado del reporte
            archivo_out.write("=========================================\n")
            archivo_out.write("      REPORTE DE ANÁLISIS DE LOGS        \n")
            archivo_out.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            archivo_out.write(f"Origen: {os.path.basename(ruta_origen)}\n")
            archivo_out.write(f"Término de búsqueda: [{palabra_clave}]\n")
            archivo_out.write("=========================================\n\n")

            # Lectura eficiente línea por línea (No sobrecarga la memoria RAM)
            for num_linea, linea in enumerate(archivo_in, start=1):
                if palabra_clave.lower() in linea.lower():
                    archivo_out.write(f"[Línea {num_linea}]: {linea.strip()}\n")
                    coincidencias += 1
                    
            archivo_out.write(f"\n[-] Fin del reporte. Total coincidencias: {coincidencias}\n")

    return coincidencias