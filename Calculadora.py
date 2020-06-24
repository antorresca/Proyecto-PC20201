import os
import turtle
import time
Datos = []

def borrarPantalla():
   os.system ("clear")
   os.system ("cls")   

def Matematicas():
    mate = {1: OperacionesBasicas,2: OperacionesVariables}
    respuesta = True
    while respuesta:
        borrarPantalla()
        print(''' BIENVENIDO A LA SECCION MATEMATICAS!
        ELIJA UNA FUNCIÓN: 
        \t 1)Operaciones basicas
        \t 2)Operaciones con variables
        ''')
        try :
            mate[int(input())]()
            respuesta = VolverAntes()
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(2)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(2) 
    return

def OperacionesBasicas():
    basica = {1: Sumar,2: Restar,3: Multiplicar,4: Radicar,5: Potenciar,6: Otro}
    bas = True
    while bas:
        borrarPantalla()
        print(''''Elija una operacion, SOLO DIGITE EL NUMERO DE LA OPCION:
        \t 1)Suma
        \t 2)Resta
        \t 3)Multiplicacion
        \t 4)Radicacion
        \t 5)Potenciacion
        \t 6)Operacion combinada
        ''')
        try:
            basica[int(input())]()
            bas = False
        except:
            print('Ha ingresado una opcion invalida,intente de nuevo')
            time.sleep(2)
    return

def Sumar():
    borrarPantalla()
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
    time.sleep(5)
    return

def Restar():
    borrarPantalla()
    print("ingrese los numeros que se van a restar separados por un espacio: ")
    numeros = list(map(float, (input().split())))
    resta = 0
    for i in range(len(numeros)):
        if i == 0:
            resta = numeros[i]
        else:
            resta -= numeros[i]
    print('El resultado es:',resta)
    time.sleep(5)
    return

def Multiplicar():
    borrarPantalla()
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
    time.sleep(5)
    return

def Dividir():
    borrarPantalla()
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
    if division == 1:
        print('')
    else:
        print('su respuesta en decimal es: ',division,'y en entero es:',int(division))
    time.sleep(5)
    return

def Potenciar():
    borrarPantalla()
    print('Ingrese la base:')
    base = float(input())
    print('ingrese exponente')
    exp = float(input())
    resultado= base**exp
    print(str(base)+'^'+str(exp)+'='+str(resultado))
    time.sleep(5)
    return

def Radicar():
    borrarPantalla()
    print('Ingrese el radicando: ')
    nume = float(input())
    print('Ingrese el indice: ')
    ind = float(input())
    raiz = nume**(1/ind)
    print(str(ind)+'√'+str(nume)+'='+str(raiz))
    time.sleep(5)
    return

def Otro():
    borrarPantalla()
    print('Ingrese su operacion:')
    operacion = separar(input())
    print(operacion)
    time.sleep(5)
    return

def OperacionesVariables():
    Avanzado = {1: Ecuaciones,2: Derivar,3: Integrar}
    Av = True
    while Av:
        borrarPantalla()
        print('''Ingrese la opcion que desee:
        \t 1)Ecuaciones
        \t 2)Derivacion
        \t 3)Integracion Indefinida
        ''')
        try:
            opcion = int(input())
            if opcion in Avanzado.keys():
                borrarPantalla()
                print('''Ingrese la funcion
                        (Con formato Pv^e donde P: coeficiente, v: variable , e: exponente)''')
                funcion = separar(input().replace('=','-'))
                letra = identificar(funcion)
                Avanzado[opcion](funcion,letra)
                Av = False
            else:
                print('Ha ingresado una opcion invalida,intente de nuevo')
                time.sleep(3)
        except:
            print('1Ha ingresado una opcion invalida,intente de nuevo')
            time.sleep(3)

def Ecuaciones(lista,variable):
    lista.sort(key = len)
    for n in lista:
        if '^2' in n:
            cuadratica(lista,variable)
            break
        else:
            normal(lista,variable)
            break
    return

