# PROYECTOIII
Tercer proyecto del segundo semestre de ingeniera en sistemas UMG
# _Proyecto III_
*****
###### Utilizando el lenguaje de programación Python junto al editor visual studio code , se realizó una aplicación con interfaz gráfica que pueda leer un archivo de texto (.txt, .cpp, .cs, .py, etc.) al presionar la opción dentro del menú. Mostrar elcontenido en pantalla en un área de texto. Se debe preguntar la ruta del archivo que se quiere leer. El contenido leído y mostrado, puede ser modificado por el usuario y debe tener la opción de guardar y guardar como.  
### *Requisitos* 
- version de python: 3.10

## *Instalación*
Visual Studio Code Version 1.72 disponible, recuerda tener presente de que los términos 32 bits y 64 bits se refieren a la forma en que el procesador de una computadora y en este [enlace](https://code.visualstudio.com/download) puedes encontrar la opción que más se acople a tus necesidades.

# Descargar proyecto
```
git clone https://github.com/Valki11/PROYECTOIII.git
```
# Instalación de Python:
Python se puede descargar de manera gratuita de su [página oficial](https://www.python.org/downloads/).
Sobre el instalador haga doble clic. En la ventana que salga es
recomendable dejar las configuraciones por defecto que sugiere
Python:
- Documentation: permite instalar la documentación al cual se
puede acceder sin necesidad de internet.
-  Pip: Es una herramienta que permite integrar paquetes y
librería de terceros.
- Tcl/tk: una librería que permite crear interfaces gráficas para
Python
- Al momento de instalar Python, uno de los factores más
importantes para que se puede ejecutar en cualquier lugar del
Sistema Operativo es la configuración de variables de entorno:
Afortunadamente Python trae una opción para realizar esta
configuración desde la instalación. Por ello es imperativo marcar
la casilla: Add Python to environment variables (Agrega a Python
a las variables de entorno). Teniendo todo ello en cuenta solo
hace falta darle clic a Instalar.
# *Instalar GIT (opcional)*
Si planeas colaborar con otras personas en el código de Python u hospedar el proyecto en un sitio de código abierto (como GitHub), VS Code admite el [control de versiones con GIT](https://code.visualstudio.com/docs/editor/versioncontrol#_git-support).La pestaña Control de código fuente de VS Code realiza un seguimiento de todos los cambios y tiene comandos GIT comunes (agregar, confirmar, enviar cambios e incorporar cambios) integrados directamente en la interfaz de usuario. Primero, debes instalar GIT para alimentar el panel de control de código fuente.

- Descarga e instala GIT para Windows desde el siguiente  [enlace](https://git-scm.com/download/win). 
- Descarga e instala Git para linux desde el siguiente [enlace](https://git-scm.com/download/linux)

- _Existe una guía detallada para la instalación , se le presentará unas series de preguntas para configurar su entorno , si usará todas las opciones predeterminas solo haga clic en "next" cada vez que lo vea, si usted quiere cambiar alguna variable en su entorno puede elegir la que más se acople a sus necesidades._

- Si por algun motivo no está familiarizado con GIT, también están [las guías de GitHub](https://guides.github.com/) las cuales puede utilizar como herramienta de apoyo.

## Tareas comunes :
#### ¿Qué son y cuáles son sus funciones?
-----
##### *Uso de librería Tkinter*
El paquete tkinter («interfaz Tk») es la interfaz por defecto de Python para el kit de herramientas de GUI Tk. Tanto Tk como tkinter están disponibles en la mayoría de las plataformas Unix, así como en sistemas Windows (Tk en sí no es parte de Python, es mantenido por ActiveState).Para indagar mejor sobre la misma está su documentación [oficial](https://docs.python.org/es/3/library/tkinter.html#tkinter-life-preserver).

##### *SCROLLEDTEXT*
tkinter.scrolledtext — Widget de texto desplazado
El módulo tkinter.scrolledtext proporciona una clase del mismo nombre que implementa un widget de texto básico que tiene una barra de desplazamiento vertical configurada para hacer «lo correcto». Usar la clase ScrolledText es mucho más fácil que configurar un widget de texto y una barra de desplazamiento directamente.

##### *MESSAGEBOX*
tkinter.messagebox — Indicadores de mensajes de Tkinter
El módulo tkinter.messagebox proporciona una clase base de plantilla, así como una variedad de métodos convenientes para configuraciones de uso común. Los cuadros de mensaje son modales y devolverán un subconjunto de (Verdadero, Falso, OK, Ninguno, Sí, No) según la selección del usuario. Los estilos y diseños de cuadros de mensajes comunes incluyen, entre otros:
> class tkinter.messagebox.Message(master=None, **options)
Crea un cuadro de mensaje de información predeterminado.

##### FILEDIALOG
El módulo de diálogo de archivos de Python Tkinter le ofrece un conjunto de diálogos únicos para usar cuando se trata de archivos. Tkinter tiene una amplia variedad de diálogos diferentes, pero los de filedialog están diseñados específicamente para la selección de archivos. Y como se esperaba de los cuadros de diálogo, estos se realizan de una manera muy fácil de usar.

A continuación se muestra una lista de todas las diferentes opciones de diálogo disponibles. Asegúrese de importar filedialog desde tkinter como se muestra a continuación. Si desea usar tkinter además de filedialog (que definitivamente lo hará), tendrá que importar tkinter por separado.

>  filedialog.asksaveasfilename()
>  filedialog.asksaveasfile()
>  filedialog.askopenfilename()
>  filedialog.askopenfile()
>  filedialog.askdirectory()
>  filedialog.askopenfilenames()
>  filedialog.askopenfiles()

##### GRID
El método grid nos permite posicionar los widgets en una celda en especifico, indicamos la celda usando el índice de fila y columna correspondiente, el ancho y la altura de cada celda son configurables, además un widget puede ocupar varias celdas si lo deseamos, usando grid podemos crear fácilmente interfaces gráficas de usuario tipo formulario.
Un ejemplo simple, para posicionar el widget w usando el método grid() deberemos indicar como mínimo la fila y la columna donde este se ubicará, de este modo: w.grid(row=1, column=2) en este ejemplo el widget w se ubicará en la celda correspondiente a la fila 1 y la columna 2, los índices de filas y columnas inician de cero.
