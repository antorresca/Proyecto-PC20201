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

derivar()