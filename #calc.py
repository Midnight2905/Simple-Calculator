#simple calculator app Python
num1 = input("Enter numbver 1: ")
num2 = input("Enter numbver 2: ")
calcFunc = input("What would you like to do? (+, -, *, /)")
#calculate and print
if(str(calcFunc) == "+"):
    print(int(num1) + int(num2))
if(str(calcFunc) == "-"):
    print(int(num1) - int(num2))
if(str(calcFunc) == "*"):
    print(int(num1) * int(num2))
if(str(calcFunc) == "/"):
    print(int(num1) / int(num2))