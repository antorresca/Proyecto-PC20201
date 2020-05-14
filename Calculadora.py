#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Usar 4 espacios para dentado

def matematicas():
    """
    Menú de las funciones propias de la matemática
    """
    print('''ELIJA UNA FUNCIÓN: 
            \t 1)Suma
            \t 2)Resta
            \t 3)Multiplicación
            \t 4)División
            \t 5)Potenciación
            \t 6)Radicación
            \t 7)Ecuacion cuadratica
            \t 8)Derivacion
            ''')
    mate = int(input())
    if mate == 1:
        sumar()
    elif mate == 2:
        restar()
    elif mate == 3:
        multiplicar()
    elif mate == 4:
        dividir()
    elif mate == 5:
        potenciar()
    elif mate == 6:
        radicar()
    elif mate == 7:
        ecuacion_cuadratica()
    elif mate == 8:
        derivar()
    else:
        volver_al_menu()

def fisica():
    """ 
    En la funcion 'fisica' se imprime un menu con las areas de la fisica que la calculadora,
    por el momento acepta 4 areas. Esta funcion opera por medio de una cadena de ifs y elfis, la 
    cual, acepta un numero que se asocia con  la rama en el print se menu de inicio de fisica al usuario. 
    """ 
    print (""" Por favor, definir el numero de la rama:
    1) Cinematica
    2) Dinamica
    3) Electromagnetismo
    4) Ondas
    """)
  Rama = int(input())
  
  if Rama == 1:
    cinematica()
  elif Rama == 2:
    dinamica()
  elif Rama == 3:
    print('electromagnetismo')
  elif Rama == 4:
    print('ondas')
  else:
    print("Rama no encontrada, Por favor, ingrese los datos nuevamente")
    fisica()   
   
def estadistica():
  """
  Menú de funciones propias de la estadística

  :param n: Número de datos a analizar, estos se almacenan en una lista
  :param xi: Dato que será almacenado en la lista 
  :param Funcion: Número que corresponde a una funcion determinada en la lista
  :param PM: Se presenta en algunas funciones para elegir si se desea saber el valor poblacional o muestral

  """
  Datos = []
  print('Ingrese cantidad de valores: ')
  n = int(input())
  for i in range(n):
    xi = float(input())
    Datos.append(xi)
  Datos.sort()
  print('''ELIJA UNA FUNCIÓN: 
    \t 1)Media
    \t 2)Mediana
    \t 3)Varianza
    \t 4)Desviación estandar
    \t 5)Coeficiente de variación
    \t 6)Percentiles
    \t 7)Cuartiles
    ''')
  Funcion = int(input())
  if Funcion == 1:
    promedio = MediaAritmetica(Datos)
    print('Promedio =',promedio)
    volver_al_menu()
  elif Funcion == 2:
    mediana = Mediana(Datos)
    print('Mediana =',mediana)
    volver_al_menu()
  elif Funcion == 3:
    print('''Elija una opción:
    \t 1) Poblacional
    \t 2) Muestral
    ''')
    PM = int(input())
    varianza = Varianza(Datos, PM)
    print('Varianza =',varianza)
    volver_al_menu()
  elif Funcion == 4:
    print('''Elija una opción:
    \t 1) Poblacional
    \t 2) Muestral
    ''')
    PM = int(input())
    s = DesviacionEstandar(Datos, PM)
    print('Desviacion =',s)
    volver_al_menu()
  elif Funcion == 5:
    print('''Elija una opción:
    \t 1) Poblacional
    \t 2) Muestral
    ''')
    PM = int(input())
    CV = CoeficienteDeVariacion(Datos, PM)
    print('C.V. ='+str(CV)+'%')
    volver_al_menu()
  elif Funcion == 6:
    Percentiles(Datos)
    volver_al_menu()
  elif Funcion == 7:
    Cuartiles(Datos)
    volver_al_menu()

def quimica():
    """ 
    *EN CONSTRUCCION*
    Funcion con el menu de las areas de la quimica
    :param area:numero entero de la opcion de la rama
    """ 
    print (""" Definir la rama:
            1) Estequiometria
            2) Gases ideales
            3) Equilbrios quimicos
            4) Enlaces intarmoleculares
    """)
    Area = int(input())
    if Area == 1:
        print('estequiometria')
    elif Area == 2:
        print('gases')
    elif Area == 2:
        print('equilibrios')
    elif Area == 2:
        print('enlaces')
    else:
        print("Rama no encontrada, Por favor, ingrese los datos nuevamente")
    print('*EN CONSTRUCCION*')
    volver_al_menu()  
    
