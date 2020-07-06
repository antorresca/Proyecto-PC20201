import os
import turtle
import time
try:
    import usuarios
except:
    g = open('usuarios.py', 'w')
    g.write('usuarios = {}')
    g.close()

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
    historial['Matematicas'].append('Suma \n\t'+'+'.join(str(x) for x in numeros)+' = '+str(suma))
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
    historial['Matematicas'].append('Resta \n\t'+'-'.join(str(x) for x in numeros)+' = '+str(resta))
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
    historial['Matematicas'].append('Multiplicacion \n\t'+'x'.join(str(x) for x in numeros)+' = '+str(mult))
    return

def Dividir():
    borrarPantalla()
    print('Ingrese los numeros que desea dividir separados por un \'/\'')
    d = list(map(int,input().split('/')))
    division =1
    try:
        for num in range(len(d)):
            if num == 0:
                division = d[num]
            else:
                division /= num
        print('su respuesta es: ',division,)
        historial['Matematicas'].append('Division \n\t'+'/'.join(str(x) for x in numeros)+'='+str(division))
    except ZeroDivisionError:
        print('No es posible dividir entre cero (0)')
        historial['Matematicas'].append('Division \n\tNo es posible division entre cero '+'/'.join(str(x) for x in numeros))
    return

def Potenciar():
    borrarPantalla()
    print('Ingrese la base:')
    base = float(input())
    print('ingrese exponente')
    exp = float(input())
    resultado= base**exp
    print(str(base)+'^'+str(exp)+'='+str(resultado))
    historial['Matematicas'].append('Potenciacion \n\t'+str(base)+'^'+str(exp)+'='+str(resultado))
    return

def Radicar():
    borrarPantalla()
    print('Ingrese el radicando: ')
    nume = float(input())
    print('Ingrese el indice: ')
    ind = float(input())
    raiz = nume**(1/ind)
    print(str(ind)+'√'+str(nume)+'='+str(raiz))
    return

def Otro():
    borrarPantalla()
    print('Ingrese su operacion:')
    separado = separar(input())
    print(separado)
    op = ['^','x','/','+','-']
    operaciones = []
    for elemento in range(len(separado)):
        for t in range(len(separado[elemento])):
            if separado[elemento][t] in op:
                operaciones.append(separado[elemento][t])
                operaciones.append(separado[elemento][t+1])
                break
            else:
                operaciones.append(separado[elemento][t])
    for t in op:
        if t in operaciones:
            g = operaciones.index(t)
            if t == '^':
                resultado = int(operaciones[g-1])**int(operaciones[g+1])
            elif t == 'x':
                resultado = int(operaciones[g-1])*int(operaciones[g+1])          
            elif t == '/':
                resultado =  int(operaciones[g-1])/int(operaciones[g+1])
            elif t == '+':
                resultado =  int(operaciones[g-1])+int(operaciones[g+1])
            elif t == '-':
                resultado = int(operaciones[g-1])-int(operaciones[g+1])
            del operaciones[g]
            operaciones[g-1] = resultado
            del operaciones[g]
    print(operaciones[0])
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
    op = ['^','x','+','-','*','/']
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

def Fisica():
    fis = {1: cinematica,2: dinamica} #falta electromagnetismo y ondas
    rta = True
    while rta:
        borrarPantalla()
        print (""" BIENVENIDO A LA SECCION FISICA
        Por favor, digite el numero de la rama:
        \t 1) Cinematica
        \t 2) Dinamica
        \t 3) Electromagnetismo
        \t 4) Ondas
        """)
        try:
            fis[int(input())]()
            rta = VolverAntes()
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(2)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(2)
    return

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

def Estadistica():
    est = {1: CrearDatos,2: AgregarDatos, 3: FuncionesEst}
    Rta = True
    while Rta:
        borrarPantalla()
        print('''ELIJA UNA OPCIÓN:
            \t 1)Crear Datos
            \t 2)Agregar Datos
            \t 3)Operaciones estadisticas
            ''')
        try:
            entrada = int(input())
            if entrada == 1:
                Datos = est[entrada]()
            else:
                try:
                    est[entrada](Datos)
                except NameError:
                    print('No se han ingresado Datos, por favor eliga la opcion 1 para continuar')
            Rta = VolverAntes()
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(2)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(2)
    return

def CrearDatos():
    print('Ingrese cantidad de valores: ')
    n = int(input())
    Datos_entrada = []
    for i in range(n):
        print('Ingrese valor:',i+1)
        xi = float(input())
        Datos_entrada.append(xi)
    Datos_entrada.sort()
    return Datos_entrada

def AgregarDatos(ListaDeDatos):
    """
    :param ListaDeDatos: Lista de datos anteriormente ingresados
    La función agrega nuevos elementos a la lista de datos con la que se está trabajando
    """
    print('Ingrese cantidad de valores: ')
    n = int(input())
    for i in range(n):
        print('Ingrese valor:',i+1)
        xi = float(input())
        ListaDeDatos.append(xi)
    ListaDeDatos.sort()
    return ListaDeDatos

