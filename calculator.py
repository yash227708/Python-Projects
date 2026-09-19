number1 = float(input("enter first number:"))
operator = (input("enter the operation you want perform:"))
number2 = float(input("enter second number:"))

if operator == "*" :
    print(number1*number2)

elif operator == "/" :
    print(f"{number1/number2: .4f}")

elif operator == "+" :
    print(number1+number2)

elif operator == "-" :
    print(number1-number2)

else:
    print("invalid input entered")