def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except ValueError:
        return "Invalid input. Please enter numbers only."


while True:
    val = input("Enter an operation (add, subtract, multiply, divide): ")
    
    while (val != "add" and val != "subtract" and val != "multiply" and val != "divide"):
        print("Invalid operation. Please try again.")
        val = input("Enter an operation (add, subtract, multiply, divide): ")

    a = float(input("Enter your first number: "))
    b = float(input("Enter your second number: "))

    if(val == "add"):
        print(add(a,b))
    elif(val == "subtract"):
        print(subtract(a,b))
    elif(val == "multiply"):
        print(multiply(a,b))
    elif(val == "divide"):
        print(divide(a,b))
    
    again = input("Do you want to perform another operation? (yes/no): ")

    while(again != "yes" and again != "no"):
        again = input("Please enter a valid response (yes/no): ")
    
    if (again == "no"):
        break

print("Goodbye!")    

    




