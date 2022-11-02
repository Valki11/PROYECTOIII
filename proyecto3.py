"""
@authors Keila Ramírez <kramireza10@miumg.gt
@description 
@cite 
@license GPL v3
@date 2022/11/03
"""
#importamos la librería tkinder , colocamos el asterisco para exportar todo el paquete.
from tkinter import*
Base=Tk()
from tkinter import ttk
#se coloca el titulo que aparecerá en la ventana.
Base.title ("Proyecto III")
#Le damos un tamaño estándar a la ventana 
Base.geometry("500x480")
#Le damos un color a la ventana, en este caso nos basamos en la tabla de colores html. 
Base.config(background='#A9E2F3')
#le cambiamos el icono, colocando la ruta donde se encuentra nuestra imagen
Base.iconbitmap('C:\\Users\\Compu Fire\\Downloads\\Squirtle.ico')
OurApp=Frame()
OurApp.pack()
OurApp.config(background='#F5F6CE')
OurApp.config(width="400", height="480")
OurApp.config(cursor="heart")

Base.mainloop()
