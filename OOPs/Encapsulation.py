# What is Encapsulation?
# Encapsulation means hiding internal data and only exposing what's necessary. It protects the object’s internal state and restricts direct access.


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance   # Private variable using double underscore
        
#     def deposite(self, amount):
#         if amount > 0:
#             self.__balance += amount
    
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient Balance !!!")

#     def get_balance(self):
#         return self.__balance
    

# acc = BankAccount("alice", 1000)
# acc.deposite(5000)
# print(acc.owner)
# print(acc.get_balance())
# acc.withdraw(30000)
# print(acc.get_balance())

# print("wait: ",acc._BankAccount__balance)
# # print(acc.__balance)