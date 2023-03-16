from category import Category
import time

groceries = Category('Groceries')
entertainment = Category('Entertainment')
python_tutorials = Category('Python Tutorials')

print("Welcome to Python Bank and Trust!")
time.sleep(2)

initial_deposit = input("Would you like to make a deposit? ").capitalize()

if initial_deposit == 'Yes':
    pass
else:
    time.sleep(1)
    print("Thank you for banking with us, have a nice day!")
    time.sleep(1)
    quit()

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

print(groceries)
print(python_tutorials)