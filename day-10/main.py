from art import logo
print (logo)

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

def ask_for_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Debe ingresar un número válido")

recalculate = "n"

while recalculate == "y" or recalculate == "n":

    if recalculate == "n":

        num1 = ask_for_number("\nCuál es el primer número?: ")
    else:
        num1 = answer

    operation_symbol = input("+\n-\n*\n/\nElija una operación: ")

    if operation_symbol not in operations:
        print(f"Operación inválida, ingrese nuevamente: {num1} +,-,*,/ ?: ")
        continue

    num2 = ask_for_number("\nCuál es el segundo número?: ")


    if operation_symbol == "/" and num2 == 0:
        print("Dividir por 0 es una operación prohibida!")
        continue
    else:
        answer = operations[operation_symbol](num1, num2)
        print (f"{num1} {operation_symbol} {num2} = {answer}")

    recalculate = input(f"\nTipeá 'y' para continuar calculando con {answer} ,'n' para volver a comenzar, cualquier tecla para salir: ").lower()

    if recalculate != "y" and recalculate != "n":
        break
