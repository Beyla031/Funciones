# @ sumar
# n1, solicita u numero
# n2, solicita otro número
# return, la suma de los dos

def sumar(n1, n2):
    return n1+n2


# @ restar
# n1, solicita u numero
# n2, solicita otro número
# return, la resta de los dos


def restar(n1,n2):
    return n1-n2



# @ dividir
# n1, solicita u numero
# n2, solicita otro número
# return, la divide de los dos

def divide(n1,n2):
    return n1/n2


# @ multiplica
# n1, solicita u numero
# n2, solicita otro número
# return, la multiplica de los dos

def multiplicar(n1,n2):
    return n1*n2



numero1 = 10
numero2 = 5

def operaciones(nombre,n1,n2):
    print(nombre)
    print(15*"-")
    print("Suma:", sumar(numero1,numero2))
    print("Resta:", restar(numero1,numero2))
    print("Divide:", divide(numero1,numero2))
    print("Multiplicación:", multiplicar(numero1,numero2))
    print(15*"-")

    def informacion(nombre,edad):
        print("Nombre",nombre)
        print("Edad",edad)
    informacion("Beyla",17)


operaciones("Beyla",10,5)