def sumar():
    """
    Funcion de sumar cierta cantidad de numeros ingresados por el usuario
    """
    suma = 0
    print('Ingrese los valores a sumar')
    m = input()
    if '+' in m:
        numeros = list(map(float, (m.split('+'))))
    else:
        numeros = list(map(float, (m.split())))
    for i in numeros:
        suma += i
    print('El resultado total de la suma es: ', suma)
    volver_al_menu()

def restar():
    """
    Funcion para restar cierta cantidad de numeros ingresados por el usuario
    :param n: cantidad de numeros que el usuario quiere sumar
    :param a: numeros que se sumaran
    """
    print("ingrese los numeros que se van a restar separados por un espacio: ")
    numeros = list(map(float, (input().split())))
    resta = 0
    for i in range(len(numeros)):
        if i == 0:
            resta = numeros[i]
        else:
            resta -= numeros[i]
    print('El resultado es:',resta)
    volver_al_menu()

def multiplicar():
    """
    Funcion para multiplicar la cantidad de numeros que desee el usuario
    """
    print('Ingrese los numeros que desea multiplicar')
    m = input()
    if '*' in m:
        numeros = list(map(float, (m.split('*'))))
    else:
        numeros = list(map(float, (m.split())))
    mult = 1
    for j in numeros:
        mult *= j
    print('el resultado de su multiplicaión es: ',mult)
    volver_al_menu()

def dividir():
    """
    Funcion para dividir cierta cantidad de elementos
    """
    print('Ingrese la cantidad de numeros que desea dividir')
    d = int(input())
    division = 1
    for h in range(d):
        print('ingrese numero [',h+1,']:')
        num = float(input())
        if num == 0:
            print('el numero que ingresó es 0,No es posible dividir entre 0')
            break
        elif h == 0:
            division = num
        else:
            division = division/num
    if division == 0:
        volver_al_menu()
    else:
        print('su respuesta en decimal es: ',division,'y en entero es:',int(division))
    volver_al_menu()

def potenciar():
    """
    Funcion para encontrar la potencia de un numero
    """
    print('Ingrese la base:')
    base = float(input())
    print('ingrese exponente')
    exp = float(input())
    resultado= base**exp
    print(str(base)+'^'+str(exp)+'='+str(resultado))
    volver_al_menu()

def radicar():
    """
    Funcion para sacarle la raiz a un numero que el usuario de
    """
    print('Ingrese el radicando: ')
    nume = float(input())
    print('Ingrese el indice: ')
    ind = float(input())
    raiz = nume**(1/ind)
    print(str(ind)+'√'+str(nume)+'='+str(raiz))
    volver_al_menu()

def ecuacion_cuadratica():
    """
    Funcion para resolver ecuaciones de segundo grado
    :param ecuacion: str de la expresion algebraica
    """
    print("""Escriba su ecuacion
          (con formato= Cv^2+/-Cv+/-C=C
          donde C es el coeficiente y v es la variable)
          """)
    ecuacion = input()
    abcedario = 'abcdefghijklmnopqrstuwxyz'
    variable = ''
    for x in abcedario:
        if x in ecuacion:
            variable = x
    ec,igualdad = ecuacion.split('=')
    lista = []
    f = 0
    if igualdad != '0':
        igualdad = int(igualdad)*-1
        ec = ec+str(igualdad)+'=0'
    for j in range(len(ec)):
        if ec[j] == '+':
            lista.append([ec[f:j]])
            f = j
        elif ec[j] == '-':
            lista.append([ec[f:j]])
            f = j
        elif ec[j] == '=':
            lista.append([ec[f:j]])
            f = j
    copia = lista[:]
    c = 0
    for g in range(len(copia)):
        for l in copia[g]:
            a = lista.pop()
            for n in a:
                v = n.split(variable)
                if '' in v:
                    b = int(v[0])
                elif '^2' in v:
                    a = int(v[0])
                else:
                    c += int(v[0])
    sqrt = ((b**2-(4*a*c))**0.5)
    cuadratica1 = (((-1)*b)+sqrt)/(2*a)
    cuadratica2 = (((-1)*b)-sqrt)/(2*a)
    if type(cuadratica1) == complex or type(cuadratica2) == complex:
        print('NO TIENE RESPUESTA DENTRO DE LOS REALES')
    else:
        print(variable+'[1]='+str(cuadratica1)+'\n'+variable+'[2]='+str(cuadratica2))
    volver_al_menu()

