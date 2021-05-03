# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main

entertainment = budget.Category("Entertainment")
#print(food)
#print(clothing)
food = budget.Category("Food")
food.deposit(90, "deposit")
food.withdraw(10.67, "milk, cereal, eggs, bacon, bread")
#food.transfer(5656512.67, entertainment)
#print(food)
print( "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
create_spend_chart([food,entertainment])
#print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
#main(module='test_module', exit=False)