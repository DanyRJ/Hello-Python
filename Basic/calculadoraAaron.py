# Funcion General
def introducirNumeros ():
    global numero1, numero2
    numero1 = int(input('Introduzca el primer numero: '))
    numero2 = int(input('Introduzca el segundo numero: '))

# Funcion sumar 
def sumar (a , b):
    print('La suma de ',a,' + ',b,' = ' ,a+b)
    
# Funcion restar 
def restar (a , b):
    print('La resta de ',a,' - ',b,' = ' ,a-b)
    
# Funcion multiplicacion
def multiplicacion (a , b):
    print('La multiplicacio de ',a,' * ',b,' = ' ,a*b)

# Funcion division 
def division (a , b):
    if b == 0:
        print('No se puede dividir entre cero')
    else:    
        print('La division de ',a,' / ',b,' = ' ,a/b)
        
# Crear menu
while True:
    print(
        '=============================== \n'
        '=         CALCULADORA         = \n'             
        '=============================== \n'
        '= 1.Sumar                     = \n'
        '= 2.Restar                    = \n'
        '= 3.Multiplicar               = \n' 
        '= 4.Dividir                   = \n'
        '= 5.Salir                     = \n'
        '=============================== \n' 
        'Que opcion desea realizar(1-4) '
    )
    
    eleccion = int(input())
    
    if eleccion == 1:
        introducirNumeros()
        sumar(numero1,numero2)
    elif eleccion == 2:
        introducirNumeros()
        restar(numero1,numero2)
    elif eleccion == 3:
        introducirNumeros()
        multiplicacion(numero1,numero2)
    elif eleccion ==4: 
        introducirNumeros()
        division(numero1,numero2)
    elif eleccion ==5:
        print('Gracias por su consulta, hasta pronto.')
        break