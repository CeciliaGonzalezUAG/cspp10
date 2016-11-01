bank_account = 10000
print("1. Withdraw \n2. Deposit \n3. Exit")
choice = input("Welcome to ATM! Pick from above [1|2|3]:")
while choice != 3: #student completes while loop
    if choice == "1": #user chooses 'withdraw'
        withdraw =int(input("Amount to withdraw: "))
        bank_account = bank_account - withdraw
        print("You now have" + " "+str(bank_account) + " in your bank account")
    elif choice == "2":
        amount = int(input("How much to deposit: "))
        bank_account = bank_account + amount
        print ("You now have " + str(bank_account) + " in your account")
    elif choice == "3": #user chooses 'exit'

        print ("1. Withdraw \n2. Deposit \n3. Exit")
    choice = input("Pick from above [1|2|3]:")