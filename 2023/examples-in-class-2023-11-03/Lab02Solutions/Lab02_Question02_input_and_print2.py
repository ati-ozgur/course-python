unit = input("Which unit you want to convert, C or F:")
if unit.upper() == "F":
    value = input("Value of Fahrenheit:")
    F = float(value)
    C = (F - 32) * 5/9
    print(f"{F} Fahrenheit equals to {C} Celsius")
if unit.upper() == "C":
    value = input("Value of Celcius:")
    C = float(value)
    F = (C * 9/5) + 32
    print(f"{C} Celsius equals to {F} Fahrenheit")


