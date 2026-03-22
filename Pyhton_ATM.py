balance = 10000

while True:   # infinite loop (menu runs again and again)
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Current Balance =", balance)
    
    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Amount Deposited Successfully")
    
    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        
        if amount > balance:
            print("Insufficient Balance ")
        else:
            balance = balance - amount
            print("Withdrawal Successful ")
    
    elif choice == 4:
        print("Thank you for using ATM ")
        break   # exit loop
    
    else:
        print("Invalid choice ")


# SAMPLE OUTPUT:
# --- ATM MENU ---
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
# Enter your choice: 1
# Current Balance = 10000
#
# Enter your choice: 3
# Enter amount to withdraw: 5000
# Withdrawal Successful 
#
# Enter your choice: 1
# Current Balance = 5000
#
# Enter your choice: 4
# Thank you for using ATM 
