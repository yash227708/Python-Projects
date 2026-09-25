a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and c>a):
        return b
    else:
        return c

print("the greatest number is: ", greatest(a, b, c))