chances = 3
balance = 224.69
pin = 5757
userPin = int(input("Enter ATM PIN:"))
while(userPin != pin):
    userPin = int(input("Enter ATM PIN:"))
print("**WELCOME TO REBEL BANK ATM**")
print("Press 1 for BALANACE CHECK: ")
print("Press 2 for WIDTHROWAL: ")
print("Press 3 for DEPOSITE: ")
print("Press 4 for PIN CHANGE: ")
choices = int(input("Enter Choices: "))
while(choices != '0'):
    if(choices == 1):
        print("Current Balance: ", balance)
        print("**WELCOME TO REBEL BANK ATM**")
        print("Press 1 for BALANACE CHECK: ")
        print("Press 2 for WIDTHROWAL: ")
        print("Press 3 for DEPOSITE: ")
        print("Press 4 for PIN CHANGE: ")
        choices = int(input("Enter Choices: "))
    elif(choices == 2):
        if(balance >= 0):
            amount= int(input("Enter Widthrowal Amount: "))
            if(amount >= balance):
                print("Insufficient Balance")
            else:
                cAmount = balance - amount
                balance = cAmount
                print("You Widthrawl: ", amount)
                print("Current Balance: ", cAmount)
                print("**WELCOME TO REBEL BANK ATM**")
                print("Press 1 for BALANACE CHECK: ")
                print("Press 2 for WIDTHROWAL: ")
                print("Press 3 for DEPOSITE: ")
                print("Press 4 for PIN CHANGE: ")
                choices = int(input("Enter Choices: "))
    elif(choices == 3):
        dAmt = int(input("Enter Deposition Amount: "))
        dAmount = balance + dAmt
        balance = dAmount
        print("Current Amount: ", balance)
        print("**WELCOME TO REBEL BANK ATM**")
        print("Press 1 for BALANACE CHECK: ")
        print("Press 2 for WIDTHROWAL: ")
        print("Press 3 for DEPOSITE: ")
        print("Press 4 for PIN CHANGE: ")
        choices = int(input("Enter Choices: "))
    elif(choices == 4):
        cPin = int(input("Enter Current PIN: "))
        if(cPin == pin):
            nPin = int(input("Enter New PIN: "))
            pin = nPin
            print("Successfully Changed  PIN")
            print("**WELCOME TO REBEL BANK ATM**")
            print("Press 1 for BALANACE CHECK: ")
            print("Press 2 for WIDTHROWAL: ")
            print("Press 3 for DEPOSITE: ")
            print("Press 4 for PIN CHANGE: ")
            choices = int(input("Enter Choices: "))



