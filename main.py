varA=int(input("Enter first number: "))20
sign=input("Enter sign: ")
varB=int(input("Enter second number: "))    
if sign == "+":
    print(f"{varA} + {varB} = {varA + varB}")   
elif sign == "-":
    print(f"{varA} - {varB} = {varA - varB}")
elif sign == "*":
    print(f"{varA} * {varB} = {varA * varB}")
elif sign == "/":
    if varB == 0:
        print("Cannot divide by zero")
    else:
        print(f"{varA} / {varB} = {varA / varB}")   
elif sign == "%":
    if varB == 0:
        print("Cannot divide by zero")
    else:
        print(f"{varA} % {varB} = {varA % varB}")
elif sign == "**":
    print(f"{varA} ** {varB} = {varA ** varB}")
