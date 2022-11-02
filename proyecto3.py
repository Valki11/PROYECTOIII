"""
@authors Keila Ramírez <kramireza10@miumg.gt
@description 
@cite 
@license GPL v3
@date 2022/11/03
"""
#importamos la librería tkinder.
from tkinter import *
import tkinter as tk
from tkinter import filedialog

def app():
    pass
Base=Tk()
#se coloca el titulo que aparecerá en la ventana.
Base.title ("Proyecto III")
#Le damos un tamaño estándar a la ventana 
Base.geometry("500x480")
#Le damos un color a la ventana, en este caso nos basamos en la tabla de colores html. 
Base.config(background='#A9E2F3')
#le cambiamos el icono, colocando la ruta donde se encuentra nuestra imagen
Base.iconbitmap('C:\\Users\\Compu Fire\\Downloads\\Squirtle.ico')
OurApp=Frame(Base)
OurApp.pack(side="left", anchor="n")
etiqueta1=Label(OurApp, text="Bienveni@, qué desea hacer?",background='#F5F6CE',font=("Segoe Script",12))
etiqueta1.pack()
Base.config(cursor="heart")
def abrirArchivos():
    archivo=filedialog.askopenfilename(title="ABRIR",initialdir="C:/", filetypes=(("Archivos pdf","*.pdf"),("Todos los Archivos","*.*"),("Archivos de texto","*.txt")))
    print(archivo)
Button(Base, text="abrir archivo",font=("Segoe Script",9),command=abrirArchivos).pack() 
Base.mainloop()
