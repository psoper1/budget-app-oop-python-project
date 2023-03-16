class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def withdrawl(self, amount, description=""):
        if self.check_funds(amount) == False:
            return False
        else:
            self.ledger.append({"amount": amount * -1, "description": description})
            return True

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        money_in_bank = 0
        for transaction in self.ledger:
            money_in_bank = money_in_bank + transaction["amount"]
        return money_in_bank

    def transfer(self, amount, group):
        if not self.withdrawl(amount, f"Transfer to {group.name}"):
            return False
        else:
            group.deposit(amount, f"Transfer from {self.name}")
            return True

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items = items + f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'

            total = total + item['amount']

        output = title + items + "Total: " + str(total)
        return output