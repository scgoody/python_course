#Student Starter code
#Student Name: Sarah Goodyear
#Date: 3/4/2025
#Assignment Title: A simple banking system

# Initialize balance and transaction history
balance = 0
transaction_history = []

# Display a menu of options to the user
while True:
    print("\nSimple Banking System")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. View Transaction History")
    print("5. Exit")
    
    # Prompt the user for their choice
    choice = input("Choose an option (1-5): ")
    
    # Implement the logic for each choice
    if choice == "1":
        # Deposit money
        try:
            amount = float(input("Enter the amount to deposit: $"))
            if amount > 0:
                balance += amount
                transaction_history.append(f"Deposited: ${amount}")
                print(f"Deposited: ${amount}")
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        pass
    elif choice == "2":
        # Withdraw money
        try:
            amount = float(input("Enter the amount to withdraw: $"))
            if amount > 0 and amount <= balance:
                balance -= amount
                transaction_history.append(f"Withdrew: ${amount}")
                print(f"Withdrew: ${amount}")
            elif amount > balance:
                print("Insufficient funds.")
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        pass
    elif choice == "3":
        # Check balance
        print(f"Your current balance is: ${balance}")
        pass
    elif choice == "4":
        # View transaction history
        if transaction_history:
            print("Transaction History:")
            for transaction in transaction_history:
                print(transaction)
        else:
            print("No transactions have been made yet.")
        pass
    elif choice == "5":
        # Exit the system
        print("Thank you for using the Simple Banking System!")
        break
    else:
        print("Invalid choice. Please try again.")
