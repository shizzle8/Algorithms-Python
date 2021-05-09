# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from prob_calculator import experiment
from unittest import main

hat= prob_calculator.Hat(yellow=5,red=1,green=3,blue=9,test=1)


#print(hat.draw(2))
#print(hat.contents)

lol = {"red": 6, "green":3}

print(experiment(hat, {"yellow":2,"blue":3,"test":1},20,100 ))




# Run unit tests automatically
main(module='test_module', exit=False)
