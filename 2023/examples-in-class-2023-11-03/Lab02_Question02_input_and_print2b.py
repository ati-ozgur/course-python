unit = input("Which unit you want to convert, C or F:")
str_value = input("enter the value of temperature:")
value = float(str_value)
if unit == "F":
    F = value
    C = (F - 32) * 5/9
    print(f"{F} Fahrenheit equals to {C} Celsius")
if unit == "C":
    C = value
    F = (C * 9/5) + 32
    print(f"{C} Celsius equals to {F} Fahrenheit")