def normal(ecuacion,variable):
    independiente = 0
    for elemento in ecuacion:
        if variable in elemento:
            if elemento[0] == variable:
                algebra = 1
            else:
                algebra = int(elemento.split(variable)[0])
        else:
            independiente += float(elemento)
    print(variable+'='+str((-1*independiente)/algebra))
    return

def cuadratica(ecuacion,variable):
    """
    Funcion para resolver ecuaciones de segundo grado
    :param ecuacion: str de la expresion algebraica
    """
    borrarPantalla()
    c = 0
    for i in ecuacion:
        if variable in i:
            for j in range(len(i)):
                if '^2' in i:
                    if i[j] == '^':
                        a = float(i[:j-1])
                else:
                    if i[j] == variable:
                        b = float(i[:j])
        else:
            c += float(i)
    X1 = (-b+((b**2)-4*a*c)**0.5)/(2*a)
    X2 = (-b-((b**2)-4*a*c)**0.5)/(2*a)
    if  type(X1) == complex or type(X2) == complex:
        print('No tiene respuesta dentro de los reales, ¿Quiere ver los resultados de todos modos? si/no')
        respuesta = input().lower()
        if respuesta == 'si' or respuesta == 's' or respuesta == 'i':
            print('X[1]=',X1,'\nX[2]=',X2) 
    else:
        print(variable+'[1]=',X1,'\n'+variable+'[2]=',X2)

def Integrar(funcion_a_integrar,variable):
    print('La integral es:')
    contador = 0
    for i in range(len(funcion_a_integrar)):
        if variable in funcion_a_integrar[i]:
            if '^' in funcion_a_integrar[i]:
                for t in range(len(funcion_a_integrar[i])):
                    if funcion_a_integrar[i][t] == '^':
                        exponente = float(funcion_a_integrar[i][t+1:])+1
                        break
            else:
                exponente = 2
            for y in range(len(funcion_a_integrar[i])):
                if funcion_a_integrar[i][y] == variable:
                    coeficiente = float(funcion_a_integrar[i][:y])
                    break
            resultado = coeficiente/exponente
            if contador != 0:
                if resultado>0:
                    resultado = '+'+str(resultado) 
            if resultado == 1:
                print(str(variable)+'^'+str(exponente),end='')
            else:
                print(str(resultado)+str(variable)+'^'+str(exponente),end='')
        else:
            print(str(funcion_a_integrar[i])+'x',end='')
    print('+C')

def Derivar(funcion_a_derivar,variable):
    print('La derivada es:')
    contador = 0
    for i in range(len(funcion_a_derivar)):
        if variable in funcion_a_derivar[i]:
            if '^' in funcion_a_derivar[i]:
                for t in range(len(funcion_a_derivar[i])):
                    if funcion_a_derivar[i][t] == '^':
                        exponente = float(funcion_a_derivar[i][t+1:])-1
                        break
            else:
                exponente = 0
            for y in range(len(funcion_a_derivar[i])):
                if funcion_a_derivar[i][y] == variable:
                    coeficiente = float(funcion_a_derivar[i][:y])
                    break
            resultado = coeficiente*(exponente+1)
            if contador != 0:
                if resultado>0:
                    resultado = '+'+str(resultado) 
            if resultado == 1:
                if exponente == 1:
                    print(str(variable),end='')
                elif exponente == 0:
                    print(str(resultado),end='')
                else:
                   print(str(variable)+'^'+str(exponente),end='')
            else:
                if exponente == 1:
                    print(str(resultado)+str(variable),end='')
                elif exponente == 0:
                    print(str(resultado),end='')
                else:
                    print(str(resultado)+str(variable)+'^'+str(exponente),end='')
            contador += 1

def separar(a):
    lista = []
    op = ['+','-','*','/']
    cont = 0
    a += '+'
    for t in range(len(a)):
        if cont < t:
            if a[t] in op:
                try:
                    if a[t+1] in op:
                        lista.append(a[cont:t+3])
                        cont = t+3
                    else:
                        lista.append(a[cont:t])
                        cont = t
                except:
                    lista.append(a[cont:t])
                    cont = t
    return lista

