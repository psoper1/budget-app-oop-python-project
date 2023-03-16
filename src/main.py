from category import Category

groceries = Category('Groceries')
entertainment = Category('Entertainment')
python_tutorials = Category('Python Tutorials')

groceries.deposit(500, "First Deposit")
# print(groceries.get_balance())
groceries.withdrawl(100, "Got groceries")
# print(groceries.get_balance())
groceries.transfer(50, python_tutorials)
# print(python_tutorials.get_balance())
python_tutorials.withdrawl(45)
entertainment.deposit(150, "Second Deposit")
entertainment.withdrawl(75)

print(groceries)
print(python_tutorials)