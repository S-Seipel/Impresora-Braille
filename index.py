import tkinter as tk
from logica_braille import texto_a_braille, render_braille_ascii

color_fondo = "#96b397"
color_input = "#c8cfae"
color_texto = "#1c1c1c"
fuente_general = ("Segoe UI", 12)
fuente_titulo = ("Segoe UI", 14, "bold")

ventana = tk.Tk()
ventana.title("IMPRESORA A BRAILLE")
ventana.attributes("-fullscreen", True)
ventana.configure(bg=color_fondo)

label_titulo = tk.Label(
    ventana,
    text="Escribí lo que quieras traducir a braille:",
    font=fuente_titulo,
    bg=color_fondo,
    fg=color_texto
)
label_titulo.pack(pady=(20, 10))

entry_texto = tk.Entry(
    ventana,
    width=50,
    font=fuente_general,
    bg=color_input,
    fg=color_texto,
    relief=tk.FLAT,
    highlightthickness=2,
    highlightbackground="#7b8c6f",
    insertbackground=color_texto
)
entry_texto.pack(pady=(0, 20), ipady=6)

salida_braille = tk.Text(
    ventana,
    height=15,
    font=("Courier New", 16),
    bg=color_input,
    fg=color_texto,
    relief=tk.FLAT,
    highlightthickness=1,
    highlightbackground="#7b8c6f"
)
salida_braille.pack(fill="both", expand=True, padx=20, pady=10)


def traducir():
    texto = entry_texto.get()
    celdas = texto_a_braille(texto)
    dibujo = render_braille_ascii(celdas)
    salida_braille.delete(1.0, tk.END)
    salida_braille.insert(tk.END, dibujo)

boton_traducir = tk.Button(
    ventana,
    text="Traducir",
    command=traducir,
    font=("Segoe UI", 12, "bold"),
    bg=color_input,
    fg=color_texto,
    relief=tk.FLAT,
    padx=20,
    pady=8,
    highlightthickness=1,
    highlightbackground="#7b8c6f"
)
boton_traducir.pack(pady=(20, 30))

ventana.mainloop()
