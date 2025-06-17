def triangulo_lleno(altura):
    for i in range(1, altura + 1):
        print('*' * i)

def main():
    try:
        altura = int(input("Ingrese la altura del triángulo: "))
        if altura < 1:
            print("La altura debe ser mayor o igual a 1.")
        else:
            print("\nTriángulo lleno:\n")
            triangulo_lleno(altura)
    except ValueError:
        print("Por favor ingrese un número entero válido.")

if __name__ == "__main__":
    main()

def triangulo_centrado(altura):
    for i in range(1, altura + 1):
        espacios = ' ' * (altura - i)
        estrellas = '*' * (2 * i - 1)
        print(espacios + estrellas)

def main():
    try:
        altura = int(input("Ingrese la altura del triángulo: "))
        if altura < 1:
            print("La altura debe ser mayor o igual a 1.")
        else:
            print("\nTriángulo centrado:\n")
            triangulo_centrado(altura)
    except ValueError:
        print("Por favor ingrese un número entero válido.")

if __name__ == "__main__":
    main()
