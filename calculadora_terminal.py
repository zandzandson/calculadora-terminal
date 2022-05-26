#calculadora de terminal
#atm a calculadora aceita letras (e obviamente falha operação)

#as funções tão rodando com while-loops porque a ideia é filtrar letras
#usando algo como 'if "numX" contem letras': print("invalid answer"), else: numX = input

num1 = 0
num2 = 0
res = 0

print("welcome to the terminal calculator")
print("here, we have the finest text based operations")
print("no GUI tho :(")
print("")
print("anyway")

def defnum1():
    global num1
    print("whats the first number?")
    while True:
        numero1 = input()
        num1 = numero1
        print("")
        break

def defnum2():
    global num2
    print("whats the second number?")
    while True:
        numero2 = input()
        num2 = numero2
        print("")
        break

#def operation():
    #global oper

while True:
    defnum1()
    defnum2()
    print("what operation do you want to do?")
    print("1. addition                 2. subtraction")
    print("3. division                 4. multiplication")
    print("")
    while True:
        ans = input()
        if ans == "1":
            res = int(num1) + int(num2)
            print("Result: " + str(res))
            print("")
            break
        if ans == "2":
            res = int(num1) - int(num2)
            print("Result: " + str(res))
            print("")
            break
        if ans == "3":
            res = int(num1) / int(num2)
            print("Result: " + str(res))
            print("")
            break
        if ans == "4":
            res = int(num1) * int(num2)
            print("Result: " + str(res))
            print("")
            break
        else:
            print("choose a valid operation")