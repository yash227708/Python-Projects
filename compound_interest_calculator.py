principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter your principal amount: "))
    if principal <= 0:
        print("Principal can't be less than or equal to zero!")

while rate <= 0:
    rate = float(input("Enter your rate of interest: "))
    if rate <= 0:
        print("rate of interest can't be less than or equal to zero!")

while time <= 0:
    time = int(input("Enter your time in years: "))
    if time <= 0:
        print("time can't be less than or equal to zero!")

total = principal * pow((1 + rate/100), time)
print(f"your balance after {time} year/s: ₹{total: .2f}")