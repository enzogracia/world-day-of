import tkinter as tk
from PIL import Image, ImageTk 

# ==========================================
root = tk.Tk()
root.title("World Day Of")
root.geometry("600x300")
root.minsize(300, 200)

try:
    ico = Image.open('test.jpg')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)
except Exception as e:
    print(f"Icono no cargado: {e}")

titulo = tk.Label(root, text="World Day Of", font=("Arial", 20, "bold"))
titulo.pack(pady=10)

# ==========================================
variable_texto = tk.StringVar()
variable_texto.set("Welcome to World Day Of, check the world days pressing the buttons.")

subtitulo = tk.Label(root, textvariable=variable_texto, font=("Arial", 12), wraplength=500)
subtitulo.pack(pady=10)

# ==========================================

def mostrar_ayer():
    variable_texto.set("Yesterday was: " + "" ) # por cambiar

def mostrar_hoy():
    variable_texto.set("Today is: " + "" ) # por cambiar

def mostrar_manana():
    variable_texto.set("Tomorrow will be: " + "" ) # por cambiar

# ==========================================
frame = tk.Frame(root)
frame.pack(expand=True)

btn_izquierda = tk.Button(frame, text="Yesterday", width=10, height=3, command=mostrar_ayer)
btn_izquierda.pack(side="left", padx=20)

btn_medio = tk.Button(frame, text="Today", width=10, height=3, command=mostrar_hoy)
btn_medio.pack(side="left", padx=20)

btn_derecha = tk.Button(frame, text="Tomorrow", width=10, height=3, command=mostrar_manana)
btn_derecha.pack(side="left", padx=20)

root.mainloop()