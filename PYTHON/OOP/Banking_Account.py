class Account():
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} made. New balance is {self.balance}")
            pass
        else:
            print("Invalid deposit amount")
            pass
            
    def withdraw(self,ammount):
        if ammount <= self.balance:
            self.balance -= ammount
            print(f"Withdrawal of {ammount} made. New balance is {self.balance}")
            pass
        else:
            print("Insufficient funds")
            pass
    def check_balance(self,ammount):
        self.balance = ammount
        print(f"Your Balance is:{ammount}")
        

            
#main logic

owner = input("Enter your name: ")
ammount =0 
acc = Account(owner)
flag = 1 

while flag == 1 :
    choice= input("Choose what you want to do ? 'D' for deposite 'W' for Withdrawal 'C' for checking the balance, Or if you want to exit then press 'N' : \n")
    choice= choice.upper()
    if choice == 'N':
        flag = 0
        break
    else:
        pass
    
    while choice== 'D' or choice == 'W' or choice == 'C':
        if choice == 'D':
            ammount = float(input("Enter the amount to deposit: "))
            acc.deposit(ammount)
            break
        elif choice == 'W':
            ammount = float(input("Enter the amount to withdraw: "))
            acc.withdraw(ammount)
            break
        elif choice == 'C' :
            acc.check_balance(ammount)
            break
        else:
            print("Invalid choice. Please choose 'D' for deposit or 'W' for withdrawal")
            
print("Thanks for using....")

        