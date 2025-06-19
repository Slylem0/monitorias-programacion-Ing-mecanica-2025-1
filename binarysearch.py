def adivinar_numero():
    print("Piensa en un número del 1 al 100 y yo lo adivinaré.")
    input("Presiona Enter cuando estés listo...")

    bajo = 1
    alto = 100
    intentos = 0

    while bajo <= alto:
        medio = (bajo + alto) // 2
        intentos += 1
        respuesta = input(f"¿Es {medio} tu número? (sí/no): ").lower()

        if respuesta == "si":
            print(f"¡Genial! Adiviné tu número en {intentos} intentos.")
            break
        else:
            pista = input(f"¿Tu número es mayor o menor que {medio}? (mayor/menor): ").lower()
            if pista == "mayor":
                bajo = medio + 1
            elif pista == "menor":
                alto = medio - 1
            else:
                print("Por favor responde con 'mayor' o 'menor'.")
    else:
        print("Parece que hubo un error o el número no estaba entre 1 y 100.")

adivinar_numero()
