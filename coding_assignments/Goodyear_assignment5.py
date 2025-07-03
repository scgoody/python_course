# addition func
def add(x, y):
    return x+y

# subtraction func
def subtract(x, y):
    return x-y

# multiplication func
def multiply(x, y):
    return x * y

# division func
def divide(x, y):
    if y == 0:
        return "Error: division by zero"
    else:
        return x / y


# Display a menu of options to the user
while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
   

    # Prompt the user for their choice
    choice = input("Choose an option (1-5): ")

    if choice in ["1","2","3","4"]:
        try:
           # get numbers for operations
            n1 = float(input("Enter the first number: "))
            n2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input: only numeric values allowed. ")
            continue
            

    # Implement the logic for each choice
    if choice == "1":
        # Addition
       output = add(n1,n2)
       print(f"The result of {n1} + {n2} is: {output}")
    elif choice == "2":
        # Subtraction
       output = subtract(n1,n2)
       print(f"The result of {n1} - {n2} is: {output}")
    elif choice == "3":
        # Multiplication
        output = multiply(n1,n2)
        print(f"The result of {n1} * {n2} is: {output}")
    elif choice == "4":
        # Division
        output = divide(n1,n2)
        print(f"The result of {n1} / {n2} is: {output}")
    elif choice == "5":
        # Exit the system
        print("Thank you for using the Simple Calculator!")
        break
    else:
        print("Invalid choice. Please try again.")
