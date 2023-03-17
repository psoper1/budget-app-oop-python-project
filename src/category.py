# Create a class called Category
class Category:
    def __init__(self, name):
        # Create attributes for the name and the ledger list
        self.name = name
        self.ledger = []

    def withdrawl(self, amount, description=""):
        # Is supposed to fail the withdrawl if the amount be withdrawn is more than what is available
        if self.check_funds(amount) == False:
            return False
        else:
            # I thought this was clever multiplying the amount by -1 to show it like it's being minued
            self.ledger.append({"amount": amount * -1, "description": description})
            return True

    def deposit(self, amount, description=""):
        # Add money to the ledger list
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        # Set the initial value of the balance to 0
        money_in_bank = 0
        # Loop to check the ledger and return an updated amount after any deposits / withdrawls
        for transaction in self.ledger:
            money_in_bank = money_in_bank + transaction["amount"]
        return money_in_bank

    def transfer(self, amount, group):
        # Checks and transfers money from one account to another, pretty limited for the moment
        if not self.withdrawl(amount, f"Transfer to {group.name}"):
            return False
        else:
            group.deposit(amount, f"Transfer from {self.name}")
            return True

    def check_funds(self, amount):
        # Checks how much money based on the updated balance
        if self.get_balance() < amount:
            return False
        else:
            return True

# Had to look up help for this part Don't quite understand how this is working, will need to research more on __str__ and how it and the syntax works

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items = items + f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'

            total = total + item['amount']

        output = title + items + "Total: " + str(total)
        return output