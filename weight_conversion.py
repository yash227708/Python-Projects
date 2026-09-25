weight = float(input("Enter your body weight: "))
unit = input("kilograms or pound? (K or L): ")

if unit == "K":
    weight = weight*2.205
    unit = "lbs."
    print(f"your weight is {round(weight, 2)} {unit}")

elif unit == "L":
    weight = weight/2.205
    unit = "kgs."
    print(f"your weight is {round(weight, 2)} {unit}")

else:
    print(f"{unit} is invalid unit")