def derivar():
    """
    Funcion para derivar monomios, es decir hallar la recta tangente a una funcion con centro en (0,0)
    :param funcion: Str con la funcion a derivar
    """
    lista = []
    variable = ''
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    print('Ingrese su función (monomio)')
    funcion = input()
    for l in abecedario:
        if l in funcion:
            variable = l
    if '^' in funcion:
        lista = list(map(float, funcion.split(variable+'^')))
    else:
        for k in range(len(funcion)):
            if k == 0:
                lista.append(funcion[k])
    base = 0
    exp = 0
    if len(lista) == 1:
        base = int(lista[0])
        exp = 1
    else:
        for j in range(len(lista)):
            if j == 0:
                base = int(lista[j])
            elif j == 1:
                exp = int(lista[j])
    b = str(base*exp)
    e = exp-1
    if e == 0:
        print(b) 
    elif e == 1:
        print(b+variable)
    elif e < 0:
        print(b+'/'+variable+'^'+str(e*-1))
    else:
        print(b+variable+'^'+str(e))
    volver_al_menu()
    
def volver_al_menu():
    """
    Funcion para volver a el menu principal del programa
    :param respuesta: Entrada string del usuario frente a la pregunta
    """
    print('¿Desea regresar al menú principal?')
    respuesta = input()
    if respuesta == 'si' or respuesta == 'Si' or respuesta == 'SI' or respuesta == 's' or respuesta == 'S' or respuesta == 'Yes' or respuesta == 'YES' or respuesta == 'Y' or respuesta == 'Y':
        main()
    else:
        print('Vuelva pronto!')

def cinematica(): 
  """
  La funcion cinematica tiene como proposito direccionar a las funciones contenidas
   en esta, las cuales son las que realizan los calculos. Esta tiene una lista llamada
   'lista_funciones_cinematica' con posibles constantes que pueden ser invocadas, 
   asi como funciones que se usan dentro de las funciones de calculo como 'sumatoria'.
   Esta tiene como entrada un string con el nombre de la variable a conocer.   
  """
  
  def sumatoria(variable_a_sumar):
    """
    La funcion sumatoria es una funcion interna, la cual sirve para varias 
    funciones de calculo dentro de la funcion 'cinematica', esta se llama en cada una
     de las funciones. 
    """
    print('Por favor, ingresar las magnitudes de', variable_a_sumar,' en su respectiva medidia del S.I y terminar con (0)')
    Sumatoria = 0
    while True:
      magnitud = float(input())
      if magnitud == 0:
        break
      Sumatoria += magnitud
    return(Sumatoria)

  def distancia():
    """
    funcion de calculo que se apoya en la funcion "sumatoria" para calcular la 
    distancia segun la ecuacion distancia = velocidad x tiempo.

    """
    velocidad=sumatoria('velocidad')
    print ("Por favor, defina la magnitud en segundos del tiempo:")
    tiempo = int(input())
    distancia = velocidad * tiempo
    print("La distancia es", distancia,"metros")
    volver_al_menu()

  def velocidad():
    """
    funcion de calculo que se apoya en la funcion "sumatoria" para calcular la 
    velocidad segun la ecuacion velocidad = distancia / tiempo.
    """
    desplazamiento=sumatoria('desplazamiento')
    print ("Por favor, defina la magnitud en segundos del tiempo:")
    tiempo = int(input())
    velocidad = desplazamiento/tiempo
    print("La velocidad es ", velocidad,"metros/segundo")
    volver_al_menu()

  def aceleracion():
    """
    funcion en la cual se piden dos valores, velocidad y tiempo para conocer una 
    aceleracion segun la ecuacion aceleracion = velocidad / tiempo
    """
    print ("Por favor, defina la magnitud en metros/segundo de la velocidad:")
    velocidad = int(input())
    print ("Por favor, defina la magnitud en segundos del tiempo:")
    tiempo = int(input())
    aceleracion = velocidad/tiempo
    print("La aceleracion es ", aceleracion,"metros/segundo^2")
    volver_al_menu()
  
  print ("""
   Por favor, definir la incognita:
   Un string que sea la variable fisica a encontar o el fenomeno fisco a comprender.
  """)
  Incognita = str(input()) 
  Incognita = Incognita.upper()  
  if Incognita == "DISTANCIA":
    distancia()
  elif Incognita == "VELOCIDAD":
    velocidad()
  elif Incognita == "ACELERACION":
    aceleracion()
  else:
    print("Variable o proceso no encontrado")
    volver_al_menu()
    
def dinamica():
  """
  por definir
  """
  print()

def MediaAritmetica(Datos):
  """
  Funcion que permite calcular la media de una lista de datos
  La lista suma cada uno de los datos y los divide entre el número de datos
  """
  sumaprom = 0
  for i in range(len(Datos)):
    sumaprom += Datos[i]
  promedio = round((sumaprom/len(Datos)),2)
  return promedio
    
def Mediana(Datos):
  """
  En caso de que el número de datos sea impar, retorna el dato en la posición central
  En caso de ser par, retorna el promedio entre los dos datos centrales
  """
  if len(Datos) % 2 == 0:
    mediana = round(((Datos[(len(Datos)-1)/2]+Datos[len(Datos)/2])/2),2)
    return mediana
  else:
    mediana = Datos[int(len(Datos)/2)]
    return mediana

