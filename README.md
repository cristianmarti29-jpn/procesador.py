# GUI Log Analyzer & File Processor 🚀

Un procesador de archivos y analizador de logs automatizado desarrollado en Python con una interfaz gráfica (GUI) responsiva en Modo Oscuro.

Este proyecto implementa buenas prácticas de desarrollo de software, separando la lógica del procesamiento (`Core`) del diseño de la interfaz de usuario (`GUI`).

## ✨ Características de Arquitectura
- **Lectura Eficiente de Stream:** Lee los flujos de archivos línea por línea, evitando la sobrecarga o desbordamiento de la memoria RAM, ideal para archivos `.log` o `.txt` pesados (Gigabytes).
- **Manejo Modular (POO):** Estructurado bajo Programación Orientada a Objetos para facilitar su escalabilidad.
- **Validación Robusta:** Control estricto de excepciones de Entrada/Salida (I/O) y paths inexistentes.

## 🛠️ Tecnologías utilizadas
- **Python 3.x**
- **Tkinter / ttk** (Librería nativa para interfaces de usuario)
- **OS & Datetime Modules** ## 🚀 Instalación y Uso
1. Clona el repositorio:
   ```bash
