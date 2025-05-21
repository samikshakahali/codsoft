op = input("Enter an operator ( + - * / ):")
num1 = float(input("Enter the 1st number : "))
num2 = float(input("Enter the 2nd number : "))

if op == "+":
    result = num1 + num2
    print(result)

elif op == "-":
    result = num1 - num2
    print(result)

elif op == "*":
    result = num1 * num2
    print(result)

elif op == "/":
    result = num1 / num2
    print(result)

else :
    print(f"{op} is not a valid operator")
    
                   
                   
                   
