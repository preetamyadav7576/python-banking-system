balance = 0
doc = { }

def check_balance() :
    print(f"Your current balance is {balance}")
    print("=========================")

def deposit() :
    deposit_money = float(input("Enter your deposit amount : "))
    print("=========================")
    global balance
    if deposit_money > 0:
      balance += deposit_money
      print("Deposited Successfully !! ")
      print("======================")
    else :
        print("You can't deposit negative money")
        print("==============================")

def withdraw() :
    withdraw_money = float(input("Enter your withdraw amount : "))
    print("=========================")
    global balance
    if withdraw_money > balance :
        print("Insufficient Money")
        print("========================")
    else :
        balance -= withdraw_money
        print("Withdraw Successfully !! ")
        print("=====================")

def check_kyc() :
    if len(doc) == 0 :
        print("Incomplete Document")
        print("=====================")
    else :
        print(f"KYC Completed and document submitted for kyc are : {doc}")
        print("======================================================")

def update_kyc() :
    global doc
    key = input ( " Enter the Document name : ")
    value = input ( " Enter the Document number : ")
    doc[key] = value

    print(" KYC Completed")
    print("===================")



print("=========================")
print("Welcome to the Banking App")
print("=========================")


while True :
    print("1 : Check your balance")
    print("2 : Deposit Money")
    print("3 : Withdraw Money")
    print("4 : Check KYC")
    print("5 : Update KYC")
    print("6 : Exit")

    print("=========================")
    choice = float(input("Enter you choice (1-4) : "))
    print("=========================")
    if choice == 1 :
        check_balance()
    elif choice ==2 :
        deposit()
    elif choice == 3 :
        withdraw()
    elif choice == 4:
        check_kyc()
    elif choice == 5:
        update_kyc()
    elif choice == 6 :
        break
    else :
        print("Invalid choice !! Try again. ")
        break

print("Thank you for using Banking App")
