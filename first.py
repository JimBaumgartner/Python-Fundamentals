"""
Calculator:
    the ability to add, subtract , divide, multiply
    and will be a command line app
"""

from calc import calculate


calculate()
while True:
    print(
        """
Calc Menu:
1. Run Operation
2. Quit
        """
    )
    choice = input("> ")
    if choice == "1":
        pass
    if choice == "2":
            exit()
    exit()
