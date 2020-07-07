import os
import turtle
import time
from matplotlib import pyplot as plt
try:
    import usuarios
except:
    g = open('usuarios.py', 'w')
    g.write('usuarios = {}')
    g.close()

def borrarPantalla():
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
    basica = {1: Sumar,2: Restar,3: Multiplicar,4: Dividir,5: Radicar,6: Potenciar,7: Otro}
    basic = {1: 'Suma',2: 'Resta',3: 'Multiplicacion',4: 'Division',5: 'Radicacion',6: 'Potencicion',7: 'Combinada'}
    bas = True
    while bas:
        borrarPantalla()
        print(''''Elija una operacion, SOLO DIGITE EL NUMERO DE LA OPCION:
        \t 1)Suma
        \t 2)Resta
        \t 3)Multiplicacion
        \t 4)Division
        \t 5)Radicacion
        \t 6)Potenciacion
        \t 7)Operacion combinada
        ''')
        try:
            opcion = int(input())
            salida = basica[opcion]()
            print(salida)
            historial['Matematicas'].append(str(basic[opcion])+'\n\t'+salida)
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
    resultado_suma = '+'.join(str(x) for x in numeros)+' = '+str(suma)
    return resultado_suma

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
    resultado_resta = '-'.join(str(x) for x in numeros)+' = '+str(resta)
    return resultado_resta

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
    resultado_multiplicacion = 'x'.join(str(x) for x in numeros)+' = '+str(mult)
    return resultado_multiplicacion

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
                division /= d[num]
        resultado_division = '/'.join(str(x) for x in d)+'='+str(division)
    except ZeroDivisionError:
        resultado_division = 'No es posible dividir entre cero (0)'
    return resultado_division

def Potenciar():
    borrarPantalla()
    print('Ingrese la base:')
    base = float(input())
    print('ingrese exponente')
    exp = float(input())
    resultado= base**exp
    resultado_potenciacion = str(base)+'^'+str(exp)+'='+str(resultado)
    return resultado_potenciacion

def Radicar():
    borrarPantalla()
    print('Ingrese el radicando: ')
    nume = float(input())
    print('Ingrese el indice: ')
    ind = float(input())
    raiz = nume**(1/ind)
    resultado_raiz = 'raiz'+str(ind)+'de'+str(nume)+'='+str(raiz)
    return resultado_raiz

def Otro():
    borrarPantalla()
    print('Ingrese su operacion:')
    operacion_comb = input()
    separado = Separar(operacion_comb.replace('x','*'))
    op = ['^','x','*','/','+','-']
    operaciones = []
    for elemento in range(len(separado)):
        for t in range(len(separado[elemento])):
            if separado[elemento][t] in op:
                if separado[elemento][t] == '-':
                    operaciones.append('+')
                else:
                    operaciones.append(separado[elemento][t])
                fin = 1
                while True:
                    try:
                        if separado[elemento][t+fin] not in op:
                            fin += 1
                    except:
                        if separado[elemento][t] == '-':
                            operaciones.append('-'+separado[elemento][t+1:t+fin+1])
                        else:
                            operaciones.append(separado[elemento][t+1:t+fin+1])
                        break
                break
            else:
                fin = 1
                while True:
                    try:
                        if separado[elemento][t+fin] not in op:
                            fin += 1
                    except:
                        if separado[elemento][t] == '-':
                            operaciones.append('-'+separado[elemento][t:t+fin+1])
                        else:
                            operaciones.append(separado[elemento][t:t+fin+1])
                        break
                break
    for rep in range(len(operaciones)):
        for t in op:
            if t in operaciones:
                g = operaciones.index(t)
                if t == '^':
                    resultado = int(operaciones[g-1])**int(operaciones[g+1])
                elif t == 'x' or t == '*':
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
    resultado_otros = operacion_comb+'='+str(operaciones[0])
    return resultado_otros

def OperacionesVariables():
    Avanzado = {1: Ecuaciones,2: Derivar,3: Integrar}
    Ava = {1: 'Ecuacion',2: 'Derivada',3: 'Integral'}
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
                entrada = input()
                if opcion == 1:
                    if Determinar(entrada):
                        funcion = Separar(entrada.replace('=','-'))
                    else:
                        funcion = Separar(entrada)
                else:
                    funcion = Separar(entrada.replace('=','-'))
                letra = Identificar(funcion)
                salida = Avanzado[opcion](funcion,letra)
                print(salida)
                historial['Matematicas'].append(Ava[opcion]+'\n\t'+entrada+salida)
                Av = False
            else:
                print('Ha ingresado una opcion invalida,intente de nuevo')
                time.sleep(3)
        except:
            print('Ha ingresado una opcion invalida,intente de nuevo')
            time.sleep(3)
    return

def Ecuaciones(lista,variable):
    contador = 0
    for n in lista:
        if '^2' in n:
            contador = 1
            break
    if contador == 1:
        return Cuadratica(lista,variable)
    else:
        return Normal(lista,variable)

def Normal(ecuacion,variable):
    independiente = 0
    for elemento in ecuacion:
        if variable in elemento:
            if elemento[0] == variable:
                algebra = 1
            else:
                algebra = int(elemento.split(variable)[0])
        else:
            independiente += float(elemento)
    resultado_normal = variable+'='+str((-1*independiente)/algebra)
    return resultado_normal

def Cuadratica(ecuacion,variable):
    a = 0
    b = 0
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
            resultado_cuadratica = variable+'[1]='+str(X1)+'\n'+variable+'[2]='+str(X2) 
    else:
        resultado_cuadratica = variable+'[1]='+str(X1)+'\n'+variable+'[2]='+str(X2)
    return resultado_cuadratica

def Integrar(funcion_a_integrar,variable):
    contador = 0
    resultado_integracion = 'La integral es: '
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
                resultado_integracion += str(variable)+'^'+str(exponente)
            else:
                resultado_integracion += str(resultado)+str(variable)+'^'+str(exponente)
        else:
            resultado_integracion += str(funcion_a_integrar[i])+'x'
    resultado_integracion += '+C'
    return resultado_integracion

def Derivar(funcion_a_derivar,variable):
    contador = 0
    resultado_derivacion = 'La derivada es:'
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
                    resultado_derivacion += str(variable)
                elif exponente == 0:
                    resultado_derivacion += str(resultado)
                else:
                   resultado_derivacion += str(variable)+'^'+str(exponente)
            else:
                if exponente == 1:
                    resultado_derivacion += str(resultado)+str(variable)
                elif exponente == 0:
                    resultado_derivacion += str(resultado)
                else:
                    resultado_derivacion += str(resultado)+str(variable)+'^'+str(exponente)
            contador += 1
    return resultado_derivacion

def Determinar(f):
    if '^2' in f:
        return True
    else:
        return False

def Separar(a):
    lista = []
    op = ['^','+','-','*','/']
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
                        if a[t] == '^':
                            lista.append(a[cont:t+2])
                            cont = t+2
                        else:
                            lista.append(a[cont:t])
                            cont = t
                except:
                    lista.append(a[cont:t])
                    cont = t
    return lista

def Identificar(lista_ecuacion):
    alfabeto = 'abcefghijklmnopqrstuvwxyz'
    for i in range(len(lista_ecuacion)):
        for v in alfabeto:
            if v in lista_ecuacion[i]:
                variable_encontrada = v
                break
        break
    return variable_encontrada

