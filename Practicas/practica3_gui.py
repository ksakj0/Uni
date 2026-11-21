import tkinter as tk
from tkinter import messagebox

class CineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cine - Sistema de Reserva de Boletos")
        self.root.resizable(False, False)

        # Variables equivalentes a practica3Clean.py
        self.tam = 15
        self.abc = "abcdefghijklmno"
        self.ocupados = 0
        self.total_asientos = self.tam * self.tam

        # Matriz que almacena el estado ('X' = libre, '☻' = ocupado)
        self.cine = [['X' for _ in range(self.tam)] for _ in range(self.tam)]
        self.botones = {}
        self.asiento_seleccionado = None  # Tupla (fila, columna)

        self._crear_interfaz()
        self._actualizar_estadisticas()

    def _crear_interfaz(self):
        # Marco principal
        contenedor = tk.Frame(self.root, bg="#1e272e", padx=20, pady=20)
        contenedor.pack(fill=tk.BOTH, expand=True)

        # Título
        titulo = tk.Label(
            contenedor,
            text="🎬 SALA DE CINE 🎬",
            font=("Arial", 18, "bold"),
            bg="#1e272e",
            fg="#f5f6fa"
        )
        titulo.pack(pady=(0, 10))

        # Indicador de pantalla
        pantalla_frame = tk.Frame(contenedor, bg="#485460", bd=2, relief=tk.RIDGE)
        pantalla_frame.pack(fill=tk.X, pady=(0, 15))
        pantalla_lbl = tk.Label(
            pantalla_frame,
            text="▬▬▬▬▬▬▬▬▬▬▬▬ PANTALLA ▬▬▬▬▬▬▬▬▬▬▬▬",
            font=("Arial", 11, "bold"),
            bg="#485460",
            fg="#d2dae2",
            pady=4
        )
        pantalla_lbl.pack()

        # Marco central para dividir cuadrícula y panel de control
        cuerpo = tk.Frame(contenedor, bg="#1e272e")
        cuerpo.pack()

        # ==================== CUADRÍCULA DE ASIENTOS ====================
        grid_frame = tk.Frame(cuerpo, bg="#1e272e", padx=5, pady=5)
        grid_frame.pack(side=tk.LEFT, padx=(0, 20))

        # Encabezado de letras (A a O)
        for col_idx, letra in enumerate(self.abc):
            lbl_col = tk.Label(
                grid_frame,
                text=letra.upper(),
                font=("Arial", 9, "bold"),
                width=3,
                bg="#1e272e",
                fg="#fbc531"
            )
            lbl_col.grid(row=0, column=col_idx + 1, pady=(0, 3))

        # Filas numeradas (1 a 15) y botones de asientos
        for r in range(self.tam):
            lbl_fila = tk.Label(
                grid_frame,
                text=str(r + 1),
                font=("Arial", 9, "bold"),
                width=3,
                bg="#1e272e",
                fg="#fbc531",
                anchor="e"
            )
            lbl_fila.grid(row=r + 1, column=0, padx=(0, 4))

            for c in range(self.tam):
                btn = tk.Button(
                    grid_frame,
                    text="X",
                    font=("Arial", 8, "bold"),
                    width=2,
                    height=1,
                    bg="#4cd137",
                    fg="#2f3640",
                    activebackground="#44bd32",
                    relief=tk.RAISED,
                    command=lambda f=r, col=c: self.click_asiento(f, col)
                )
                btn.grid(row=r + 1, column=c + 1, padx=1, pady=1)
                self.botones[(r, c)] = btn

        # ==================== PANEL LATERAL DE CONTROL ====================
        panel_lateral = tk.Frame(cuerpo, bg="#2f3640", padx=15, pady=15, relief=tk.GROOVE, bd=2)
        panel_lateral.pack(side=tk.RIGHT, fill=tk.Y)

        # Leyenda visual
        tk.Label(
            panel_lateral,
            text="Leyenda",
            font=("Arial", 11, "bold"),
            bg="#2f3640",
            fg="#f5f6fa"
        ).pack(anchor="w", pady=(0, 5))

        leyenda_box = tk.Frame(panel_lateral, bg="#2f3640")
        leyenda_box.pack(anchor="w", pady=(0, 15))

        # Libre (X)
        tk.Label(leyenda_box, text=" X ", bg="#4cd137", fg="#2f3640", font=("Arial", 8, "bold")).grid(row=0, column=0, padx=(0, 6), pady=2)
        tk.Label(leyenda_box, text="Libre ('X')", bg="#2f3640", fg="#f5f6fa", font=("Arial", 9)).grid(row=0, column=1, sticky="w")

        # Seleccionado
        tk.Label(leyenda_box, text=" • ", bg="#fbc531", fg="#2f3640", font=("Arial", 8, "bold")).grid(row=1, column=0, padx=(0, 6), pady=2)
        tk.Label(leyenda_box, text="Seleccionado", bg="#2f3640", fg="#f5f6fa", font=("Arial", 9)).grid(row=1, column=1, sticky="w")

        # Ocupado (☻)
        tk.Label(leyenda_box, text="☻", bg="#e84118", fg="#f5f6fa", font=("Arial", 8, "bold")).grid(row=2, column=0, padx=(0, 6), pady=2)
        tk.Label(leyenda_box, text="Ocupado ('☻')", bg="#2f3640", fg="#f5f6fa", font=("Arial", 9)).grid(row=2, column=1, sticky="w")

        # Formulario de Reserva
        tk.Label(
            panel_lateral,
            text="Selección de Asiento",
            font=("Arial", 11, "bold"),
            bg="#2f3640",
            fg="#f5f6fa"
        ).pack(anchor="w", pady=(5, 5))

        form_box = tk.Frame(panel_lateral, bg="#2f3640")
        form_box.pack(anchor="w", pady=(0, 10))

        tk.Label(form_box, text="Fila (1-15):", bg="#2f3640", fg="#f5f6fa").grid(row=0, column=0, sticky="w", pady=2)
        self.entry_fila = tk.Entry(form_box, width=7, font=("Arial", 10))
        self.entry_fila.grid(row=0, column=1, pady=2, padx=(5, 0))

        tk.Label(form_box, text="Columna (A-O):", bg="#2f3640", fg="#f5f6fa").grid(row=1, column=0, sticky="w", pady=2)
        self.entry_col = tk.Entry(form_box, width=7, font=("Arial", 10))
        self.entry_col.grid(row=1, column=1, pady=2, padx=(5, 0))

        btn_comprar = tk.Button(
            panel_lateral,
            text="Comprar Boleto",
            bg="#00a8ff",
            fg="#ffffff",
            activebackground="#0097e6",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            command=self.reservar_asiento
        )
        btn_comprar.pack(fill=tk.X, pady=(5, 12))

        # Mensaje de estado
        self.lbl_estado = tk.Label(
            panel_lateral,
            text="Selecciona un asiento",
            font=("Arial", 9, "italic"),
            bg="#2f3640",
            fg="#dcdde1",
            wraplength=180
        )
        self.lbl_estado.pack(fill=tk.X, pady=(0, 15))

        # Estadísticas / Contadores
        tk.Label(
            panel_lateral,
            text="Estadísticas",
            font=("Arial", 11, "bold"),
            bg="#2f3640",
            fg="#f5f6fa"
        ).pack(anchor="w", pady=(5, 4))

        self.lbl_libres = tk.Label(
            panel_lateral,
            text="",
            font=("Arial", 10),
            bg="#2f3640",
            fg="#4cd137",
            anchor="w"
        )
        self.lbl_libres.pack(fill=tk.X, pady=1)

        self.lbl_ocupados = tk.Label(
            panel_lateral,
            text="",
            font=("Arial", 10),
            bg="#2f3640",
            fg="#e84118",
            anchor="w"
        )
        self.lbl_ocupados.pack(fill=tk.X, pady=1)

        # Botón para limpiar / reiniciar sala
        btn_reiniciar = tk.Button(
            panel_lateral,
            text="Reiniciar Sala",
            bg="#718093",
            fg="#f5f6fa",
            font=("Arial", 9),
            cursor="hand2",
            command=self.reiniciar_sala
        )
        btn_reiniciar.pack(fill=tk.X, pady=(15, 0))

    def click_asiento(self, fila, col):
        """Maneja el clic directo en un botón de asiento."""
        # Si el asiento ya está ocupado
        if self.cine[fila][col] == '☻':
            messagebox.showwarning("Asiento ocupado", "Ese asiento ya esta ocupado")
            return

        # Deseleccionar anterior si estaba seleccionado
        if self.asiento_seleccionado and self.asiento_seleccionado != (fila, col):
            prev_f, prev_c = self.asiento_seleccionado
            if self.cine[prev_f][prev_c] == 'X':
                self.botones[(prev_f, prev_c)].config(text="X", bg="#4cd137")

        # Seleccionar el nuevo
        self.asiento_seleccionado = (fila, col)
        self.botones[(fila, col)].config(text="•", bg="#fbc531")

        # Actualizar campos de texto
        letra = self.abc[col].upper()
        self.entry_fila.delete(0, tk.END)
        self.entry_fila.insert(0, str(fila + 1))
        self.entry_col.delete(0, tk.END)
        self.entry_col.insert(0, letra)

        self.lbl_estado.config(
            text=f"Asiento seleccionado: {letra}{fila + 1}",
            fg="#fbc531"
        )

    def reservar_asiento(self):
        """Valida y efectúa la compra/reserva del asiento."""
        fila_str = self.entry_fila.get().strip()
        col_str = self.entry_col.get().strip().lower()

        # Validación de fila numérica
        if not fila_str.isdigit():
            messagebox.showerror("Error", "Fila o columna fuera de rango")
            return

        a = int(fila_str)
        b = col_str

        # Búsqueda de columna (exactamente como en practica3Clean.py)
        col = -1
        for i, j in enumerate(self.abc):
            if j == b:
                col = i
                break

        # Validaciones de rango y ocupación
        if a < 1 or a > self.tam or col == -1:
            messagebox.showwarning("Fuera de rango", "Fila o columna fuera de rango")
            return
        elif self.cine[a - 1][col] == '☻':
            messagebox.showwarning("Asiento ocupado", "Ese asiento ya esta ocupado")
            return
        else:
            # Asignar asiento
            self.cine[a - 1][col] = '☻'
            self.ocupados += 1

            # Actualizar botón gráfico
            btn = self.botones[(a - 1, col)]
            btn.config(text="☻", bg="#e84118", fg="#ffffff", activebackground="#c23616")

            self.asiento_seleccionado = None
            self._actualizar_estadisticas()
            self.lbl_estado.config(
                text=f"¡Asiento {self.abc[col].upper()}{a} reservado!",
                fg="#4cd137"
            )
            messagebox.showinfo("Confirmación", "Asiento reservado")

    def _actualizar_estadisticas(self):
        libres = self.total_asientos - self.ocupados
        self.lbl_libres.config(text=f"Asientos libres: {libres}")
        self.lbl_ocupados.config(text=f"Asientos ocupados: {self.ocupados}")

    def reiniciar_sala(self):
        if messagebox.askyesno("Confirmar", "¿Deseas vaciar la sala de cine?"):
            self.ocupados = 0
            self.asiento_seleccionado = None
            for r in range(self.tam):
                for c in range(self.tam):
                    self.cine[r][c] = 'X'
                    self.botones[(r, c)].config(text="X", bg="#4cd137", fg="#2f3640")
            self._actualizar_estadisticas()
            self.entry_fila.delete(0, tk.END)
            self.entry_col.delete(0, tk.END)
            self.lbl_estado.config(text="Sala reiniciada", fg="#dcdde1")

if __name__ == "__main__":
    root = tk.Tk()
    app = CineGUI(root)
    root.mainloop()
