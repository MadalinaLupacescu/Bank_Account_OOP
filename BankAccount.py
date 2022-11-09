class BankAccount:
    def __init__(self, nr_cont, name, balance):
        self.nr_cont = nr_cont
        self.name = name
        self.balance = balance

    def __str__(self):
        return "The bank account - " + str(self.nr_cont) + "\nPerson - " + self.name + "\nAccount balance - " + str(self.balance) + " euro"

    
    def balance_view(self):
        return "Account balance - " + str(self.balance) + " euro"

    def emit_cash(self, amount_withdrawn):
        if self.balance > amount_withdrawn:
            self.balance -= amount_withdrawn
            return "You extracted - " + str(amount_withdrawn)
        else:
            return "Error. You don't have enough money in your bank account"

    def loadtheaccount(self, entered_amount):
        if entered_amount >0:
            self.balance += entered_amount
            return "After entering the money, your bank account is - " + str(self.balance)
        else:
            return "Error. The amount of 0 euros cannot be processed"

    def bank_taxes(self, percent):
        amount_in_percentage = (self.balance * percent) / 100
        self.balance -= amount_in_percentage
        return "The bank took - " + str(amount_in_percentage) +"\n" +\
               "Balance - " + str(self.balance)
    

def bank_transfer(sender_account, receiver_account, money):
    if sender_account.balance > money:
        sender_account.balance = sender_account.balance - money
        receiver_account.balance = receiver_account.balance + money
        return "Sender account - "+ str(sender_account.balance) + "\nReceiver account - " + str(receiver_account.balance)
    else:
        return "Error. The amount exceeds the possible limit of the account"

        

my_obj = BankAccount(1234567891011, "Madalina Lupacescu", 10050.45)
print("----------")
print(my_obj)

print("----------")
print(my_obj.balance_view())

print("----------")
print(my_obj.emit_cash(500))

print("----------")
print(my_obj.balance_view())

print("----------")
print(my_obj.loadtheaccount(20000))

print("----------")
print(my_obj.bank_taxes(5))


obj1 = BankAccount(1245854215421, "Alexandru", 15000)
obj2 = BankAccount(2464631134494, "Maxim", 10000)

print("----------")
print(bank_transfer(obj1, obj2, 5040))