def Fisica():
    """
    Parametros: N.A
    Definicion: En esta funcion se define un menu que envia a las distintas funciones que representan un
    submenu que representa cada rama de la fisica escrita en el programa 
    """ 
    fis = {1: Cinematica ,2: Dinamica_y_energia ,3:Electromagnetismo ,4:Ondas} 
    rta = True
    while rta:
        borrarPantalla()
        print (""" BIENVENIDO A LA SECCION FISICA
        Por favor, digite el numero de la rama:
        \t 1) Cinematica
        \t 2) Dinamica y energia
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
  
def Cinematica(): 
    """
    La funcion cinematica tiene como proposito direccionar a las funciones contenidas
    en esta, las cuales son las que realizan los calculos. Esta tiene un diccionario 
    con posibles constantes que pueden ser invocadas, 
    asi como funciones que se usan dentro de las funciones de calculo como 'sumatoria'.
    Esta tiene como entrada un string con el nombre de la variable a conocer.   
    """
    dicc_cinematica= {1:Distancia,2:Velocidad,3:Aceleracion,4:Constantes_cinematica}
    rta = True
    while rta:
        borrarPantalla()
        print (""" BIENVENIDO A LA SECCION CINEMATICA
        Por favor, digite el numero de la varaible o proceso:
        \t 1) Distancia
        \t 2) Velocidad
        \t 3) Aceleracion
        \t 4) Constantes o conversor de medidas
        """)
        try:
            dicc_cinematica[int(input())]()
            rta = VolverAntes()
        except FloatingPointError:
            print('Ingrese, por favor, las magnitudes numericas reales separadas per un punto (.)')
            time.sleep(5)
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(5)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(5)
        except ZeroDivisionError:
            print('Ingrese, por favor, una magnitud distinta a cero en el denominador')
            time.sleep(5)
        
def Distancia():
    """
    funcion de calculo que se apoya en la funcion "sumatoria" para calcular la 
    distancia segun la ecuacion distancia = velocidad x tiempo.
    """
    velocidad = Sumatoria('velocidad',True)
    if velocidad > 299792458 or -299792458 > velocidad:
        print("La velocidad no puede sobrepasar la costante de la velocidad de la luz, por favor ingrese datos reales")
    else:
        print ("Por favor, defina la magnitud en segundos del tiempo:")
        tiempo = float(input())
        distancia = round(velocidad * tiempo,3)
        print("La distancia es", distancia,"metros")
        historial['Fisica'].append('Distancia \n\t'+str(distancia)+'metros')
        
def Velocidad():
    """
    funcion de calculo que se apoya en la funcion "sumatoria" para calcular la 
    velocidad segun la ecuacion velocidad = distancia / tiempo.
    """
    desplazamiento=Sumatoria('desplazamiento',True)
    print ("Por favor, defina la magnitud en segundos del tiempo:")
    tiempo = float(input())
    velocidad = round(desplazamiento/tiempo,3)
    if velocidad > 299792458 or -299792458 > velocidad:
        print("La velocidad no puede sobrepasar la costante de la velocidad de la luz, por favor ingrese datos reales (Max Planck esta triste)")
    else:
        print("La velocidad es ", velocidad,"metros/segundo")
        historial['Fisica'].append('Velocidad \n\t'+str(velocidad)+'metros/segundos')

def Aceleracion():
    """
    funcion en la cual se piden dos valores, velocidad y tiempo para conocer una 
    aceleracion segun la ecuacion aceleracion = velocidad / tiempo
    """
    print ("Por favor, defina la magnitud en metros/segundo de la velocidad:")
    velocidad = float(input())
    if velocidad > 299792458 or -299792458 > velocidad:
        print("La velocidad no puede sobrepasar la costante de la velocidad de la luz, por favor ingrese datos reales")
    else:
        print ("Por favor, defina la magnitud en segundos del tiempo:")
        tiempo = float(input())
        aceleracion = round(velocidad/tiempo,3)
        print("La aceleracion es ", aceleracion,"metros/segundo^2")
        historial['Fisica'].append('Aceleracion \n\t'+str(aceleracion)+'metros/segundos^2')
    return(aceleracion)
  
def Constantes_cinematica():
    """
    Parametros: N.A
    Definicion: En esta funcion se  genera un submenu para direccionar a un 
    imprimible en pantalla con el valor de una constante o  a una relacion entre dos 
    unidades de medidas distintas, con la ayuda de la funcion regla_de_tres 
    """
    rta = True
    while rta:
        borrarPantalla()
        cte_cinematica = {5:[[1,0.447],["mi/h","m/s"]],1:"La velocidad de la luz es de 299792458 m/s en el vacio",2:"La velocidad del sonido es de 343 m/s en el aire",3:[[1,3.6],["m/s","Kmh"]],4:[[1,2.54],["in","cm"]]}
        print (""" BIENVENIDO A LA SECCION DE CONSTANTES DE CINEMATICA
        Por favor, digite el numero de la constante, relacion o proceso:
        \t 1) Velociadad de la luz
        \t 2) Velocidad del sonido
        \t 3) km/h : m/s
        \t 4) in : cm
        \t 5) mi/h : m/s
        """)
        try:
            entrada = int(input())
            if entrada > 2:
                Regla_de_tres(cte_cinematica[entrada])
            else:
                print(cte_cinematica[entrada])
            rta = VolverAntes()
        except FloatingPointError:
            print('Ingrese, por favor, las magnitudes numericas reales separadas per un punto (.)')
            time.sleep(2)
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(2)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(2)
        except ZeroDivisionError:
            print('Ingrese, por favor, una magnitud distinta a cero en el denominador')
            time.sleep(2)

def Dinamica_y_energia():
    """
    La funcion dinamica_y_energia tiene como proposito direccionar a las funciones contenidas
    en esta, las cuales son las que realizan los calculos. Esta tiene un diccionario 
    llamado "dicc_dinamica" con posibles constantes que pueden ser invocadas, 
    asi como funciones que se usan dentro de las funciones de calculo como 'sumatoria'.
    Esta tiene como entrada un string con el nombre de la variable a conocer.   
    """
    dicc_dinamica= {1:Fuerza,2:Masa,3:Presion,4:Trabajo,5:Potencia_mecanica,6:Constantes_dinamica}
    rta = True
    while rta:
        borrarPantalla()
        print (""" BIENVENIDO A LA SECCION CINEMATICA
        Por favor, digite el numero de la varaibla o proceso:
        \t 1) Fuerza
        \t 2) Masa
        \t 3) Presion
        \t 4) Trabajo 
        \t 5) Potencia
        \t 6) Constantes o conversor de medidas
        """)
        try:
            dicc_dinamica[int(input())]()
            rta = VolverAntes()
        except FloatingPointError:
            print('Ingrese, por favor, las magnitudes numericas reales separadas por un punto (.)')
            time.sleep(5)
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(5)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(5)
        except ZeroDivisionError:
            print('Ingrese, por favor, una magnitud distinta a cero en el denominador')
            time.sleep(5)

def Fuerza():
    """
    Parametros: N.A
    Definicion: En esta funcion se da un menu para dedicir si se usa la funcion aceleracion
    para encontrar la aceleracion o ingresarla directamete, con esto se procede a buscar la 
    fuerza. 
    """ 
    dicc_ingreso = {1:input ,2:Aceleracion} 
    rta = True
    while rta:
        borrarPantalla()
        print ("""
        Para el valor de aceleracion desea:
        1) Ingresarlo (en este caso debe ingresar le valor en m/s^2 despues de marcar a opcion)
        2) Calcularlo
        """)
        try:
            a = float(dicc_ingreso[int(input())]())
            print("Por favor, ingrese la magnitud de la masa en Kg")
            masa = float(input())
            print("El valor de la fuerza es de", str(a*masa), "N")
            historial['Fisica'].append('Fuerza \n\t'+str(a*masa)+'N')
            rta = VolverAntes()
        except FloatingPointError:
            print('Ingrese, por favor, las magnitudes numericas reales separadas por un punto (.)')
            time.sleep(5)
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(5)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(5)
        except ZeroDivisionError:
            print('Ingrese, por favor, una magnitud distinta a cero en el denominador')
            time.sleep(5)
        
def Masa():
    """
    Parametros: N.A
    Definicion: En esta funcion se da un menu para dedicir si se usa la funcion aceleracion
    para encontrar la aceleracion o ingresarla directamete, con esto se procede a buscar la 
    masa. 
    """ 
    dicc_ingreso = {1:input ,2:Aceleracion} 
    rta = True
    while rta:
        borrarPantalla()
        print ("""
        Para el valor de aceleracion desea:
        1) Ingresarlo (en este caso debe ingresar le valor en m/s^2 despues de marcar a opcion)
        2) Calcularlo 
        """)
        try:
            a = float(dicc_ingreso[int(input())]())
            print("Por favor, ingrese la magnitud de la fuerza")
            fuerza = float(input())
            print("El valor de la masa es de", str(fuerza/a), "Kg")
            historial['Fisica'].append('Masa \n\t'+str(fuerza/a)+'Kg')
            rta = VolverAntes()
        except FloatingPointError:
            print('Ingrese, por favor, las magnitudes numericas reales separadas por un punto (.)')
            time.sleep(5)
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(5)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(5)
        except ZeroDivisionError:
            print('Ingrese, por favor, una magnitud distinta a cero en el denominador')
            time.sleep(5)
        
def Presion():
    """
    Parametros: N.A
    Definicion: En esta funcion se encarga de encontrar la presio, puede hacerse ingresando datos de fuerza o calculandolos
    """ 
    dicc_ingreso = {1:input ,2:Fuerza} 
    rta = True
    while rta:
        borrarPantalla()
        print ("""
        Para el valor de fuerza desea:
        1) Ingresarlo (en este caso debe ingresar le valor en N despues de marcar la opcion)
        2) Calcularlo
        """)
        try:
            f = float(dicc_ingreso[int(input())]())
            print("Por favor, ingrese la magnitud del area en m^2")
            area = float(input())
            print("El valor de la presion es de", str(f/area), "Pa")
            historial['Fisica'].append('Presion \n\t'+str(f/area)+'Pa')
            rta = VolverAntes()
        except FloatingPointError:
            print('Ingrese, por favor, las magnitudes numericas reales separadas por un punto (.)')
            time.sleep(5)
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(5)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(5)
        except ZeroDivisionError:
            print('Ingrese, por favor, una magnitud distinta a cero en el denominador')
            time.sleep(5)

def Trabajo():
    """
    Parametros: N.A
    Definicion: En esta funcion se  encuentra el valor del trabajo, puede que con un ingreso de datos o con la funcion de fuerza
    """
    dicc_ingreso = {1:input ,2:Fuerza} 
    rta = True
    while rta:
        borrarPantalla()
        print ("""
        Para el valor de fuerza desea:
        1) Ingresarlo (en este caso debe ingresar le valor en N, despues de marcar a opcion)
        2) Calcularlo
        """)
        try:
            f = float(dicc_ingreso[int(input())]())
            print("Por favor, ingrese la magnitud de la distancia ")
            distancia = Sumatoria("distancia",True)
            print("El valor del trabajo es de", str(f*distancia), "J")
            historial['Fisica'].append('Trabajo \n\t'+str(f*distancia)+'J')
            rta = VolverAntes()
        except FloatingPointError:
            print('Ingrese, por favor, las magnitudes numericas reales separadas por un punto (.)')
            time.sleep(5)
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(5)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(5)
        except ZeroDivisionError:
            print('Ingrese, por favor, una magnitud distinta a cero en el denominador')
            time.sleep(5)

def Potencia_mecanica():
    """
    Parametros: N.A
    Definicion: En esta funcion se  
    """ 
    dicc_ingreso = {1:input ,2:Trabajo} 
    rta = True
    while rta:
        borrarPantalla()
        print ("""
        Para el valor de aceleracion desea:
        1) Ingresarlo (en este caso debe ingresar le valor en m/s^2 despues de marcar a opcion)
        2) Calcularlo
        """)
        try:
            t = float(dicc_ingreso[int(input())]())
            print("Por favor, ingrese la magnitud del tiempo en seg")
            tiempo = float(input())
            print("El valor de la potencia es de", str(t*tiempo), "J/s")
            historial['Fisica'].append('Potencia \n\t'+str(t*tiempo)+'J/s')
            rta = VolverAntes()
        except FloatingPointError:
            print('Ingrese, por favor, las magnitudes numericas reales separadas por un punto (.)')
            time.sleep(5)
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(5)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(5)
        except ZeroDivisionError:
            print('Ingrese, por favor, una magnitud distinta a cero en el denominador')
            time.sleep(5)

def Constantes_dinamica():
    """
    Parametros: N.A
    Definicion: En esta funcion se  genera un submenu para direccionar a un 
    imprimible en pantalla con el valor de una constante o  a una relacion entre dos 
    unidades de medidas distintas, con la ayuda de la funcion regla_de_tres 
    """     
    rta = True
    while rta:
        borrarPantalla()
        cte_cinematica = {1:"El peso en la tierra es de 9.871 m/s^2",2:"La constante de gravitacion universal de 6.67 X 10^-11 Nm^2/kg",3:[[1,101325],["Pa","atm"]],4:[[1,4184],["Kcal","J"]],5:[[1,14.7],["atm" , "lb/pulg^2" ]],6:[[1,4.448],["lb" , "N"  ]]}
        print (""" BIENVENIDO A LA SECCION DE CONSTANTES DE DINAMICA
        Por favor, digite el numero de la constante, relacion o proceso:
        \t 1) Peso en la tierra
        \t 2) Constante de gravitacion universal
        \t 3) Pa : atm
        \t 4) J : Kcal
        \t 5) atm : lb/pulg^2 
        \t 6) lb : N 
        """)
        try:
            entrada = int(input())
            if entrada > 2:
                Regla_de_tres(cte_cinematica[entrada])
            else:
                print(cte_cinematica[entrada])
            rta = VolverAntes()
        except FloatingPointError:
            print('Ingrese, por favor, las magnitudes numericas reales separadas per un punto (.)')
            time.sleep(2)
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(2)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(2)
        except ZeroDivisionError:
            print('Ingrese, por favor, una magnitud distinta a cero en el denominador')
            time.sleep(2)
  
def Electromagnetismo():
    """
    La funcion electromagnetismo tiene como proposito direccionar a las funciones contenidas
    en esta, las cuales son las que realizan los calculos. Esta tiene un diccionario
    llamado "dicc_electromagnetismo" con posibles constantes que pueden ser invocadas, 
    asi como funciones que se usan dentro de las funciones de calculo como 'sumatoria'.
    Esta tiene como entrada un string con el nombre de la variable a conocer.   
    """
    dicc_electromagnetismo= {1:Voltaje,2:Corriente,3:Resistencia,4:Potencia_electrica,5:Lectura_resistencias,6:Constantes_electromagnetismo} 
    rta = True
    while rta:
        borrarPantalla()
        print (""" BIENVENIDO A LA SECCION CINEMATICA
        Por favor, digite el numero de la varaibla o proceso:
        \t 1) Voltaje
        \t 2) Corriente
        \t 3) Resistencia
        \t 4) Potencia electrica
        \t 5) Calculadora de resistencias
        \t 6) Constantes o conversor de medidas
        """)
        try:
            dicc_electromagnetismo[int(input())]()
            rta = VolverAntes()
        except FloatingPointError:
            print('Ingrese, por favor, las magnitudes numericas reales separadas per un punto (.)')
            time.sleep(10)
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(10)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(10)
        except ZeroDivisionError:
            print('Ingrese, por favor, una magnitud distinta a cero en el denominador')
            time.sleep(10)

def Voltaje():
    """
    Parametros: N.A
    Definicion: En esta funcion se  encarga de hacer una relacion del voltaje
    """ 
    print("""
    Por favor, ingrese el numero de la variable que le falta:
    1) Corriente ( I )
    2) Resistencia ( R )
    3) Potencia ( P )
    """)
    entrada = int(input())
    if entrada == 1:
        print("Ingrese la magnitud de la potencia en vatios")
        potencia = float(input())
        print("Ingrese la magnitud de la resitencia en Ohms")
        resistencia = float(input())
        print("El voltaje es de :"+str(round((potencia*resistencia)^(1/2),3))+"Voltios")
        historial['Fisica'].append('Voltaje \n\t'+str(round((potencia*resistencia)^(1/2),3))+'Voltios')
    elif entrada == 2:
        print("Ingrese la magnitud de la potencia en vatios")
        potencia = float(input())
        print("Ingrese la magnitud de la corriente en Amperios")
        corriente = float(input())
        print("El voltaje es de :"+str(round((potencia/corriente),3))+"Voltios")
        historial['Fisica'].append('Voltaje \n\t'+str(round((potencia/corriente),3))+'Voltios')
    elif entrada == 3:
        print("Ingrese la magnitud de la corriente en Amperios")
        corriente = float(input())
        print("Ingrese la magnitud de la resitencia en Ohms")
        resistencia = float(input())
        print("El voltaje es de :"+str(round((potencia*resistencia),3))+"Voltios")
        historial['Fisica'].append('Voltaje \n\t'+str(round((potencia*resistencia),3))+'Voltios')

def Corriente():
    """
    Parametros: N.A
    Definicion: En esta funcion se  
    """ 
    print("""
    Por favor, ingrese el numero de la variable que le falta:
    1) Resistencia ( R )
    2) Voltaje ( V )
    3) Potencia ( P )
    """)
    entrada = int(input())
    if entrada == 1:
        print("Ingrese la magnitud de la tension(voltaje) en Voltios")
        voltaje = float(input())
        print("Ingrese la magnitud de la potencia en vatios")
        potencia = float(input())
        print("La corriente es de :"+str(round((potencia/voltaje),3))+"Amperios")
        historial['Fisica'].append('Corriente \n\t'+str(round((potencia/voltaje),3))+'Amperios')
    elif entrada == 2:
        print("Ingrese la magnitud de la potencia en vatios")
        potencia = float(input())
        print("Ingrese la magnitud de la resitencia en Ohms")
        resistencia = float(input())
        print("La corriente es de :"+str(round((potencia/resistencia)*(1/2),3))+"Amperios")
        historial['Fisica'].append('Corriente \n\t'+str(round((potencia/resistencia)*(1/2),3))+'Amperios')
    elif entrada == 3:
        print("Ingrese la magnitud de la resitencia en Ohms")
        resistencia = float(input())
        print("Ingrese la magnitud de la tension(voltaje) en Voltios")
        voltaje = float(input())
        print("La corriente es de :"+str(round(voltaje/resistencia,3))+"Amperios")
        historial['Fisica'].append('Corriente \n\t'+str(round(voltaje/resistencia,3))+'Amperios')

def Resistencia():
    """
    Parametros: N.A
    Definicion: En esta funcion se  
    """ 
    print("""
    Por favor, ingrese el numero de la variable que le falta:
    1) Corriente ( I )
    2) Voltaje ( V )
    3) Potencia ( P )
    """)
    entrada = int(input())
    if entrada == 1:
        print("Ingrese la magnitud de la tension(voltaje) en Voltios")
        voltaje = float(input())
        print("Ingrese la magnitud de la potencia en vatios")
        potencia = float(input())
        print("La resistencia es de :"+str(round((voltaje**2)/(potencia),3))+"Ohms")
        historial['Fisica'].append('Resistencia \n\t'+str(round((voltaje**2)/(potencia),3))+'Ohms')
    elif entrada == 2:
        print("Ingrese la magnitud de la potencia en vatios")
        potencia = float(input())
        print("Ingrese la magnitud de la corriente en Amperios")
        corriente = float(input())
        print("La resistencia es de :"+str(round((potencia)/(corriente**2),3))+"Ohms")
        historial['Fisica'].append('Resistencia \n\t'+str(round((potencia)/(corriente**2),3))+'Ohms')
    elif entrada == 3:
        print("Ingrese la magnitud de la corriente en Amperios")
        corriente = float(input())
        print("Ingrese la magnitud de la tension(voltaje) en Voltios")
        voltaje = float(input())
        print("La resistencia es de :"+str(round(voltaje/corriente,3))+"Ohms")
        historial['Fisica'].append('Resistencia \n\t'+str(round(voltaje/corriente,3))+'Ohms')

def Potencia_electrica():
    print("""
    Por favor, ingrese el numero de la variable que le falta:
    1) Corriente ( I )
    2) Voltaje ( V )
    3) Resistencia ( R )
    """)
    entrada = int(input())
    if entrada == 1:
        print("Ingrese la magnitud de la tension(voltaje) en Voltios")
        voltaje = float(input())
        print("Ingrese la magnitud de la resitencia en Ohms")
        resistencia = float(input())
        print("La potencia es de :"+str(round((voltaje**2)/(resistencia),3))+"Vatios")
        historial['Fisica'].append('Potencia \n\t'+str(round((voltaje**2)/(resistencia),3))+'Vatios')
    elif entrada == 2:
        print("Ingrese la magnitud de la resitencia en Ohms")
        resistencia = float(input())
        print("Ingrese la magnitud de la corriente en Amperios")
        corriente = float(input())
        print("La potencia es de :"+str(round((corriente**2)*resistencia),3)+"Vatios")
        historial['Fisica'].append('Potencia \n\t'+str(round((corriente**2)*resistencia),3)+'Vatios')
    elif entrada == 3:
        print("Ingrese la magnitud de la corriente en Amperios")
        corriente = float(input())
        print("Ingrese la magnitud de la tension(voltaje) en Voltios")
        voltaje = float(input())
        print("La potencia es de :"+str(round((corriente*voltaje),3))+"Vatios")
        historial['Fisica'].append('Potencia \n\t'+str(round((corriente*voltaje),3))+'Vatios')

def Lectura_resistencias():
    """
    Parametros: N.A
    Definicion: En esta funcion se usa la libreria turtle para imprimir le dibujo de 
    una resistencia con su valor calculado 
    """ 
    print("Por favor ingrese el numero de bandas de la resistencia: Opciones( 3 - 4 - 5 )")
    bandas = int(input())
    borrarPantalla()
    dicc_digitos = {"negro":[0,"black"],"cafe":[1,"brown"],"rojo":[2,"darkred"],"naranja":[3,"darkorange1"],"amarillo":[4,"yellow"],"verde":[5,"darkgreen"],"azul":[6,"blue1"],"violeta":[7,"darkorchid3"],"gris":[8,"darkgrey"],"blanco":[9,"azure"]}
    dicc_factor = {"negro":[1,"black"],"cafe":[10,"brown"],"rojo":[100,"darkred"],"naranja":[1000,"darkorange1"],"amarillo":[10000,"yellow"],"verde":[100000,"darkgreen"],"azul":[1000000,"blue1"],"violeta":[10000000,"darkorchid3"],"oro":[0.1,"darkgoldenrod"],"plata":[0.01,"azure3"]}
    dicc_tolerancia = {"negro":["+/- 1%","black"],"cafe":["+/- 2%","brown"],"verde":["+/- 0.5%","darkgreen"],"azul":["+/- 0.25%","blue1"],"violeta":["+/- 0.1%","darkorchid3"],"gris":["+/- 0.05%","darkgrey"],"oro":["+/- 5%","darkgoldenrod"],"plata":["+/- 10%","azure3"],"otro":["+/- 20%","beige"]}
    lista_bandas=[]
    print(
    """Ingrese los colores de las bandas de la resistencia de acuerdo con la siguiente lista:
    Digito:         Factor:         Tolerancia:       
    Negro           Negro           Negro
    Cafe            Cafe            Cafe
    Rojo            Rojo            -
    Naranja         Naranja         -
    Amarillo        Amarillo        -
    Verde           Verde           Verde
    Azul            Azul            Azul
    Violeta         Violeta         Violeta
    Gris            -               Gris
    Blanco          -               -
    -               Oro             Oro
    -               Plata           Plata
    """)
    if bandas == 3:
        valor = 0
        factor_digital = 1
        for banda_leida in range(bandas-1):
            print("Banda (Digito) ",str(banda_leida+1)+") :")
            banda_leida = str(input())
            banda_leida = banda_leida.lower()
            valor += dicc_digitos[banda_leida][0]*factor_digital
            factor_digital *= 10
            lista_bandas += [dicc_digitos[banda_leida][1]]
        print("Banda (Factor) ",str(bandas)+") :")
        banda_leida = str(input())
        banda_leida = banda_leida.lower()
        valor = str(valor*dicc_factor[banda_leida][0]) , dicc_tolerancia["otro"][0]
        lista_bandas += [dicc_factor[banda_leida][1]]+[dicc_tolerancia["otro"][1]]
        lista_final = [lista_bandas], [valor]

    elif bandas == 4:
        valor = 0
        factor_digital = 1
        for banda_leida in range(bandas-2):
            print("Banda (Digito) ",str(banda_leida+1)+") :")
            banda_leida = str(input())
            banda_leida = banda_leida.lower()
            valor += dicc_digitos[banda_leida][0]*factor_digital
            factor_digital *= 10
            lista_bandas += [dicc_digitos[banda_leida][1]]
        print("Banda (Factor) ",str(bandas-1)+") :")
        banda_leida = str(input())
        banda_leida = banda_leida.lower()
        lista_bandas += [dicc_factor[banda_leida][1]]
        valor = str(valor*dicc_factor[banda_leida][0])
        print("Banda (Tolerancia) ",str(bandas)+") :")
        banda_leida = str(input())
        banda_leida = banda_leida.lower()
        valor += dicc_tolerancia[banda_leida][0]
        lista_bandas += [dicc_tolerancia[banda_leida][1]]
        lista_final = [lista_bandas] +[valor]

    elif bandas == 5:
        valor = 0
        factor_digital = 1
        for banda_leida in range(bandas-2):
            print("Banda (Digito) ",str(banda_leida+1)+") :")
            banda_leida = str(input())
            banda_leida = banda_leida.lower()
            valor += dicc_digitos[banda_leida][0]*factor_digital
            factor_digital *= 10
            lista_bandas += [dicc_digitos[banda_leida][1]]
        print("Banda (Factor) ",str(bandas-1)+") :")
        banda_leida = str(input())
        banda_leida = banda_leida.lower()
        lista_bandas += [dicc_factor[banda_leida][1]]
        valor = str(valor*dicc_factor[banda_leida][0])
        print("Banda (Tolerancia)",str(bandas)+") :")
        banda_leida = str(input())
        banda_leida = banda_leida.lower()
        valor += dicc_tolerancia[banda_leida][0]
        lista_bandas += [dicc_tolerancia[banda_leida][1]]
        lista_final = [lista_bandas] + [valor] + [bandas]
    print("El valor de la resistencia es de :"+valor+"Ohms")
    historial['Fisica'].append('Lectura de resistencias \n\t'+str(valor)+'Vatios')
    return(lista_final)
    
def Constantes_electromagnetismo():
    """
    Parametros: N.A
    Definicion: En esta funcion se  genera un submenu para direccionar a un 
    imprimible en pantalla con el valor de una constante o  a una relacion entre dos 
    unidades de medidas distintas, con la ayuda de la funcion regla_de_tres 
    """
    rta = True
    while rta:
        borrarPantalla()
        cte_electromagnetismo = {1:"La constante de Coulumb es 8.99*10^9 N*m^2/C^2",2:"La carga de un electron es de 1.6 * 10^-19 N*m^2/kg^2",3:[[1,3.6],["m/s","Kmh"]],4:[[1,2.54],["in","cm"]]}
        print (""" BIENVENIDO A LA SECCION DE CONSTANTES DE ELECTROMAGNETISMO
        Por favor, digite el numero de la constante, relacion o proceso:
        \t 1) Constante de Coulumb
        \t 2) Carga de un electron
        \t 3) km/h : m/s
        \t 4) in : cm
        """)
        try:
            entrada = int(input())
            if entrada > 2:
                Regla_de_tres(cte_electromagnetismo[entrada])
            else:
                print(cte_electromagnetismo[entrada])
            rta = VolverAntes()
        except FloatingPointError:
            print('Ingrese, por favor, las magnitudes numericas reales separadas per un punto (.)')
            time.sleep(2)
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(2)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(2)
        except ZeroDivisionError:
            print('Ingrese, por favor, una magnitud distinta a cero en el denominador')
            time.sleep(2)

def Ondas():
    """
    La funcion ondas tiene como proposito direccionar a las funciones contenidas
    en esta, las cuales son las que realizan los calculos. Esta tiene un diccioanrio
    llamado "dicc_ondas" con posibles constantes que pueden ser invocadas, 
    asi como funciones que se usan dentro de las funciones de calculo como 'sumatoria'.
    Esta tiene como entrada un string con el nombre de la variable a conocer.   
    """
    dicc_ondas= {1:Vel_onda,2:Frecuencia_onda,3:Longitud_onda,4:Cambio_temperatura,5:Constantes_ondas}
    rta = True
    while rta:
        borrarPantalla()
        print (""" BIENVENIDO A LA SECCION ONDAS
        Por favor, digite el numero de la varaible o proceso:
        \t 1) Velocidad de una onda
        \t 2) Frecuencia de una onda
        \t 3) Longitud de onda
        \t 4) Cambio de velocidad por temperatura
        \t 5) Constantes o conversor de medidas
        """)
        try:
            dicc_ondas[int(input())]()
            rta = VolverAntes()
        except FloatingPointError:
            print('Ingrese, por favor, las magnitudes numericas reales separadas per un punto (.)')
            time.sleep(10)
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(10)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(10)
        except ZeroDivisionError:
            print('Ingrese, por favor, una magnitud distinta a cero en el denominador')
            time.sleep(10)

def Vel_onda():
    """
    Parametros: N.A
    Definicion: En esta funcion se  encarga de hacer una relacion del voltaje
    """ 
    print("Por favor, ingrese la magnitud de la longitud de onda en m")
    longitud = float(input())
    print("Por favor, ingrese la magnitud de la frecuencia en Hz")
    frecuencia = float(input())
    velocidad = round(longitud*frecuencia,3)
    if velocidad > 299792458 or -299792458 > velocidad:
        print("La velocidad no puede sobrepasar la costante de la velocidad de la luz, por favor ingrese datos reales ")
    else:
        print("La velocidad es de"+str(round(velocidad,3))+"m/s")
        historial['Fisica'].append('Velocidad onda \n\t'+str(round(velocidad,3))+'m/s')

def Frecuencia_onda():
    dicc_ingreso = {1:input ,2:Velocidad} 
    rta = True
    while rta:
        borrarPantalla()
        print ("""
        Para el valor de velocidad desea:
        1) Ingresarlo (en este caso debe ingresar le valor en m/s despues de marcar a opcion)
        2) Calcularlo
        """)
        try:
            vel = float(dicc_ingreso[int(input())]())
            print("Por favor, ingrese la magnitud de la longitud de onda en m")
            longitud = float(input())
            print("El valor de la frecuencia es de"+str(round(vel/longitud,3))+"Hz")
            historial['Fisica'].append('Frecuencia onda \n\t'+str(round(vel/longitud,3))+"Hz")
            rta = VolverAntes()
        except FloatingPointError:
            print('Ingrese, por favor, las magnitudes numericas reales separadas por un punto (.)')
            time.sleep(5)
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(5)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(5)
        except ZeroDivisionError:
            print('Ingrese, por favor, una magnitud distinta a cero en el denominador')
            time.sleep(5)

def Longitud_onda():
    dicc_ingreso = {1:input ,2: Velocidad} 
    rta = True
    while rta:
        borrarPantalla()
        print ("""
        Para el valor de velocidad desea:
        1) Ingresarlo (en este caso debe ingresar le valor en m/s despues de marcar a opcion)
        2) Calcularlo
        """)
        try:
            vel = float(dicc_ingreso[int(input())]())
            print("Por favor, ingrese la magnitud de la frecuencia en Hz")
            frecuencia = float(input())
            print("El valor de la longitud de onda es de"+str(round(vel/frecuencia,3))+"m")
            historial['Fisica'].append('Longitud onda \n\t'+str(round(vel/frecuencia,3))+"m")
            rta = VolverAntes()
        except FloatingPointError:
            print('Ingrese, por favor, las magnitudes numericas reales separadas por un punto (.)')
            time.sleep(5)
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(5)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(5)
        except ZeroDivisionError:
            print('Ingrese, por favor, una magnitud distinta a cero en el denominador')
            time.sleep(5)
    
def Cambio_temperatura():
    """
    Parametros: N.A
    Definicion: En esta funcion se  encarga de hacer una relacion del voltaje
    """ 
    print("Por favor, ingrese la magnitud de la temperatura inicial en K")
    temperatura_inicial = float(input())
    print("Por favor, ingrese la magnitud de la temperatura final en K")
    temperatura_final = float(input())
    print("Por favor, ingrese la magnitud de la velocidad inicial en m/s")
    velocidad_inicial = float(input())
    if velocidad_inicial > 299792458 or -299792458 > velocidad_inicial:
        print("La velocidad no puede sobrepasar la costante de la velocidad de la luz, por favor ingrese datos reales ")
    else:
        velocidad = velocidad_inicial*(temperatura_final/temperatura_inicial)**(1/2)
        print(velocidad)
        if velocidad > 299792458 or -299792458 > velocidad:
            print("La velocidad no puede sobrepasar la costante de la velocidad de la luz, por favor ingrese datos reales ")
        else:
            print("La nueva velocidad es de"+str(round(velocidad,3))+"m/s la anterior velocidad era:"+str(round(velocidad_inicial,3))+"m/s" )
            historial['Fisica'].append('Cambio de velocidad \n\tde'+str(round(velocidad_inicial,3))+"m/s a "+str(round(velocidad,3))+"m/s")
  
def Constantes_ondas():
    """
    Parametros: N.A
    Definicion: En esta funcion se  genera un submenu para direccionar a un 
    imprimible en pantalla con el valor de una constante o  a una relacion entre dos 
    unidades de medidas distintas, con la ayuda de la funcion regla_de_tres 
    """
    rta = True
    while rta:
        borrarPantalla()
        cte_ondas = {1:Cambio_temp(["K","Cº"]),2:Regla_de_tres([[1,10^-10],["Angstrom (A)","m"]])}
        print (""" BIENVENIDO A LA SECCION DE CONSTANTES DE ELECTROMAGNETISMO
        Por favor, digite el numero de la constante, relacion o proceso:
        \t 1) K : Cº
        \t 2) Angstrom (A) : m
        """)
        try:
            entrada = int(input())
            cte_ondas[entrada]
            rta = VolverAntes()
        except FloatingPointError:
            print('Ingrese, por favor, las magnitudes numericas reales separadas per un punto (.)')
            time.sleep(2)
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(2)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(2)
        except ZeroDivisionError:
            print('Ingrese, por favor, una magnitud distinta a cero en el denominador')
            time.sleep(2)

def Sumatoria(variable_a_sumar,verdad):
    """
    Parametros: variable_a_sumar= cadena de caracteres con el nombre de la variable a calcular
                verdad = booleano que define si solo se suman dos magnitudes
    Definicion: En esta funcion se  encara de invocar sumatorias y luego hacer una diferencia
    """
    if verdad:
        print('Por favor, ingresar las magnitudes de', variable_a_sumar," en su respectiva medidia del S.I y terminar con (0)")
        Sumatoria = 0
        while True:
            magnitud = float(input())
            if magnitud == 0:
                break
            Sumatoria += magnitud
        return(Sumatoria)
    else:
        print('Por favor, ingresar dos magnitudes de', variable_a_sumar," en su respectiva medidia del S.I")
        Sumatoria = 0
        for magnitud in range(2):
            magnitud = float(input())
            Sumatoria += magnitud
        return(Sumatoria)

def Regla_de_tres(relacion):
    """
    Parametros: relacion= lista compuesta de 2 sublistas, una contiene los dos valores
    enteros de la relacion entre unidades de medida, mientras que la otra tiene las 
    cadenas de carateres con los simbolos de dichas unidades 
    Definicion: En esta funcion usa una regla de tres, para convertir de una unidad de medida a otra
    """ 
    borrarPantalla()
    print("Por favor, ingrese la magnitud de la variable principal")
    variable_principal = float(input()) 
    print("escoja el numero de la denominacion de la variable de la siguente lista")
    for llave in relacion[1]:
        print(str(relacion[1].index(llave)+1)+")",llave)
    entrada = int(input())
    if entrada == 1:
        regla_tres = (variable_principal*relacion[0][1])/relacion[0][0]
        print("El resultado es:",str(round(regla_tres,3)),relacion[1][1])
    elif entrada == 2:
        regla_tres = (variable_principal*relacion[0][0])/relacion[0][1]
        print("El resultado es:",str(round(regla_tres,3)),relacion[1][0])
        
    else:
        print(int(relacion))

def Cambio_temp(lista):
    print("Elija el numero de la variable:")
    for unidad in lista:
        print((str(lista.index(unidad)+1))+")",unidad)
    entrada = int(input())
    print("Ingrese la magnitud de de la temperatura en", str(lista[entrada]))
    temperatura = float(input())
    if entrada == 1:
        if temperatura <= 0:
            print("La temperarura en el sistema absoluto (K), no puede ser menor a 0")
        else:
            print("La temperatura es de "+str(round(temperatura+273.15))+str(lista[1]))
            historial['Fisica'].append('Cambio de temperatura \n\t'+str(round(temperatura+273.15))+str(lista[1]))
    elif entrada == 2:
        temperatura -= 273.15
        if temperatura <= 0:
            print("La temperarura en el sistema absoluto (K), no puede ser menor a 0")
        else:
            print("La temperatura es de "+str(round(temperatura+273.15))+str(lista[0]))
            historial['Fisica'].append('Cambio de temperatura \n\t'+str(round(temperatura+273.15))+str(lista[0]))

def Estadistica():
    est = {1: CrearDatos,2: AgregarDatos, 3: FuncionesEst, 4: GraficasEst, 5: TablasEstadisticas}
    Rta = True
    global Datos
    while Rta:
        borrarPantalla()
        print('''ELIJA UNA OPCIÓN:
            \t 1)Crear Datos
            \t 2)Agregar Datos
            \t 3)Operaciones estadisticas
            \t 4)Graficas Estadisticas
            \t 5)Tablas Estadisticas
            ''')
        try:
            entrada = int(input())
            if entrada == 1:
                Datos = est[entrada]()
            elif entrada == 2:
                try:
                    Datos = est[entrada](Datos)
                except:
                    print('No se han ingresado Datos, por favor eliga la opcion 1 para continuar')
                    Rta = VolverAntes()
            else:
                try:
                    est[entrada](Datos)
                except NameError:
                    print('No se han ingresado Datos, por favor eliga la opcion 1 para continuar')
            Rta = VolverAntes()
        except KeyError:
            print('La opcion seleccionada no se encuentra en la lista presentada')
            time.sleep(1)
        except ValueError:
            print('La opcion no es valida, tenga en cuenta que SOLO es el numero de la opcion deseada')
            time.sleep(1)
    return

def TablasEstadisticas(DatosNormales):
    try:
        os.remove('Tabla_Estadistica.csv')
        time.sleep(1)
        DatosOrd = AgruparDatos(DatosNormales)
        Tabla = open('Tabla_Estadistica.csv','w')
        Cadena = 'Intervalos,Marca de Clase,fi,Fi,hi,Hi\n'
        Tabla.write(Cadena)
        for i in range(len(DatosOrd[0])):
            Cadena = str(DatosOrd[0][i])+','+str(DatosOrd[1][i])+','+str(DatosOrd[2][i])+','+str(DatosOrd[3][i])+','+str(DatosOrd[4][i])+','+str(DatosOrd[5][i])+'\n'
            Tabla.write(Cadena)
        Tabla.close()
    except:
        DatosOrd = AgruparDatos(DatosNormales)
        Tabla = open('Tabla_Estadistica.csv','w')
        Cadena = 'Intervalos,Marca de Clase,fi,Fi,hi,Hi\n'
        Tabla.write(Cadena)
        for i in range(len(DatosOrd[0])):
            Cadena = str(DatosOrd[0][i])+','+str(DatosOrd[1][i])+','+str(DatosOrd[2][i])+','+str(DatosOrd[3][i])+','+str(DatosOrd[4][i])+','+str(DatosOrd[5][i])+'\n'
            Tabla.write(Cadena)
        Tabla.close()

def CrearDatos():
    print('Ingrese los datos separados por un espacio')
    Datos_entrada = input()
    Datos_entrada = Datos_entrada.split()
    Datos_entrada = list(map(float, Datos_entrada))
    Datos_entrada.sort()
    print('El numero de datos ingresado es: '+str(len(Datos_entrada)))
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
    FEs = {1: 'Media',2: 'Mediana',3: 'Varianza',4: 'Desviacion estandar',5: 'Coeficiente de variación',6: 'Percentil',7: 'Cuartil'}
    Fe = True
    historial['Estadistica'].append('Datos \n\t'+str(Datos))
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
            historial['Estadistica'].append(FEs[funcion]+'\n\t'+salida[0]+str(salida[1]))
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

def AgruparDatos(iDatos):
    DatosAgrupados = []
    Rango = (max(iDatos)-min(iDatos))
    NumIntervalos = int(Rango**0.5)
    Amplitud = round((Rango/NumIntervalos),1)
    Intervalos = []
    LimiteInf = min(iDatos)
    for i in range(NumIntervalos-1):
        LimiteSup = round((LimiteInf+Amplitud),1)
        iIntervalo = (LimiteInf,LimiteSup)
        Intervalos.append(iIntervalo)
        LimiteInf = LimiteSup
    iIntervalo = (LimiteInf, max(iDatos))
    Intervalos.append(iIntervalo)
    DatosAgrupados.append(Intervalos)
    MarcasDeClase = [round(((Intervalos[i][0]+Intervalos[i][1])/2),1) for i in range(NumIntervalos)]
    DatosAgrupados.append(MarcasDeClase)
    FrecuenciasAbs = [0 for i in range(NumIntervalos)]
    for i in range(NumIntervalos):
        for j in range(len(iDatos)):
            if (iDatos[j] >= Intervalos[i][0]) and (iDatos[j] < Intervalos[i][1]):
                FrecuenciasAbs[i] += 1
    if (iDatos[j] >= Intervalos[len(Intervalos)-1][0]) and (iDatos[j] <= Intervalos[len(Intervalos)-1][1]):
        FrecuenciasAbs[NumIntervalos-1] +=1
    DatosAgrupados.append(FrecuenciasAbs)
    FrecuenciasAbsAcum = [FrecuenciasAbs[0]]
    for i in range(1,len(FrecuenciasAbs)):
        iFrecuenciaAbsAcum = FrecuenciasAbs[i] + FrecuenciasAbsAcum[i-1]
        FrecuenciasAbsAcum.append(iFrecuenciaAbsAcum)
    DatosAgrupados.append(FrecuenciasAbsAcum)
    FrecuenciasRel = [round((FrecuenciasAbs[i]/len(iDatos)),2) for i in range(NumIntervalos)]
    DatosAgrupados.append(FrecuenciasRel)
    FrecuenciasRelAcum = [FrecuenciasRel[0]]
    for i in range(1,len(FrecuenciasAbs)):
        iFrecuenciaRelAcum = FrecuenciasRel[i] + FrecuenciasRelAcum[i-1]
        FrecuenciasRelAcum.append(iFrecuenciaRelAcum)
    DatosAgrupados.append(FrecuenciasRelAcum)
    return DatosAgrupados

def GraficoPastel(DatosAgrupados):
    plt.style.use('seaborn-colorblind')
    slices = DatosAgrupados[2]
    labels = ['Intervalo'+str(DatosAgrupados[0][i]) for i in range(len(DatosAgrupados[1]))]
    plt.pie(slices, labels=labels, shadow=True, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
    print('Ingrese un titulo para el diagrama de pastel:')
    Titulo = input()
    plt.title(Titulo)
    plt.tight_layout()
    plt.show()

def Histograma(Datos, DatosAgrupados, Mediana):
    plt.style.use('fivethirtyeight')
    NumBins = len(DatosAgrupados[0])
    bins = []
    for i in range(len(DatosAgrupados[0])):
        bins.append(DatosAgrupados[0][i][0])
        bins.append(DatosAgrupados[0][i][1])
    plt.hist(Datos,color='#e377c2', bins=bins, edgecolor='black')
    color = '#ff7f0e'
    plt.axvline(Mediana, color=color, label='Mediana', linewidth=2)
    plt.legend()
    print('Ingrese un titulo para el diagrama de barras:')
    Titulo = input()
    plt.title(Titulo)
    plt.xlabel('Intervalos')
    plt.ylabel('# de elementos por intervalo')
    plt.tight_layout()
    plt.show()

def Ojiva(DatosAgrupados):
    plt.style.use('seaborn-colorblind')
    ages_x = DatosAgrupados[1]
    dev_y = DatosAgrupados[5]
    plt.plot(ages_x, dev_y, color='#444444',marker='*', label='All Devs')
    plt.xlabel('Marcas de clase del intervalo')
    plt.ylabel('Frecuencias relativas acumuladas')
    print('Ingrese un titulo para el diagrama de Ojiva:')
    Titulo = input()
    plt.title(Titulo)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def GraficasEst(Datos):
    grafs = {1: GraficoPastel, 2: Histograma, 3: Ojiva}
    DatosAgrupados = AgruparDatos(Datos)
    Fe = True
    while Fe:
        borrarPantalla()
        print('''ELIJA UNA FUNCIÓN: 
        \t 1)Grafico Pastel
        \t 2)Histograma
        \t 3)Ojiva
        ''')
        try:
            funcion = int(input())
            salida = grafs[funcion](DatosAgrupados)
            Fe = VolverAntes()
        except:
            print('Opcion invalida')
    return

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
    
def Contra(usuario):
    Mensaje = usuario
    Mensaje = Mensaje.split(' ')
    Semilla = 213
    Limite = 1000000
    PesosLista = Peso(Mensaje, Semilla)
    CheckSumLista = CheckSum(PesosLista, Semilla, Limite)
    resultado = CheckSumLista[len(CheckSumLista)-1]
    return resultado
    
def Login():
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
            cont = str(Contra(user))
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
                    time.sleep(1.5)
                    break
                else:
                    print('Las contrasenas no coinciden')
                    time.sleep(1.5)
    with open('usuarios.py','w') as usernames:
        usernames.write('usuarios ='+str(us)+'\n')
    return True

def Logo_principal():
    """
    funcion sin parametros de entrada
    En esta funcion se crea un logo con la libreria turtle con las siguentes caracterisiticas:
    Crea un fractal controlado por recursion 
    Crea la imagen de una calculadora
    Crea la imagen de el nombre del proyecto ()
    Envia mensajes en la ventana de turtle
    Se cierra con un click del usuario 
    """
    def Imagen(tortuga):
        """
        parametros:
        tortuga= elemento con el que se va hacer la imagen
        En esta funcion se crea una imagen de una calculadora, unicamente con funciones de turtle, con una funcion que crea cuadrilateros
        """
        def Cuadrilateros(tortuga,color,inicio,largo,alto):
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
            tortuga.speed(0)
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
        Cuadrilateros(tortuga,0,[-100,120],200,300)
        Cuadrilateros(tortuga,1,[-80,335],160,60)
        lista = [[-70,250],[-70,150],[20,250],[20,150]]
        for posicion in lista:
            Cuadrilateros(tortuga,2,posicion,50,50)
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
    def Escribir(tortuga):
        """
        Parametros:
        tortuga= elemento con el que se posiciona los mensajes escritos en pantalla
        la funcion es la encargada de usar la libreria turtle para posicionar mensajes en pantalla, a estos mesajes se les puede introducir valores de fuentes y tamanos de letras
        """
        tortuga.hideturtle()
        tortuga.up()
        tortuga.goto(-300,-100)
        tortuga.write("CALCULADORA",font=("Arial",17,"normal"))
        tortuga.goto(-80,-245)
        tortuga.write("2020-1",font=("Arial",10,"normal"))
        tortuga.goto(0,-10)
        tortuga.write("\"fuente de investigacion\"",align=("center"),font=("castellar",12,"normal"))
        tortuga.goto(0,-350)
        tortuga.write("(Haga click en la ventana para continuar)",align=("center"),font=("times new roman",7,"normal"))
        tortuga.goto(0,-350)   
    def Fractal(tortuga,espaciador,puntos):
        """
        Parametros:
        tortuga= elemento con el que se dibuja la fuente
        espaciador=entero con el que se se realiza la recursion 
        puntos= lista con los valores que cambian para definir el tamanno y posicion de las lineas
        la funcion usa la recursion de la funcion llamada "koch" para generar lineas horizontales que simulan una fuente
        """
        def Dibujar(puntos,tortuga):
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

        def Division(lista, valor):
            """
            Parametros:
            lista = lista con los valores de los puntos la cual seran cambiados con esta funcion
            valoer = entero con que sirve de factor para cambiar el valor de los puntos de la lista
            La funcion se encarga de cambiar los valores de la lista de puntos con una division entre el valor
            """
            puntos = [[lista[0][0]/valor,lista[0][1]+30/valor], [lista[1][0]/valor,lista[1][1]+30/valor]]
            return puntos

        def Koch(puntos,grado,tortuga):
            """
            Parametros:
            grado = entero que se disminuye para llegar al caso base de la recursion
            tortuga= elemento con el que se dibuja la fuente
            puntos= lista de valores con los que se forman las lineas
            la funcion es la encargada de la recursion de las linaeas para cambiar los valores y posicion, se basa en la teoria del matematico Helge Von Koch para cambiar los valores del
            tamano de las lineas por medio de los puntos
            """
            Dibujar(puntos,tortuga)
            if grado > 0:
                for numero in range(2,4):
                    Koch(Division(puntos,numero),grado-1, tortuga)
        tortuga.hideturtle()
        tortuga.speed(0)
        Koch(Division(puntos,3),espaciador,tortuga)
    def Nombre(tortuga):
        """
        parametros:
        tortuga= elemento con el que se escribe el nombre del proyecto
        En esta funcion se escribe el nombre del proyecto, unicamente con funciones de turtle, sin funciones adicionales
        """
        tortuga.hideturtle()
        tortuga.up()
        tortuga.goto(-300,-100)
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
        tortuga.fillcolor("black")
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
    def Linea_media(tortuga):
        tortuga.hideturtle()
        tortuga.up()
        tortuga.pensize(5)
        tortuga.goto(0,-70)
        tortuga.down()
        tortuga.right(90)
        tortuga.forward(200)
    def Logo_un():
        alex = turtle.Turtle()
        alex.color('green')
        alex.speed(0)
        alex.hideturtle()
        alex.fillcolor('green')
        alex.begin_fill()
        alex.up()
        alex.goto(200,-205)
        alex.down()
        alex.circle(70)
        alex.end_fill()
        alex.goto(200,-200)
        alex.left(90)
        alex.forward(91)
        alex.left(90)
        alex.forward(49)
        alex.color('white')
        alex.fillcolor('white')
        alex.begin_fill()
        alex.left(90)
        alex.forward(42)
        alex.circle(14,90)
        alex.forward(31.5)
        alex.left(90)
        alex.forward(56)
        alex.left(90)
        alex.forward(7)
        alex.left(90)
        alex.forward(33)
        alex.circle(-15.75,180)
        alex.forward(33)
        alex.left(90)
        alex.forward(7)
        alex.end_fill()
        alex.up()
        alex.goto(200,-200)
        alex.left(180)
        alex.forward(49)
        alex.left(90)
        alex.forward(35)
        alex.down()
        alex.fillcolor('white')
        alex.begin_fill()
        alex.forward(42)
        alex.circle(14,90)
        alex.forward(31.5)
        alex.left(90)
        alex.forward(56)
        alex.left(90)
        alex.forward(7)
        alex.left(90)
        alex.forward(33)
        alex.circle(-15.75,180)
        alex.forward(33)
        alex.left(90)
        alex.forward(7)
        alex.end_fill()
        alex.up()
        alex.goto(205,-235)
        alex.color('black')
        alex.down()
        alex.write('UNIVERSIDAD NACIONAL DE COLOMBIA',align=('center'),font=('Ancizar sans',15))
    pantalla = turtle.Screen()
    pantalla.title("Logo FEM")
    pantalla.setup(900,850,200,0)
    pantalla.bgcolor("light blue")
    a = turtle.Turtle()
    b = turtle.Turtle()
    c = turtle.Turtle()
    d = turtle.Turtle()
    e = turtle.Turtle()
    a.pensize(2)
    b.pensize(6)
    c.pensize(2)
    d.pensize(10)
    a.pencolor("green")
    b.pencolor("black")
    c.pencolor("black")
    Fractal(a,3,[[-500,10],[500,10]])
    Imagen(b)
    Nombre(c)
    Linea_media(e)
    Logo_un()
    Escribir(d)   
    pantalla.exitonclick()
    pantalla.title("Calculadora_resistencias")

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
        HUser.write('--------------------------------------------------------------------------------\n')
        HUser.write('Entrada: '+inicio+'\n')
        for linea in historial:
            HUser.write(linea+'\n')
            if len(historial[linea]) != 0:
                for contenido in historial[linea]:
                    HUser.write('\t'+contenido+'\n')
            else:
                HUser.write('\tNo se realizaron operaciones en esta funcion\n')
        HUser.write('Salida: '+fin+'\n')
        HUser.write('')
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
    Logo_principal()
    funciones = {1:Matematicas,2:Estadistica,3:Fisica}
    bandera = Login()
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
            time.sleep(3)    
    salida = time.strftime("%d-%m-%Y %H:%M", time.localtime())
    print('Desea guardar su historial?')
    respuestahisto = input().lower()
    if respuestahisto == 'si':
        GuardarHistorial(entrada,salida)
    print('Vuelva Pronto')
    time.sleep(10)    

main()