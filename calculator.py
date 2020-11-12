import os

#funciones
def add(x, y):
    resultado = (x + y)
    guardar_archivo(str(resultado))
    return resultado

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def potencial(x, y):
    return x ** y

def pregunta():
    input('Press ENTER to new operation')

def guardar_archivo(valor):
    fh = open("historial.txt", "a")
    fh.write(valor)
    fh.close

def menu():
    os.system('cls')
    print("Jorge's Calculator")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Potencial")

    choice = input("Let's calculate something today, shall we? Please choose one number 1,2,3,4,5!: ")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if choice == "1":
        print(num1, "+",num2,"=", add(num1,num2))
        pregunta()
        menu()
    elif choice == "2":
        print(num1, "-",num2,"=", substract(num1,num2))
        pregunta()
        menu()
    elif choice == "3":
        print(num1, "*",num2, "=", multiply(num1,num2))
        pregunta()
        menu()
    elif choice == "4":
        print(num1, "/",num2, "=", divide(num1,num2))
        pregunta()
        menu()
    elif choice == "5":
        print(num1, "**",num2, "=", potencial(num1,num2))
        pregunta()
        menu()
    else:
        print("Invalid Input")

#llama al funcion menu
menu()

input('Press ENTER to exit')
