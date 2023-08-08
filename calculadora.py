import math
import os

#Funciones de las operaciones basicas de una calculadora. Suma, resta, multiplicación, división, potenciacion, radicación, porcetaje y operaciones con parentesis.

def suma(a, b):
    os.system("cls")
    return a + b



def resta(a, b):
    os.system("cls")
    return a - b



def multiplicacion(a, b):
    os.system("cls")
    return a * b



def division(a, b):
    os.system("cls")
    if b != 0:
        return a / b
    else:
        raise ValueError("Division por cero")



def potencia(a, b):
    os.system("cls")
    return a ** b



def radicacion(a):
    os.system("cls")
    if a >= 0:
        return math.sqrt(a)
    else:
        raise ValueError("No se puede calcular la raiz cuadrada de un número negativo")



def porcentaje(numero, porcentaje):
    os.system("cls")
    return (numero * porcentaje) / 100



def operaciones_con_parentesis(expresion):
    os.system("cls")
    try:
        return eval(expresion)
    except Exception:
        print("Entrada inválida. Por favor, ingrese un numero valido.")



#Este menú es para que sea un poco más sencillo para hacer las operaciones.

def menu():
    print("Hola!! Bienvenido a la calculadora :)")
    print()
    print("Menú de operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz Cuadrada")
    print("7. Porcentaje")
    print("8. Operaciones con paréntesis")
    print("9. Salir")

def main():
    while True:
        menu()
        opcion = int(input("Selecciona una operación (1-9): "))
        
        if opcion == 9:
            print("Gracias por usar la calculadora. Nos vemos luego UwU")
            break
        
        if opcion < 1 or opcion > 9:
            os.system("cls")
            print("Opción inválida. Por favor, eliga una opción que se muestre en el menú.")
            continue
        
        if opcion in [1, 2, 3, 4, 5, 6]:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                
                if opcion == 1:
                    print("Resultado:", suma(num1, num2))
                elif opcion == 2:
                    print("Resultado:", resta(num1, num2))
                elif opcion == 3:
                    print("Resultado:", multiplicacion(num1, num2))
                elif opcion == 4:
                    try:
                        print("Resultado:", division(num1, num2))
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un numero valido.")
                elif opcion == 5:
                    print("Resultado:", potencia(num1, num2))

            except ValueError:
                print("Entrada inválida. Por favor, ingrese un numero valido.")

        elif opcion == 6: 
            try:
                num = float(input("Ingresa un número: "))
                print("Resultado:", radicacion(num))
            except ValueError:("Entrada inválida. Por favor, ingrese un numero valido.") 
        elif opcion == 7: 
            try:
                num = float(input("Ingresa un número: "))
                porc = float(input("Ingresa el porcentaje a calcular: "))
                print("Resultado:", porcentaje(num, porc))
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un numero valido.")
        
        elif opcion == 8:
            expresion = input("Ingresa una operación con paréntesis")
            print("Resultado:", operaciones_con_parentesis(expresion))
    
        
if __name__ == "__main__":
    main()