def FuncionesEst(Datos):
    """
    Menú de funciones propias de la estadística
    """
    FEst = {1: MediaAritmetica,2: Mediana,6: Percentiles, 7:Cuartiles} 
    Fe = True
    while Fe:
        borrarPantalla()
        print('''ELIJA UNA FUNCIÓN: 
        \t 1)Media
        \t 2)Mediana
        \t 3)Varianza
        \t 4)Desviación estandar
        \t 5)Coeficiente de variación
        \t 6)Percentiles
        \t 7)Cuartiles
        ''')
        try:
            funcion = int(input())
            if funcion >=3 and funcion <=5:
                salida = PoblacionMuestra(Datos,funcion)
            else:
                salida = FEst[funcion](Datos)
            print(salida[0],salida[1])
            Fe = VolverAntes()
        except:
            print('Opcion invalida')
    return

def PoblacionMuestra(Datos,opcion):
    PM = {3: Varianza,4: DesviacionEstandar,5: CoeficienteDeVariacion}
    while True:
        print('''Elija una opción:
        \t 1) Poblacional
        \t 2) Muestral
        ''')
        try:
            Pob = int(input())
            return PM[opcion](Datos,Pob)
        except:
            print('Opcion invalida vuelva a intentar')
            time.sleep(5)    

def MediaAritmetica(Datos):
    """
    Funcion que permite calcular la media de una lista de datos
    La lista suma cada uno de los datos y los divide entre el número de datos
    """
    sumaprom = 0
    for i in range(len(Datos)):
        sumaprom += Datos[i]
    promedio = round((sumaprom/len(Datos)),2) 
    return 'El promedio es:',promedio
    