def Varianza(Datos, PM):
  """
  Dependiendo del valor del parámetro PM calcula la varianza poblacional o muestral
  Llama a la cunción MediaAritmetica()
  Suma los cuadrados del resultado de restar el dato en la posición i con la mediana
  En caso de ser poblacional el valor se divide por n y si es muestral se divide por n-1
  Y retorna el valor varianza con 2 decimales

  """
  promedio = MediaAritmetica(Datos)
  if PM == 1:
    sumvarianza = 0
    for i in range(len(Datos)):
        sumvarianza += ((Datos[i]-promedio)**2)
    varianza = round((sumvarianza/len(Datos)),2)
    return varianza
  elif PM == 2:
    sumvarianza = 0
    for i in range(len(Datos)):
      sumvarianza += ((Datos[i]-promedio)**2)
    varianza = round((sumvarianza/(len(Datos)-1)),2)
    return varianza

def DesviacionEstandar(Datos, PM):
    """
    Llama a la funcion Varianza() y calcula la raíz cuadrada del valor varianza
    Retorna el valor s (Desviacion Estandar) con 2 decimales
    """
    varianza = Varianza(Datos,PM)
    s = round((varianza**0.5),2)
    return s

def CoeficienteDeVariacion(Datos, PM):
  """
  Llama a la funcion DesviacionEstandar()
  Divide el valor s entre el valor promedio, este se multiplica por 100 para obtenes el valor de porcentaje
  Retorna el valor CV con dos decimales

  """
  s = DesviacionEstandar(Datos, PM)
  promedio = MediaAritmetica(Datos)
  CV = round(((s/promedio)*100),2)
  return CV

def Percentiles(Datos):
  """
  :param k: Número que corresponde al percentil que se desea buscar, este número debe estar entre 1 y 99
  En caso de que el número de datos sea impar, imprime el dato en la posición correspondiente del percentil
  En caso de ser par, imprime el promedio entre los dos datos cercanos a las posición correspondiente al percentil
  """
  print('Ingrese el percentil:')
  k = int(input())
  if (k > 0) and (k <= 100):
    if len(Datos)%2 != 0:
      print('P'+str(k)+' =',Datos[int((k*(len(Datos)+1)/100)-1)])
    else:
      print('P'+str(k)+' =',round((Datos[(int(k*(len(Datos)+1)/100))-1]+Datos[(int(k*(len(Datos)+1)/100))]/2),2))
  else:
    print('ERROR')
  volver_al_menu()
  
def Cuartiles(Datos):
    """
    Menú de cuartiles
    :param k: Número que corresponde a una función determinada en el menú
    En caso de que el numero de datos sea sea impar, mprime el dato correspondiente a la posición de cada cuartil
    En caso de que el numero de datos sea par, imprime el promedio de los datos cercanos a la posición del cuartil
    """
    print('''Elija un cuartil:
          \t 1) Q1
          \t 2) Q2
          \t 3) Q3
    ''')
    k = int(input())
    if len(Datos)%2 != 0:
        if k == 1:
            print('Q1 =',Datos[int((k*(len(Datos)+1)/4)-1)])
        elif k == 2:
            mediana = Mediana(Datos)
            print('Q2 =', mediana)
        elif k == 3:
            print('Q3 =',Datos[int((k*(len(Datos)+1)/4)-1)])
        else:
            print('ERROR')
    else:
        if k == 1:
            print('Q1 =',round((Datos[(int(k*(len(Datos)+1)/4))-1]+Datos[(int(k*(len(Datos)+1)/4))]/2),2))
        elif k == 2:
            mediana = Mediana(Datos)
            print('Q2 =', mediana)
        elif k == 3:
            print('Q3 =',round((Datos[(int(k*(len(Datos)+1)/4))-1]+Datos[(int(k*(len(Datos)+1)/4))]/2),2))
        else:
            print('ERROR')
    volver_al_menu()
   
def main():
    """
    Funcion para desplegar el menu de opciones de la calculadora
    :param opcion: numero de la opcion que eligió el usuario
    """
    print('''ELIJA UNA OPCIÓN:
            \t 1)MATEMÁTICAS
            \t 2)ESTADÍSTICA
            \t 3)FÍSICA
            \t 4)QUÍMICA
            ''')
    opcion = int(input())
    if opcion == 1:
        matematicas()
    elif opcion == 2:
        estadistica()
    elif opcion == 3:
        fisica()
    elif opcion == 4:
        quimica()
    else:
        print('***OPCIÓN INVALIDA***')
        main()
       
main()