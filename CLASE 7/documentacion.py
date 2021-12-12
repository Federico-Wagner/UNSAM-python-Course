#EJERCICIO 7.8 DOCUMENTACION
# 1
def valor_absoluto(n):
    ''' Devuelve el valor absoluto del valor n que ingresa a la funcion
    PreC: El valor de n debe ser de tipo int o float (numerico)
    posC: El valor retornado sera el modulo del valor ingresado y del mismo tipo
    '''
    if n >= 0:
        return n
    else:
        return -n
#Esta funcion no posee un ciclo en su interior por lo
# cualno se puede considerar que existaun invariante

#2
def suma_pares(l):
    ''' Devuelve la suma de todos los numeros pares de una variable iterable
    PrecC: el valor suministrado a l debe ser de tipo iterable y estar compuesto por valores de tipo int o float
    PosC: El valor devuelto sera numerico correspondiente a la suma de todos los elementos pares
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0
    return res
# El invariante de esta funcion es la variable res la cual durante la ejecucion del
# codigo, poseera la suma parcial hasta el elemento que se encuentre ejecutando

#3
def veces(a, b):
    '''Devuelve a * b siempre y cuando b sea un numero positivo
    PreC:   -El valor de a debe pertenecer a los numeros racionales.
            -El valor de b debe pertenecer a los numeros entreroslos positivos incluyendo al 0
    PosC:   -Entregara la suma de el valor de a una cantidad de b veces
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
#Esta funcion posee dos invariantes nb y res los cuales nb contara las veces que falta sumar a en
# un cuenta regresiva y res llevara la suma parcial de cada ciclo hasta llegar al valor de a*b

#4
def collatz(n):
    ''' Devuelve el valor de res siendo este la cantidad de veces mas 1 que se ejecuto el ciclo while de la funcion
    PreC: n debe ser de tipo numerico
    PosC: Devuelve la cantida de veces que n fue impoar durante el ciclo while
    '''
    res = 1
    while n!=1:
        if n % 2 == 0:
            n = n//2  #divido por 2 y obtengo la parte entera del resultado
        else:
            n = 3 * n + 1
        res += 1
    return res
#El invariante de esta funcion es res el mismo lleva una cuenta de la cantidad
# de veces que fue ejecutado el ciclo while dentro de la funcion mas uno