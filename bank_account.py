# class BankAccount:
#     bank_name = "Big Time Bank"
#     all_accounts =[]

#     def __init__(self, int_rate, balance): 
#         self.balance = balance
#         self.int_rate = int_rate
#         BankAccount.all_accounts.append(self)

#     @classmethod
#     def all_balances(cls):
#         sum = 0
#         for account in cls.all_accounts:
#             sum += account.balance
#         return sum
    
#     @classmethod
#     def display_all(cls):
#         for index in range(len(cls.all_accounts)):
#             cls.all_accounts[index].display_account_info()
    
#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         return self
    
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds: Charging a $5 fee")
#             self.balance = self.balance - 5
#         else:
#             self.balance = self.balance - amount
#         return self
    
#     def display_account_info(self):
#         print(f"Balance: {self.balance}")
#         print(f"Interest: {self.int_rate}")
#         return self
    
#     def yield_interest(self):
#         interest = self.balance * self.int_rate
#         self.balance = self.balance + interest
#         return self

# account_0 = BankAccount (.01, 0)
# account_1 = BankAccount (.02, 100)

# account_0.deposit(50).deposit(125).deposit(75).withdraw(20).yield_interest().display_account_info()
# account_1.deposit(1000).deposit(50).withdraw(100).withdraw(50).withdraw(500).withdraw(20).yield_interest().display_account_info()
# print(BankAccount.all_balances())
# BankAccount.display_all()

# Write an algorithm that takes an array and moves all of the zeros to the end, 
# preserving the order of the other elements.
# returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)
    return arr

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
print(move_zeros([5, 0, 5, 5, 0, 5, 5]))