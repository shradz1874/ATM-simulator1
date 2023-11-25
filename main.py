import time

class ATM:
    def __init__(self, balance, pin):
        self.balance = 2000
        self.pin = 1234

    def check_balance(self):
        y=int(input("Enter your pin: "))
        if y== 1234:
            print("Your account balance is: " , self.balance )
        else:
            print(f"invalid pin")



    def deposit(self):
        y = int(input("Enter your pin: "))
        if y == 1234:
            amount = int(input("Enter your amount: "))
            self.balance += amount
            print(f"Deposit successful. Your new balance is: {self.balance}")

        else:
             print("invalid pin")




    def withdraw(self):
        y = int(input("Enter your pin: "))
        if y == 1234:
            amount = int(input("Enter your amount: "))
            if amount > self.balance:
                print("Insufficient balance")

            else:
                 self.balance -= amount
                 print(f"Withdrawal successful. Your new balance is: {self.balance}")
        else:
            print(f"invalid pin")



def main():
    atm = ATM(balance= 0000, pin= 1234)

    while True:
        print("Welcome to the ATM!")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            atm.check_balance()
        elif choice == 2:
            atm.deposit()
        elif choice == 3:
            atm.withdraw()
        elif choice == 4:
            break

        time.sleep(2)

if __name__ == "__main__":
    main()