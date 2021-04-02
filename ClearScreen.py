#!/usr/bin/env python3
# ^ After creating a file, click w and copy this in before you get into the file
# Test2.py
# ClearScreen.py
## NEED TO CHANGE THE TERM variable
# This happens: TERM environment variable not set.

import os
from time import sleep;

def clear():
    os.system("clear")

for i in range(2):
    clear()
    print("HELLLLLLOOOOOOOOOO\n"*5)

