from tkinter import *

# Iniciar tkinter
aplicacion = Tk()
# Título de la ventana
aplicacion.title("Sistema de facturación")
# Tamaño de la ventana
aplicacion.geometry("1020x630+0+0")
# Evitar modificación de tamaño
aplicacion.resizable(False,False)
# Color de fondo
aplicacion.config(background="burlywood")

# Panel superior
panel_superior = Frame(aplicacion, border=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta título
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturación", foreground="azure4",
                        font=('Dosis', 58), bg='burlywood', width=23)
etiqueta_titulo.grid(row=0, column=0)

# Evitar que la ventana se cierre
aplicacion.mainloop()