def otra_consulta():
    repetir_consulta = input("¿Deseas hacer otra consulta?\n1. Sí\n2. No\n\n\t--> :  ")
    if repetir_consulta == "1":
        return True
    elif repetir_consulta == "2":
        print("\n\nGracias por usar la calculadora IMC...\n\n")
        return False
    else:
        print("\nOpción no válida, por favor ingresa 1 o 2.\n")
        return otra_consulta()


def calcular_imc():
    peso = int(input("Ingrese el peso en (kg) de la persona: "))
    altura_cm = int(input("Ingrese la altura en (cm) de la persona: "))
    altura_m = altura_cm / 100

    imc = peso / (altura_m ** 2)

    if imc < 18.5:
        print("\ncuidado! estás en bajo peso")

    elif 18.5 <= imc < 25:
        print("\nEstás normal de peso, sigue así!")

    elif 25 <= imc < 30:
        print("\ncuidado! estás sobrepeso")

    else:
        print("\nTe encuentras en obeso")

    print(f"Tu IMC es: {imc:.2f}")

    return otra_consulta()


while True:
    if not calcular_imc():
        break