def Mediana(Datos):
    """
    En caso de que el número de datos sea impar, retorna el dato en la posición central
    En caso de ser par, retorna el promedio entre los dos datos centrales
    """
    if len(Datos) % 2 == 0:
        mediana = round(((Datos[(len(Datos)-1)//2]+Datos[len(Datos)//2])//2),2)
    else:
        mediana = Datos[int(len(Datos)/2)]
    return 'La mediana es:',mediana

def Varianza(Datos, PM):
    """
    Dependiendo del valor del parámetro PM calcula la varianza poblacional o muestral
    Llama a la cunción MediaAritmetica()
    Suma los cuadrados del resultado de restar el dato en la posición i con la mediana
    En caso de ser poblacional el valor se divide por n y si es muestral se divide por n-1
    Y retorna el valor varianza con 2 decimales
    """
    promedio = MediaAritmetica(Datos)[1]
    if PM == 1:
        sumvarianza = 0
        for i in range(len(Datos)):
            sumvarianza += ((Datos[i]-promedio)**2)
        varianza = round((sumvarianza/len(Datos)),2)
    elif PM == 2:
        sumvarianza = 0
        for i in range(len(Datos)):
            sumvarianza += ((Datos[i]-promedio)**2)
        varianza = round((sumvarianza/(len(Datos)-1)),2)
    return 'La varianza es:',varianza

def DesviacionEstandar(Datos, PM):
    """
    Llama a la funcion Varianza() y calcula la raíz cuadrada del valor varianza
    Retorna el valor s (Desviacion Estandar) con 2 decimales
    """
    varianza = Varianza(Datos,PM)[1]
    s = round((varianza**0.5),2)
    return 'La desviacion estandar es:',s

def CoeficienteDeVariacion(Datos, PM):
  """
  Llama a la funcion DesviacionEstandar()
  Divide el valor s entre el valor promedio, este se multiplica por 100 para obtenes el valor de porcentaje
  Retorna el valor CV con dos decimales

  """
  s = DesviacionEstandar(Datos, PM)[1]
  promedio = MediaAritmetica(Datos)[1]
  CV = round(((s/promedio)*100),2)
  return 'El coeficiente de variacion es: ',CV

def Percentiles(Datos):
    """
    :param Datos: Número que corresponde al percentil que se desea buscar, este número debe estar entre 1 y 99
    En caso de que el número de datos sea impar, imprime el dato en la posición correspondiente del percentil
    En caso de ser par, imprime el promedio entre los dos datos cercanos a las posición correspondiente al percentil
    """
    print('Ingrese el percentil:')
    k = int(input())
    if (k > 0) and (k <= 100):
        if len(Datos)%2 != 0:
            percentil = 'P'+str(k)+' =',Datos[int((k*(len(Datos)+1)/100)-1)]
        else:
            percentil = 'P'+str(k)+' =',round(((Datos[(int(k*(len(Datos)+1)/100))-1]+Datos[(int(k*(len(Datos)+1)/100))])/2),2)
    else:
        percentil = 'ERROR',''
    return percentil

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
            respuesta = 'Q1 =',Datos[int((k*(len(Datos)+1)/4)-1)]
        elif k == 2:
            mediana = Mediana(Datos)[1]
            respuesta = 'Q2 =', mediana
        elif k == 3:
            respuesta = 'Q3 =',Datos[int((k*(len(Datos)+1)/4)-1)]
        else:
            respuesta = 'ERROR',''
    else:
        if k == 1:
            respuesta = 'Q1 =',round(((Datos[(int(k*(len(Datos)+1)/4))-1]+Datos[(int(k*(len(Datos)+1)/4))])/2),2)
        elif k == 2:
            mediana = Mediana(Datos)[1]
            respuesta = 'Q2 =', mediana
        elif k == 3:
            respuesta = 'Q3 =',round(((Datos[(int(k*(len(Datos)+1)/4))-1]+Datos[(int(k*(len(Datos)+1)/4))])/2),2)
        else:
            respuesta = 'ERROR',''
    return respuesta

def Peso(Mensaje, Semilla):
    Peso_Palabra = []
    for i in range(len(Mensaje)):
        iPeso = 0
        for x in range(len(Mensaje[i])):
            iPeso += (ord(Mensaje[i][x])*(x+1))%Semilla
        Peso_Palabra.append(iPeso)
    return Peso_Palabra
    
def CheckSum(PesosLista, Semilla, Limite):
    Checksum_List = [0]
    for i in range(len(PesosLista)):
        Check = (Checksum_List[i]+PesosLista[i])*Semilla
        if Check > Limite:
            Check = Check%Limite
        Checksum_List.append(Check)
    return Checksum_List
    
def contra(usuario):
    Mensaje = usuario
    Mensaje = Mensaje.split(' ')
    Semilla = 213
    Limite = 1000000
    PesosLista = Peso(Mensaje, Semilla)
    CheckSumLista = CheckSum(PesosLista, Semilla, Limite)
    resultado = CheckSumLista[len(CheckSumLista)-1]
    return resultado
    
def login():
    global user
    try:
        us = usuarios.usuarios
    except:
        us = {}
    res = True
    errores = 0
    while res:
        borrarPantalla()
        print('ingrese su usuario')
        user = input()
        if user in us.keys():
            print('ingrese su clave')
            con = input()
            if us[user] == con:
                g = chr(9608)
                for t in range(101):
                    print('Cargando . . .',t,'% ',(t//2)*g,end='\r')
                    if t <= 50:
                        time.sleep(0.1)
                    elif t == 80:
                        time.sleep(0.2)
                    elif t == 90:
                        time.sleep(0.2)
                    else:
                        time.sleep(0.05)
                res = False
            else:
                errores += 1
                print('contrasena incorrecta')
                if errores < 3:
                    print('Le quedan',3- errores,'intentos')
                elif errores == 3:
                    del us[user]
                    print('Su usuario se ha eliminado de la base de datos')
        else:
            print('su usuario es: '+user)
            cont = str(contra(user))
            print('su contrasena sera: ',cont)
            print('¿Desea cambiar su contrasena? Si/No')
            cambio = input()
            if cambio.lower() == 'si':
                print('Ingrese su nueva contrasena')
                cont = input()
            while True:
                print('Confirme la contrasena por favor')
                conf = input()
                if cont == conf:
                    us[user] = cont
                    print('Usuario y contrasena registrado correctamente')
                    break
                else:
                    print('Las contrasenas no coinciden')
                    time.sleep(1.5)
    with open('usuarios.py','w') as usernames:
        usernames.write('usuarios ='+str(us)+'\n')
    return True
    
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

def GuardarHistorial(inicio,fin):
    try:
        os.mkdir('Archivos usuarios')
    except FileExistsError:
        print('')
    try:
        os.mkdir('Archivos usuarios/'+user)
    except FileExistsError:
        print('')
    with open('Archivos usuarios/'+user+'/Historial','+a') as HUser:
        HUser.write('Entrada: '+inicio+'\n')
        for linea in historial:
            HUser.write(linea+'\n')
            for contenido in historial[linea]:
                HUser.write(contenido+'\n')
        HUser.write('Salida: '+fin+'\n')
    return

def VolverAntes():
    time.sleep(2)
    print('¿Desea regresar al menú de la funcion? Si/No')
    respuesta = input()
    if respuesta.lower() == 'si':
        return True
    else:
        return False
    
def VolverInicio():
    time.sleep(1)
    print('¿Desea regresar al menú principal? Si/No')
    respuesta = input()
    if respuesta.lower() == 'si':
        return True
    else:
        return False

def main():
    global historial
    historial = {'Matematicas':[],'Estadistica':[],'Fisica':[]}
    logo_principal()
    funciones = {1:Matematicas,2:Estadistica,3:Fisica}
    bandera = login()
    entrada = time.strftime("%d-%m-%Y %H:%M", time.localtime())
    while bandera:
        borrarPantalla()
        print('''ELIJA UNA OPCIÓN:
        \t 1)MATEMÁTICAS
        \t 2)ESTADÍSTICA
        \t 3)FÍSICA
        ''')
        try:
            funciones[int(input())]()
            bandera = VolverInicio()
        except:
            print('***OPCIÓN INVALIDA***')     
    salida = time.strftime("%d-%m-%Y %H:%M", time.localtime())
    print('Desea guardar su historial?')
    respuestahisto = input().lower()
    if respuestahisto == 'si':
        GuardarHistorial(entrada,salida)
    print('Vuelva Pronto')
    time.sleep(2)    

main()