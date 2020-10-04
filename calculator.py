#GraphicCalculator


# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def mult(x, y):
    return x * y

# This function divides two numbers
def devide(x, y):
    return x / y

print("Select Operation")
print("1-ADD")
print("2-SUBTRACTION")
print("3-MULTIPLY")
print("4-DIVIDE")

while True:
    # Take input from the user
    choice = input("Enter Choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = int(input("enter first number: "))
        num2 = int(input("enter second number: "))

    if(choice == '1'):
        print(num1, "+", num2, "=", add(num1, num2))

    elif (choice == '2'):
            print(num1, "-", num2, "=", subtract(num1, num2))

    elif (choice == '3'):
                print(num1, "*", num2, "=", mult(num1, num2))

    elif (choice == '4'):
        print(num1, "/", num2, "=", devide(num1, num2))
    break
else:
    print("Invalid Input")


