import sys
import os


sys.path.insert(1, 'ScriptsAndData')

print("FLIMMERS BAZAAR VIEWER!")
print("FLIMMERS BAZAAR VIEWER!")
print("FLIMMERS BAZAAR VIEWER!")
print("FLIMMERS BAZAAR VIEWER!")
print("FLIMMERS BAZAAR VIEWER!")
print("FLIMMERS BAZAAR VIEWER!")
print("FLIMMERS BAZAAR VIEWER!")

print("If the product you want to see doesnt exist, it spits out an KeyError.")
print()
i = 0
while i < 10:

    print("Do you want to see the best product to flip, or the price of one single product? Or do you want to quit?")
    print()
    print("Or do you want to see the item with the highest quickbuy and quicksell differnce on the Bazaar?")
    
    answer = input("Enter 'best margin', 'single product', 'highest difference' or 'quit': ")
    
    answer = answer.lower()
    
    if answer == "best margin":
        print("ok, you will get the product with the best profit margin:")
        import EveryProduct
        os.system("EveryProduct.py")

    elif answer == "single product":
        print("ok, you will get the price of a single product:")
        import SpecificProduct
        os.system("SpecificProduct.py")

    elif answer == "highest difference":
        print("ok, you will get the products with the highest price difference:")
        import HighestPriceDifference
        os.system("HighestPriceDifference.py")

    elif answer == "quit":
        print("ok, quitting the programm")
        break
        sys.exit
    else:
        print("Enter 'best margin', 'single product' or 'quit': ")
