# Import the category class and any other methods I may need

from category import Category
import time

# Hardcode some initial values
groceries = Category('Groceries')
entertainment = Category('Entertainment')
python_tutorials = Category('Python Tutorials')

# Prints the opening since this is semi user driven
print("Welcome to Python Bank and Trust!")
time.sleep(2)

# Generic true or false to start the process
initial_deposit = input("Would you like to make a deposit? ").capitalize()

if initial_deposit == 'Yes':
    pass
else:
    time.sleep(1)
    print("Thank you for banking with us, have a nice day!")
    time.sleep(1)
    quit()

# Questions that take the user through depositing and moving money and withdrawing money
# Mostly hardcoded but is a semi-trick...

groceries.deposit(int(input("How much would you like to deposit for Groceries? ")), "First Deposit")
time.sleep(1)
# print(groceries.get_balance())
groceries.withdrawl(int(input("How much would you like to take out for Groceries? ")), "Got groceries")
time.sleep(1)
# print(groceries.get_balance())
groceries.transfer(int(input("How much would you like to transfer to your Python Tutorials fund? ")), python_tutorials)
time.sleep(1)
# print(python_tutorials.get_balance())
python_tutorials.withdrawl(int(input("How much would you like to take out from your Python Tutorials fund? ")))
time.sleep(1)
entertainment.deposit(int(input("How much would you like to deposit for Entertainment?? ")), "Second Deposit")
time.sleep(1)
entertainment.withdrawl(int(input("How much would you like to take out from your Entertainment fund? ")))
time.sleep(1)

# Prints a couple of the categories to show on the receipt

print(groceries)
print(python_tutorials)