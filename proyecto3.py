"""
@author Keila Ramírez <kramireza10@miumg.gt
@description 
@cite este código está basado en el siguiente enlace https://www.tutorialesprogramacionya.com/pythonya/
@license 
@date 2022/09/03
"""
import sys
import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
from tkinter import filedialog as fd

class Proyecto:

    def __init__(self):
        self.base=tk.Tk()
        self.agregar_nuevomenu()
        #Le damos tamaño y color a la ventana de texto usando la tabla de colores html. 
        self.scrolledtext1=st.ScrolledText(self.base, width=50, height=30,background='#F7F8E0')
        self.scrolledtext1.grid(column=0,row=0,padx=15,pady=15)
        #se coloca el titulo que aparecerá en la ventana.
        self.base.title ("Proyecto III")
        #Le damos un tamaño estándar a la ventana 
        self.base.geometry("460x520")
        #Le damos un color a la ventana, en este caso nos basamos en la tabla de colores html. 
        self.base.config(background='#A9E2F3')
        #le cambiamos el icono, colocando la ruta donde se encuentra nuestra imagen
        self.base.iconbitmap('C:\\Users\\Compu Fire\\Downloads\\Squirtle.ico')
        #le cambiamos el icono al cursor.
        self.scrolledtext1.config(cursor="heart")
        self.base.mainloop()

    def agregar_nuevomenu(self):
        menu1 = tk.Menu(self.base)
        self.base.config(menu=menu1)
        options = tk.Menu(menu1, tearoff=1)
        options2=tk.Menu(menu1, tearoff=1)
        options.add_command(label="Guardar archivo como", background="#ADD8E6", foreground="#FF0000", activebackground="#32CDFF", command=self.guardarcomo)
        options.add_separator()
        options.add_command(label="Guardar archivo", background="#ADD8E6", foreground="#FF0000", activebackground="#32CDFF", command=self.guardar)
        options.add_command(label="abrir archivo", background="#ADD8E6", foreground="#FF0000", activebackground="#32CDFF", command=self.abrir)
        options2.add_command(label="manual de usuario", background="#ADD8E6", foreground="#FF0000", activebackground="#32CDFF",command=self.link_clicked)
        options2.add_command(label="información", background="#ADD8E6", foreground="#FF0000", activebackground="#32CDFF",command=self.info)
        options.add_separator()
        options.add_command(label="Salir", command=self.salir)
        menu1.add_cascade(label="Archivo", menu=options)  
        menu1.add_cascade(label="Ayuda", menu=options2)  
        menu1.add_cascade(label="Editar", menu=options2)  

    def salir(self):
        sys.exit(0)
    
    def guardar(self):
        nombrearch=fd.SaveAs(initialdir = "C:\\Users\\Compu Fire\\OneDrive\\Escritorio\\tkinder",title = "Guardar ")
    def guardarcomo(self):
        nombrearch=fd.asksaveasfilename(initialdir = "C:\\Users\\Compu Fire\\OneDrive\\Escritorio\\tkinder",title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*"),("Archivos pdf","*.pdf")))
        if nombrearch!='':
            archi1=open(nombrearch, "w", encoding="utf-8")
            archi1.write(self.scrolledtext1.get("1.0", tk.END))
            archi1.close()
            mb.showinfo("notify!", "Proceso finalizado con éxito")

    def abrir(self):
        nombrearch=fd.askopenfilename(initialdir = 'C:\\Users\\Compu Fire\\OneDrive\\Escritorio\\tkinder' ,title = "Seleccione archivo",filetypes = (("Archivos pdf","*.pdf"),("txt files","*.txt"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "r")
            contenido=archi1.read()
            archi1.close()
            self.scrolledtext1.delete("1.0", tk.END) 
            self.scrolledtext1.insert("1.0", contenido)
            
    def link_clicked(self):
        import webbrowser
        webbrowser.open("https://github.com/Valki11/PROYECTOIII.git")
    def info(self):
        import webbrowser
        webbrowser.open("C:\\Users\\Compu Fire\\OneDrive\\Escritorio\\tkinder\\información.txt") 
        
            
    
App=Proyecto()
