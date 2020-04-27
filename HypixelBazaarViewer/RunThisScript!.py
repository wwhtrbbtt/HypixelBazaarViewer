import sys
import os


sys.path.insert(1, 'ScriptsAndData')
print("""  ______ _      _____ __  __ __  __ ______ _____   _____
 |  ____| |    |_   _|  \/  |  \/  |  ____|  __ \ / ____|
 | |__  | |      | | | \  / | \  / | |__  | |__) | (___
 |  __| | |      | | | |\/| | |\/| |  __| |  _  / \___ \
 | |    | |____ _| |_| |  | | |  | | |____| | \ \ ____) |
 |_|__  |______|_____|_|  |_|_|  |_|______|_|__\_\_____/
 |  _ \   /\    |___  /   /\        /\   |  __ \
 | |_) | /  \      / /   /  \      /  \  | |__) |
 |  _ < / /\ \    / /   / /\ \    / /\ \ |  _  /
 | |_) / ____ \  / /__ / ____ \  / ____ \| | \ \
 |____/_/____\_\/_____/_/    \_\/_/____\_\_|__\_\
 \ \    / /_   _|  ____\ \        / /  ____|  __ \
  \ \  / /  | | | |__   \ \  /\  / /| |__  | |__) |
   \ \/ /   | | |  __|   \ \/  \/ / |  __| |  _  /
    \  /   _| |_| |____   \  /\  /  | |____| | \ \
  ___\/  _|_____|______|   \/  \/   |______|_|  \_\
 |___ \ / _ \ / _ \/_ |
   __) | | | | | | || |
  |__ <| | | | | | || |
  ___) | |_| | |_| || |
 |____/ \___/ \___/ |_|

                               """)
print("If the product you want to see doesnt exist, it spits out an KeyError.")

i = 0
while i < 10:

    print("Do you want to see the prices of every produkt, or one single product? Or do you want to quit?")
    answer = input("Enter 'best margin', 'single product' or 'quit': ")
    answer = answer.lower()
    if answer == "best margin":
        print("ok, you will get the product with the best profit margin:")
        import EveryProduct
        os.system("EveryProduct.py")

    elif answer == "single product":
        print("ok, you will get the price of a single product:")
        import SpecificProduct
        os.system("SpecificProduct.py")

    elif answer == "quit":
        print("ok, quitting the programm")
        break
        sys.exit
    else:
        print("Enter 'best margin', 'single product' or 'quit': ")
