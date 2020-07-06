def logo_principal():
    """
    funcion sin parametros de entrada
    En esta funcion se crea un logo con la libreria turtle con las siguentes caracterisiticas:
    Crea un fractal controlado por recursion 
    Crea la imagen de una calculadora
    Crea la imagen de el nombre del proyecto ()
    Envia mensajes en la ventana de turtle
    Se cierra con un click del usuario 
    """
    def imagen(tortuga):
        """
        parametros:
        tortuga= elemento con el que se va hacer la imagen
        En esta funcion se crea una imagen de una calculadora, unicamente con funciones de turtle, con una funcion que crea cuadrilateros
        """
        def cuadrilateros(tortuga,color,inicio,largo,alto):
            """
            Parametros:
            tortuga= elemento con el que se dibuja la fuente
            color= entero que sirve de indice en una lista
            inicio= lista con las coordenadas iniciales en las que se pone la esquina inferior izquierda del cuadrado
            largo= entero que define el latgo del cuadrilatero
            alto=entero que define el ancho del cuadrilatero
            la funcion es la encargada de usar la libreria turtle para dibujar cuadrilateros y loa rellena
            """
            lista_color = ["snow3","skyblue1","seagreen3"]
            tortuga.speed(100000)
            tortuga.up()
            tortuga.fillcolor(lista_color[color])
            tortuga.goto(inicio[0],inicio[1])
            tortuga.down()
            tortuga.begin_fill()
            tortuga.color(lista_color[color])
            tortuga.goto(inicio[0]+largo,inicio[1])
            tortuga.goto(inicio[0]+largo,inicio[1]+alto)
            tortuga.goto(inicio[0],inicio[1]+alto)
            tortuga.goto(inicio[0],inicio[1])
            tortuga.end_fill()
        tortuga.hideturtle()
        cuadrilateros(tortuga,0,[-100,120],200,300)
        cuadrilateros(tortuga,1,[-80,335],160,60)
        lista = [[-70,250],[-70,150],[20,250],[20,150]]
        for posicion in lista:
            cuadrilateros(tortuga,2,posicion,50,50)
        tortuga.pencolor("black")
        tortuga.pensize(7)
        tortuga.up()
        tortuga.goto(30,275)
        tortuga.down()
        tortuga.goto(60,275)
        tortuga.up()
        tortuga.goto(-60,275)
        tortuga.down()
        tortuga.goto(-30,275)
        tortuga.up()
        tortuga.goto(-45,290)
        tortuga.down()
        tortuga.goto(-45,260)
        tortuga.up()
        tortuga.goto(30,185)
        tortuga.down()
        tortuga.goto(60,185)
        tortuga.up()
        tortuga.goto(30,165)
        tortuga.down()
        tortuga.goto(60,165)
        tortuga.up()
        tortuga.goto(-30,185)
        tortuga.down()
        tortuga.goto(-60,165)
        tortuga.up()
        tortuga.goto(-30,165)
        tortuga.down()
        tortuga.goto(-60,185)
        ceros = [-75,-35,5,45]
        for numero in ceros:
            tortuga.up()
            tortuga.goto(numero,345)
            tortuga.down()
            tortuga.pensize(3)
            tortuga.goto(numero+30,345)
            tortuga.goto(numero+30,390)
            tortuga.goto(numero,390)
            tortuga.goto(numero,345)
    def escribir(tortuga):
        """
        Parametros:
        tortuga= elemento con el que se posiciona los mensajes escritos en pantalla
        la funcion es la encargada de usar la libreria turtle para posicionar mensajes en pantalla, a estos mesajes se les puede introducir valores de fuentes y tamanos de letras
        """
        tortuga.hideturtle()
        tortuga.up()
        tortuga.goto(0,-30)
        tortuga.write("\"fuente de investigacion\"",align=("center"),font=("castellar",20,"normal"))
        tortuga.goto(0,-350)
        tortuga.write("(Haga click en la ventana para continuar)",align=("center"),font=("times new roman",30,"normal"))   
    def fractal(tortuga,espaciador,puntos):
        """
        Parametros:
        tortuga= elemento con el que se dibuja la fuente
        espaciador=entero con el que se se realiza la recursion 
        puntos= lista con los valores que cambian para definir el tamanno y posicion de las lineas
        la funcion usa la recursion de la funcion llamada "koch" para generar lineas horizontales que simulan una fuente
        """
        def dibujar(puntos,tortuga):
            """
            Parametros:
            tortuga= elemento con el que se dibuja la fuente
            puntos= lista de valores con los que se forman las lineas
            la funcion es la encargada de usar la libreria turtle para dibujar las lineas
            """
            tortuga.up()
            tortuga.goto(puntos[0][0],puntos[1][1])
            tortuga.down()
            tortuga.goto(puntos[0][0],puntos[0][1])
            tortuga.goto(puntos[1][0],puntos[1][1])

        def division(lista, valor):
            """
            Parametros:
            lista = lista con los valores de los puntos la cual seran cambiados con esta funcion
            valoer = entero con que sirve de factor para cambiar el valor de los puntos de la lista
            La funcion se encarga de cambiar los valores de la lista de puntos con una division entre el valor
            """
            puntos = [[lista[0][0]/valor,lista[0][1]+30/valor], [lista[1][0]/valor,lista[1][1]+30/valor]]
            return puntos

        def koch(puntos,grado,tortuga):
            """
            Parametros:
            grado = entero que se disminuye para llegar al caso base de la recursion
            tortuga= elemento con el que se dibuja la fuente
            puntos= lista de valores con los que se forman las lineas
            la funcion es la encargada de la recursion de las linaeas para cambiar los valores y posicion, se basa en la teoria del matematico Helge Von Koch para cambiar los valores del
            tamano de las lineas por medio de los puntos
            """
            dibujar(puntos,tortuga)
            if grado > 0:
                for numero in range(2,4):
                    koch(division(puntos,numero),grado-1, tortuga)
        tortuga.hideturtle()
        tortuga.speed(10000)
        koch(division(puntos,3),espaciador,tortuga)
    def nombre(tortuga):
        """
        parametros:
        tortuga= elemento con el que se escribe el nombre del proyecto

        En esta funcion se escribe el nombre del proyecto, unicamente con funciones de turtle, sin funciones adicionales
        """
        tortuga.hideturtle()
        tortuga.up()
        tortuga.goto(-120,-100)
        tortuga.speed(10)
        tortuga.color("black")                             
        tortuga.fillcolor("blue")
        tortuga.up()
        tortuga.down()
        tortuga.begin_fill()
        tortuga.forward(70)
        tortuga.right(90)
        tortuga.forward(20)
        tortuga.right(90)
        tortuga.forward(50)
        tortuga.left(90)
        tortuga.forward(30)
        tortuga.left(90)
        tortuga.forward(30)
        tortuga.right(90)
        tortuga.forward(20)
        tortuga.right(90)
        tortuga.forward(30)
        tortuga.left(90)
        tortuga.forward(60)
        tortuga.right(90)
        tortuga.forward(20)
        tortuga.right(90)
        tortuga.forward(130)
        tortuga.right(90)
        tortuga.forward(70)
        tortuga.right(90)
        tortuga.end_fill()
        tortuga.color("black")
        tortuga.fillcolor("white")
        tortuga.begin_fill()
        tortuga.forward(130)
        tortuga.left(90)
        tortuga.forward(70)
        tortuga.left(90)
        tortuga.forward(20)
        tortuga.left(90)
        tortuga.forward(50)
        tortuga.right(90)
        tortuga.forward(40)
        tortuga.right(90)
        tortuga.forward(30)
        tortuga.left(90)
        tortuga.forward(20)
        tortuga.left(90)
        tortuga.forward(30)
        tortuga.right(90)
        tortuga.forward(30)
        tortuga.right(90)
        tortuga.forward(50)
        tortuga.left(90)
        tortuga.forward(20)
        tortuga.left(90)
        tortuga.forward(70)
        tortuga.end_fill()
        tortuga.right(180)
        tortuga.forward(70)
        tortuga.fillcolor("red")
        tortuga.begin_fill()
        tortuga.forward(20)
        tortuga.right(50)
        tortuga.forward(60)
        tortuga.left(100)
        tortuga.forward(60)
        tortuga.right(50)
        tortuga.forward(20)
        tortuga.right(90)
        tortuga.forward(130)
        tortuga.right(90)
        tortuga.forward(20)
        tortuga.right(90)
        tortuga.forward(100)
        tortuga.left(140)
        tortuga.forward(60)
        tortuga.right(100)
        tortuga.forward(60)
        tortuga.left(140)
        tortuga.forward(100)
        tortuga.right(90)
        tortuga.forward(20)
        tortuga.right(90)
        tortuga.forward(130)
        tortuga.right(180)
        tortuga.forward(130)
        tortuga.end_fill()
    import turtle
    pantalla = turtle.Screen()
    pantalla.title("Logo FEM")
    pantalla.setup(width=800,height=1000)
    pantalla.bgcolor("white")
    a = turtle.Turtle()
    b = turtle.Turtle()
    c = turtle.Turtle()
    d = turtle.Turtle()
    a.pensize(2)
    b.pensize(6)
    c.pensize(2)
    d.pensize(20)
    a.pencolor("green")
    b.pencolor("black")
    c.pencolor("black")
    fractal(a,3,[[-500,10],[500,10]])
    imagen(b)
    nombre(c)
    escribir(d)   
    pantalla.exitonclick()


logo_principal()

