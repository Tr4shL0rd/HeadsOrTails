#!/usr/bin/env python3
import random
from termcolor import colored 
import time




choice = input("heads or tails? ")
headsbets = input("what is your bet for heads? ")
tailsbets = input("what is your bet for tails? ")
print()
print()
HoT = (["heads", "tails"])

cpu = random.choice(HoT)

if choice != cpu:
    print("the coin landed on {}".format(cpu))
    if cpu == "heads":
        print(headsbets)
    else:
        print(tailsbets)
else:
    print("the coin landed on {}".format(cpu))
    if cpu == "tails":
        print(tailsbets)
    else:
        print(headsbets)