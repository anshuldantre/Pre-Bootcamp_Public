class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self.account = BankAccount(interest_rate=0.02, balance=0, acc_type=acc_type)
        self.account = {'Checking': BankAccount(interest_rate=0.02, balance=0),
                        'Savings': BankAccount(interest_rate=0.02, balance=0)}

    def display_user_balance(self):
        # print(f'within user class, {self.name}')
        self.account.user_balance(self)
        return self

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def do_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self

    # def add_account(self, acc_type):
    #     if acc_type in self.account:
    #         print(f"Account type {acc_type} already exists for you")
    #     else:
    #         self.account[acc_type]=BankAccount(acc_type, interest_rate=0.02, balance=0)

class BankAccount:
    acc_dict = {}
    def __init__(self, acc_type, interest_rate, balance):
        self.acc_type = acc_type
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.acc_list.append(self)

    @staticmethod
    def withdrawal_allowed(balance,amount):
        return balance - amount > 0

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if BankAccount.withdrawal_allowed(self.balance, amount):
            self.balance -= amount
        else:
            print('Insufficient funds, deducting $5 as Penalty')
            self.balance -= 5
        return self

    def user_balance(self):
        for i in range(0,len(BankAccount.acc_list)):
            print(BankAccount.acc_list[i])

        # for i in range (0,len(instance_name.account)):
        #     print(instance_name.account.acc_type[i])
        # print(f'{instance_name.name}, {instance_name.account.acc_type} balance = {instance_name.account.balance}')

        # for name in BankAccount.acc_list:
        #     print((BankAccount.acc_list[name].acc_type))
        
        # for i in range(0,len(BankAccount.acc_list)):
        #     print((BankAccount.acc_list[i].acc_type))
        # print(f'{name}, {self.acc_type} balance = {self.balance}')
        # return self

# user1 = User('Anshul Dantre','anshul.dantre@codingdojo.com', 'savings')
# user2 = User('Robert Buckley','robert.buckley@codingdojo.com','savings')
# user1 = User('Anshul Dantre','anshul.dantre@codingdojo.com', 'checking')
# user4 = User('Robert Buckley','robert.buckley@codingdojo.com', 'checking')

user1 = User('Anshul Dantre','anshul.dantre@codingdojo.com')

# print(user1.account)
# user1.add_account('checking')
# user1.add_account('checking')
# print(user1.name)
# print(user1.account['checking'].balance)
# user1.add_account('savings')
# print(user1.account)

# user1.display_user_balance()
# print('----------------------------------------')
# user1.make_deposit(5).make_deposit(4).make_deposit(3).do_withdrawal(1).display_user_balance()
# user2.make_deposit(100).make_deposit(200).make_deposit(300).do_withdrawal(356).display_user_balance()
# user3.make_deposit(1500).make_deposit(2500).make_deposit(1500).display_user_balance()
# print('----------------------------------------')



# print('----------------------------------------')
# for i in range(0,len(BankAccount.acc_list)):
#     print((BankAccount.acc_list[i].balance))