print("""******************************
Welcome To The 'Banking System'

""")

class BankAccount(object):
    def __init__(self, name, accno, balance):
        self.name = name
        self.acccno = accno
        self.balance = balance

    def balanceCheck(self, f1):
        print(f'Balance is : {self.balance}')
        data = self.balance
        f1.write("\nAccount # is : " + str(self.acccno))
        f1.write("\nUser Name is : " + self.name)
        f1.write("\nBalance is : " + str(data) + "\n")

    def withdraw(self, am, f1):
        if am <= self.balance:
            self.balance -= am
            f1.write("\n" + str(am) + " is DEBITED")
            f1.write("\nBalance After Withdraw: "+ str(self.balance))
            print(f"Balance After Withdraw: {self.balance}")
        else:
            print("Insufficient balance!")
            print("______________________")
            f1.write("\nAttempted to withdraw " + str(am) + " but insufficient balance.")
            f1.write("\n_______________________________________________________________")
    def deposit(self, am, f1):
        self.balance += am
        f1.write("\n" + str(am) + " is CREDITED")
        f1.write("\nBalance After Deposit: "+ str(self.balance))
        print(f"Balance After Deposit: {self.balance}")

class savingAcc(BankAccount):
    def addInterest(self):
        interest = self.balance / 50
        print(f"Interest on your Amount is : {interest}")
        self.balance += interest


# MAIN _ WORK
char = ""
while char.lower() != "q":
    print("Press 'S' to *START* || Press 'Q' to Quit   \n>ENTER: ")
    char = input().lower()

    if char == 's':
        n = input("Enter your name: ")
        a = int(input("Enter Your Account #: "))
        b = int(input("Enter Your Initial Balance: "))
        s = savingAcc(n, a, b)

        with open("bankDetails.txt", "a") as f1:
            s.balanceCheck(f1)
            
            while True:
                print("\nDo you want to Deposit or Withdraw?")
                print("Enter 'd' for Deposit or 'w' for Withdraw (or 'q' to quit): ")
                action = input().lower()

                if action == 'd':
                    amount = int(input("Enter amount to deposit: "))
                    s.deposit(amount, f1)
                elif action == 'w':
                    amount = int(input("Enter amount to withdraw: "))
                    s.withdraw(amount, f1)
                elif action == 'q':
                    print("Exiting the transaction menu...")
                    break
                else:
                    print("Invalid input! Please enter 'd' for deposit, 'w' for withdraw, or 'q' to quit.")

         
            s.balanceCheck(f1)

    elif char == 'q':
        print("Exiting the system...")
    else:
        print("Invalid input. Please enter 'S' to start or 'Q' to quit.")

