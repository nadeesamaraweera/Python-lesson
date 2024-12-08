# Write a python program to define ansd use a car representing the bank account.

#   * create the class name "BankAccount" with the following
#          1.an attribute "account_holder" to store the name of the account_holder.
#          2.an attribute "balance" to store the account balance initilize to zero.

#   * add the following methods to the class
#           deposite(amount)
#           withdraw(amount) =subscibe the given amount from the balance if sufficense an exit.
#           display(balance)= print the current balance.

#   * write the small script to demostarte to following  create an object of the bank account class.
#                 perform the  few widraw and 
#                 display the balance after each opertaions.



class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if amount < 0:
            print("Amount must be positive.")

        elif amount > self.balance:
            print("Insufficient balance to complete the withdrawal.")

        else :
            self.balance -= amount
          

account = BankAccount("Nadeesha")
account.display()

account.deposit(1000) 
account.display()

account.withdraw(300)  
account.display()


account.withdraw(800)  
account.display()

account.deposit(500)  
account.display()
