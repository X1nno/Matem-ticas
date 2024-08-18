from os import system
system("cls")
import math
import sympy as sp

def menu():
    while True:
        print("\n--- Menú de Operaciones Matemáticas Aplicadas ---")
        print("1. Calcular derivada (ejemplo: 2*x**2 + 3*x + 1)")
        print("2. Calcular integral (ejemplo: x**3 + 2*x**2)")
        print("3. Resolver ecuación cuadrática (ejemplo: a=1, b=-3, c=2)")
        print("4. Resolver sistema de ecuaciones lineales (ejemplo: 2*x + y - 3, x - y - 2)")
        print("5. Calcular valor presente o futuro (ejemplo: P=1000, r=0.05, n=10)")
        print("6. Calcular área bajo la curva (ejemplo: x**2, a=0, b=2)")
        print("7. Calcular límite (ejemplo: sin(x)/x cuando x tiende a 0)")
        print("8. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            calcular_derivada()
        elif opcion == "2":
            calcular_integral()
        elif opcion == "3":
            resolver_ecuacion_cuadratica()
        elif opcion == "4":
            resolver_sistema_ecuaciones()
        elif opcion == "5":
            calcular_valor_presente_futuro()
        elif opcion == "6":
            calcular_area_bajo_curva()
        elif opcion == "7":
            calcular_limite()
        elif opcion == "8":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

def calcular_derivada():
    x = sp.symbols('x')
    funcion = input("Ingresa la función en términos de x (ejemplo: 2*x**2 + 3*x + 1): ")
    derivada = sp.diff(funcion, x)
    print(f"La derivada de {funcion} es {derivada}")

def calcular_integral():
    x = sp.symbols('x')
    funcion = input("Ingresa la función en términos de x (ejemplo: x**3 + 2*x**2): ")
    integral = sp.integrate(funcion, x)
    print(f"La integral de {funcion} es {integral}")

def resolver_ecuacion_cuadratica():
    a = float(input("Ingresa el coeficiente a (ejemplo: 1): "))
    b = float(input("Ingresa el coeficiente b (ejemplo: -3): "))
    c = float(input("Ingresa el coeficiente c (ejemplo: 2): "))
    
    discriminante = b**2 - 4*a*c
    if discriminante >= 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"Las soluciones son {raiz1} y {raiz2}")
    else:
        print("La ecuación no tiene soluciones reales.")

def resolver_sistema_ecuaciones():
    print("Ejemplo: 2*x + y - 3 = 0 y x - y - 2 = 0")
    ecuacion1 = input("Ingresa la primera ecuación: ")
    ecuacion2 = input("Ingresa la segunda ecuación: ")
    
    x, y = sp.symbols('x y')
    eq1 = sp.Eq(eval(ecuacion1), 0)
    eq2 = sp.Eq(eval(ecuacion2), 0)
    
    solucion = sp.solve((eq1, eq2), (x, y))
    print(f"La solución es: {solucion}")

def calcular_valor_presente_futuro():
    P = float(input("Ingresa el valor presente (P) (ejemplo: 1000): "))
    r = float(input("Ingresa la tasa de interés (r) en decimal (ejemplo: 0.05 para 5%): "))
    n = int(input("Ingresa el número de períodos (n) (ejemplo: 10): "))
    
    FV = P * (1 + r)**n
    PV = FV / (1 + r)**n
    
    print(f"Valor Futuro (FV): {FV}")
    print(f"Valor Presente (PV): {PV}")

def calcular_area_bajo_curva():
    x = sp.symbols('x')
    funcion = input("Ingresa la función en términos de x (ejemplo: x**2): ")
    a = float(input("Ingresa el límite inferior de integración (a) (ejemplo: 0): "))
    b = float(input("Ingresa el límite superior de integración (b) (ejemplo: 2): "))
    
    area = sp.integrate(funcion, (x, a, b))
    print(f"El área bajo la curva de {funcion} entre {a} y {b} es {area}")

def calcular_limite():
    x = sp.symbols('x')
    funcion = input("Ingresa la función en términos de x (ejemplo: sin(x)/x): ")
    punto = float(input("Ingresa el punto al que se aproxima x (ejemplo: 0): "))
    
    limite = sp.limit(funcion, x, punto)
    print(f"El límite de {funcion} cuando x tiende a {punto} es {limite}")


if __name__ == "__main__":
    menu()
