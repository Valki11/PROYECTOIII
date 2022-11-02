#importamos la librería tkinder , colocamos el asterisco para exportar todo el paquete.
from tkinter import*
Base=Tk()
#se coloca el titulo que aparecerá en la ventana.
Base.title("Proyecto III")
#Le damos un tamaño estándar a la ventana 
Base.geometry("500x480")
#Le damos un color a la ventana, en este caso nos basamos en la tabla de colores html. 
Base.config(background='#CEE3F6')
#le cambiamos el icono 
Base.iconbitmap('C:\\Users\\Compu Fire\\Downloads\\Squirtle.ico')

Base.mainloop()
