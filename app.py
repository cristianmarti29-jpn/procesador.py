import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
# Importamos la lógica del otro archivo
from procesador import filtrar_archivo

class AppProcesador:
    def __init__(self, root):
        self.root = root
        self.root.title("Log Analyzer & File Processor")
        self.root.geometry("550x320")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e") # Fondo oscuro tipo VS Code

        # Variables de control
        self.ruta_entrada = tk.StringVar()
        self.ruta_salida = tk.StringVar()

        # Configuración de estilos para los botones de Tkinter
        estilo = ttk.Style()
        estilo.theme_use('clam')
        estilo.configure('TButton', background='#333333', foreground='#ffffff', borderwidth=0, font=("Arial", 9, "bold"))
        estilo.map('TButton', background=[('active', '#4f4f4f')])

        self.construir_vista()

    def construir_vista(self):
        # Entrada de archivo
        tk.Label(self.root, text="Seleccionar archivo origen (.txt, .log):", bg="#1e1e1e", fg="#00ffcc", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=(15, 2))
        f_entrada = tk.Frame(self.root, bg="#1e1e1e")
        f_entrada.pack(fill="x", padx=20)
        tk.Entry(f_entrada, textvariable=self.ruta_entrada, bg="#2d2d2d", fg="#ffffff", bd=1, insertbackground="white").pack(side="left", expand=True, fill="x", ipady=4)
        ttk.Button(f_entrada, text="Examinar", command=self.cargar_archivo).pack(side="right", padx=(5, 0))

        # Palabra clave
        tk.Label(self.root, text="Palabra o parámetro a buscar (Ej: ERROR, CRITICAL, INFO):", bg="#1e1e1e", fg="#00ffcc", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=(15, 2))
       # CÓDIGO CORREGIDO (Reemplázalo por esto)
        self.entrada_clave = tk.Entry(self.root, bg="#2d2d2d", fg="#ffffff", bd=1, insertbackground="white", font=("Arial", 10), width=25)
        self.entrada_clave.pack(anchor="w", padx=20, ipady=4)
        self.entrada_clave.insert(0, "ERROR")

        # Salida de archivo
        tk.Label(self.root, text="Destino del reporte generado:", bg="#1e1e1e", fg="#00ffcc", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=(15, 2))
        f_salida = tk.Frame(self.root, bg="#1e1e1e")
        f_salida.pack(fill="x", padx=20)
        tk.Entry(f_salida, textvariable=self.ruta_salida, bg="#2d2d2d", fg="#ffffff", bd=1, insertbackground="white").pack(side="left", expand=True, fill="x", ipady=4)
        ttk.Button(f_salida, text="Definir", command=self.definir_salida).pack(side="right", padx=(5, 0))

        # Botón de Acción Principal
        btn_procesar = tk.Button(self.root, text="INICIAR PROCESAMIENTO", bg="#007acc", fg="#ffffff", font=("Arial", 11, "bold"), bd=0, activebackground="#005999", activeforeground="white", command=self.procesar)
        btn_procesar.pack(fill="x", padx=20, pady=(25, 0), ipady=8)

    def cargar_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto/Logs", "*.txt *.log"), ("Todos los archivos", "*.*")])
        if archivo:
            self.ruta_entrada.set(archivo)
            # Autocompletar sugerencia de salida en la misma ruta
            ruta, nombre = os.path.split(archivo)
            self.ruta_salida.set(os.path.join(ruta, f"reporte_{nombre}"))

    def definir_salida(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivo de texto", "*.txt")])
        if archivo:
            self.ruta_salida.set(archivo)

    def procesar(self):
        orig = self.ruta_entrada.get()
        dest = self.ruta_salida.get()
        clave = self.entrada_clave.get().strip()

        if not orig or not dest or not clave:
            messagebox.showwarning("Campos incompletos", "Por favor rellena todos los campos antes de ejecutar.")
            return

        try:
            total = filtrar_archivo(orig, dest, clave)
            messagebox.showinfo("Proceso Exitoso", f"Análisis completado.\nSe encontraron {total} coincidencias de '{clave}'.\nReporte guardado con éxito.")
        except Exception as e:
            messagebox.showerror("Error de Ejecución", f"No se pudo procesar el archivo:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppProcesador(root)
    root.mainloop()