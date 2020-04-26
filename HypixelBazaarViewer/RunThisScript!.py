import sys
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

i = 0
while i < 10:

    print("Do you want to see the prices of every produkt, or one specific product?")
    answer = input("Enter 'all' or 'specific': ")
    if answer == "all":
        print("ok, you get the prices of every product:")
        import EveryProdukt
        # Do this.
    elif answer == "specific":
        # Do that.
        print("ok, you will get the price of a specific product:")
        import SpecificProduct
    else:
        print("Enter 'all' or 'specific': ")


