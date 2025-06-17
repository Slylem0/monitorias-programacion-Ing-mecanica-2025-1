def rectangulo_lleno(ancho, alto):
    for _ in range(alto):
        print('*' * ancho)

def rectangulo_vacio(ancho, alto):
    for fila in range(alto):
        if fila == 0 or fila == alto - 1:
            print('*' * ancho)
        else:
            print('*' + ' ' * (ancho - 2) + '*')

def main():
    ancho = int(input("Ingrese el ancho del rectángulo: "))
    alto = int(input("Ingrese el alto del rectángulo: "))

    print("\nRectángulo lleno:\n")
    rectangulo_lleno(ancho, alto)

    print("\nRectángulo vacío:\n")
    if ancho >= 2 and alto >= 2:
        rectangulo_vacio(ancho, alto)
    else:
        print("No se puede dibujar un rectángulo vacío con esas dimensiones.")


if __name__ == "__main__":
    main()