def identificar(lista_ecuacion):
    alfabeto = 'abcefghijklmnopqrstuvwxyz'
    for i in range(len(lista_ecuacion)):
        for v in alfabeto:
            if v in lista_ecuacion[i]:
                variable_encontrada = v
                break
        break
    return variable_encontrada

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
    print('''ELIJA UNA OPCIÓN:
            \t 1)Crear Datos
            \t 2)Agregar Datos
            \t 3)Operaciones estadisticas
            \t 4)Volver al menu principal
            ''')
    OpcionesDatos = int(input())
    if OpcionesDatos == 1:
        CrearDatos()
    elif OpcionesDatos == 2:
        AgregarDatos()
    elif OpcionesDatos == 3:
        if len(Datos) == 0:
            print(Datos)
            print('No hay datos a procesar, ingrése los datos')
            estadistica()
        else:
            FuncionesEst()

def CrearDatos():
    if len(Datos) == 0:
        AgregarDatos()
    else:
        for i in range(len(Datos)):
            Datos.remove(Datos[0])
        AgregarDatos()

def AgregarDatos():
    print('Ingrese cantidad de valores: ')
    n = int(input())
    for i in range(n):
        xi = float(input())
        Datos.append(xi)
    Datos.sort()
    estadistica()

def FuncionesEst():
    """
    Menú de funciones propias de la estadística

    """
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
        estadistica()
    elif Funcion == 2:
        mediana = Mediana(Datos)
        print('Mediana =',mediana)
        estadistica()
    elif Funcion == 3:
        print('''Elija una opción:
        \t 1) Poblacional
        \t 2) Muestral
        ''')
        PM = int(input())
        varianza = Varianza(Datos, PM)
        print('Varianza =',varianza)
        estadistica()
    elif Funcion == 4:
        print('''Elija una opción:
        \t 1) Poblacional
        \t 2) Muestral
        ''')
        PM = int(input())
        s = DesviacionEstandar(Datos, PM)
        print('Desviacion =',s)
        estadistica()
    elif Funcion == 5:
        print('''Elija una opción:
        \t 1) Poblacional
        \t 2) Muestral
        ''')
        PM = int(input())
        CV = CoeficienteDeVariacion(Datos, PM)
        print('C.V. ='+str(CV)+'%')
        estadistica()
    elif Funcion == 6:
        Percentiles(Datos)
        estadistica()
    elif Funcion == 7:
        Cuartiles(Datos)
        estadistica()

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
  
    print ("""
    Por favor, definir la incognita:
    Un string que sea la variable fisica a encontar o el fenomeno fisco a comprender.
    """)
    Incognita = str(input()) 
    Incognita = Incognita.upper()  
    #if Incognita == "DISTANCIA":
        #distancia()
    #elif Incognita == "VELOCIDAD":
        #velocidad()
    if Incognita == "ACELERACION":
        aceleracion()
    else:
        print("Variable o proceso no encontrado")
    
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

def VolverAntes():
    print('¿Desea regresar al menú de la funcion? Si/No')
    respuesta = input()
    if respuesta.lower() == 'si':
        return True
    else:
        return False
    
def VolverInicio():
    print('¿Desea regresar al menú principal? Si/No')
    respuesta = input()
    if respuesta.lower() == 'si':
        return True
    else:
        return False

def main():
    funciones = {1:Matematicas}
    bandera = True
    while bandera:
        borrarPantalla()
        print('''ELIJA UNA OPCIÓN:
        \t 1)MATEMÁTICAS
        \t 2)ESTADÍSTICA
        \t 3)FÍSICA
        \t 4)QUÍMICA
        ''')
        try:
            funciones[int(input())]()
            bandera = VolverInicio()
        except:
            print('***OPCIÓN INVALIDA***')     
    print('Vuelva Pronto')
    time.sleep(2)    
        
main()