import tkinter as tk

win = tk.Tk()
win.title("Cine") #Esto es el nombre de la ventana
win.geometry("800x600")
win.configure(bg="#b5bbc4")
tittle = tk.Label(  #Esto es el titulo que se muestra por encima de todo lo demas
    win,
    text = "Bienvenido al cine!",
    font = ("Arial", 20, "bold"),
    fg = "white",
    bg = "#b5bbc4"
    )
entrada_fila = tk.Entry(
    win,
    font = ("Arial", 10),
    width = 30
    )
tittle.pack(pady = 10) #Esto se tiene que poner en cada una de las funciones, sin ello el texto no aparece

entrada_fila.insert(0, "Que fila quieres?") # .insert = campo de texto
entrada_fila.pack(pady = 10)

def clean():
    entrada_fila.delete(0, tk.END)
boton = tk.Button(  #Esto es un boton
    win,
    text = "Limpiar",
    command = clean
    )
boton.pack(pady = 15)
win.mainloop() #Esto siempre va al final de las instrucciones de creacion de ventana