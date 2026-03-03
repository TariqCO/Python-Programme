cart = []
total = []

def groceryFunc(var):
    if var == "rice":
        rate = 300
    elif var == "wheat flour":
        rate = 250
    elif var == "cooking oil":
        rate = 550
    elif var == "sugar":
        rate = 180
    elif var == "salt":
        rate = 50
    elif var == "tea":
        rate = 900
    elif var == "coffee":
        rate = 1200
    elif var == "spices":
        rate = 400
    elif var == "lentils":
        rate = 350
    elif var == "milk":
        rate = 200
    elif var == "eggs":
        rate = 300
    elif var == "butter":
        rate = 850
    elif var == "bread":
        rate = 120
    elif var == "biscuits":
        rate = 150
    elif var == "noodles":
        rate = 100
    else:
        rate = 0
    return rate

def electronicFunc(var):
    if var == "juicer machine":
        rate = 4500
    elif var == "iron":
        rate = 2500
    elif var == "washing machine":
        rate = 55000
    elif var == "blender":
        rate = 3500
    elif var == "air conditioner":
        rate = 120000
    elif var == "refrigerator":
        rate = 95000
    elif var == "microwave oven":
        rate = 30000
    elif var == "electric kettle":
        rate = 4000
    elif var == "vacuum cleaner":
        rate = 18000
    elif var == "water dispenser":
        rate = 25000
    elif var == "ceiling fan":
        rate = 7000
    elif var == "LED TV":
        rate = 85000
    elif var == "room heater":
        rate = 6000
    elif var == "dishwasher":
        rate = 110000
    elif var == "coffee maker":
        rate = 15000
    else:
        return None
    return rate

def fashionFunc(var):
    if var == "t shirt":
        rate = 1500
    elif var == "jeans":
        rate = 3500
    elif var == "jacket":
        rate = 6000
    elif var == "sneakers":
        rate = 8000
    elif var == "formal shoes":
        rate = 7000
    elif var == "watch":
        rate = 12000
    elif var == "handbag":
        rate = 5000
    elif var == "sunglasses":
        rate = 2500
    elif var == "belt":
        rate = 1500
    elif var == "cap":
        rate = 1200
    elif var == "wallet":
        rate = 2000
    elif var == "kurta":
        rate = 4000
    elif var == "abaya":
        rate = 6500
    elif var == "scarf":
        rate = 1800
    elif var == "socks":
        rate = 500
    else:
        rate = 0
    return rate

    
def receipt(cart, total):
    print("\nThank You for buying from lelo ecommerce store.")

    for i in range(0, len(cart)):
        print(f"{i+1}- {cart[i]} Rs.{total[i]}/-")
        
    print(f"\nTotal {len(cart)} items in your cart")
    print(f"Total Amount Rs.{sum(total)}/-")
    

def siteEngin (catName, items):
    while True:
        title = catName.capitalize()
        print(f"\n ==== {title} ==== \n")
        bucket = items
        
        for i in bucket:
            print(f"-{i}")

        var = input("\nPlease mention what you want to add to cart from above list. \nNote: Type exactly from the list: ").lower()
    
        if catName == "grocery":
            rate = groceryFunc(var)
        elif catName == "electronic":
            rate = electronicFunc(var)
        elif catName == "clothes":
            rate = fashionFunc(var)            
        else:
            print("Category not found")
            
        if var in bucket:
            print(f"\n{var} Rs. {rate} Added to cart")
            
            cart.append(var)
            total.append(rate)
            
            rerun = input(f"\nDo you want to continue buying {catName}? (yes/no)")

            if rerun == "yes":
                continue
            elif rerun == "no":
                break
            else:
                print("Invalid Input")
 
        else:
            print("-" * 45)
            print(f"{var} not found in the store. Check if there is a typing mistake!")
            print("-" * 45)

        
print("\n====== Welcome to lelo ecommerce store! ====== \n")

while True:
    select = int(input("Select Category:\n1. Grocery \n2. Electronic \n3. Clothes\n-->| "))

    if select == 1:
        groceries = [
        "rice",
        "wheat flour",
        "cooking oil",
        "sugar",
        "salt",
        "tea",
        "coffee",
        "spices",
        "lentils",
        "milk",
        "eggs",
        "butter",
        "bread",
        "biscuits",
        "noodles"]
        siteEngin("grocery", groceries)
           
    elif select == 2:
        electronics = [
        "juicer machine",
        "iron",
        "washing machine",
        "blender",
        "air conditioner",
        "refrigerator",
        "microwave oven",
        "electric kettle",
        "vacuum cleaner",
        "water dispenser",
        "ceiling fan",
        "LED TV",
        "room heater",
        "dishwasher",
        "coffee maker"]
        siteEngin("electronic", electronics)
        
    elif select == 3:
        fashion = [
        "t shirt",
        "jeans",
        "jacket",
        "sneakers",
        "formal shoes",
        "watch",
        "handbag",
        "sunglasses",
        "belt",
        "cap",
        "wallet",
        "kurta",
        "abaya",
        "scarf",
        "socks"]
        siteEngin("clothes", fashion)
    else:  
        print("Invalid Category selecton Input...")
        

    menu = input("\nDo you want to continue buying? \n1. Continue Buying \n2. Remove Item \n3. Exit \n-->| ")
    
    if menu == "1":
        continue
    elif menu == "2":
        print(f"\n==== Items in your cart =====\n")
        
        for i in cart:
            print(f"- {i}")

        itemName = input("\nEnter the item name to remove from your cart: ")
        itemIndex = cart.index(itemName)
        cart.remove(itemName)
        total.pop(itemIndex)

        print(f"\n==== Updated Cart ====\n")
 
    elif menu == "3":
        print("\n==== Exiting =====.")
    else:
        print("Invalid Input")



    #Ending ===================================================
    receipt(cart, total)    
    break
