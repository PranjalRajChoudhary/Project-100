class account(object):
    def __init__(self,card,pin):
        self.card = card
        self.pin = pin

    def cashWithdrawl(self):
        print("The cash has been withdrawn from the account")

    def cashDeposited(self):
        print("The cash has been deposited to the account")

    def BankBalanceInquiry(self):
        print("The current balance of the account is 20000 rupees")

Customer = account(10,20)
Customer.cashDeposited()
Customer.cashWithdrawl()
Customer.BankBalanceInquiry()