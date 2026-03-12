
stock=["pulses","spices","dairy","rice","wheat","computer","mobile_phone","led","graphic_card","charger","mango","potato","apple","spinach","tomato","green_chilli","grapes","onion","pents","shirt","belt","trouser","hoodie","jackets","muffler","panadol","brufen","bascopan","relief","surbex_z","risek"]
inventoryList=[]
cart=[] 
total=[]


def rate_option(var):
    if var=="pulses":
        rate=500
    elif var=="spices":
        rate=150
    elif var=="dairy":
        rate=300
    elif var=="rice":
        rate=4000
    elif var=="wheat":
        rate=3000
    elif var=="computer":
        rate=20000
    elif var=="mobile_phone":
        rate=50000
    elif var=="led":
        rate=60000
    elif var=="graphic_card":
        rate=50000
    elif var=="charger":
        rate=1200
    elif var=="mango":
        rate=200
    elif var=="potato":
        rate=100
    elif var=="apple":
        rate=180
    elif var=="spinach":
        rate=250
    elif var=="tomato":
        rate=150
    elif var=="green_chilli":
        rate=100
    elif var=="grapes":
        rate=400
    elif var=="onion":
        rate=120
    elif var=="pents":
        rate=4000
    elif var=="shirt":
        rate=3000
    elif var=="belt":
        rate=500
    elif var=="hoodie":
        rate=3000
    elif var=="jackets":
        rate=5000
    elif var=="muffler":
        rate=1500
    elif var=="panadol":
        rate=45
    elif var=="brufen":
        rate=40
    elif var=="bascopan":
        rate=30
    elif var=="relief":
        rate=100
    elif var=="surbex_z":
        rate=700
    elif var=="risek":
        rate=300
    else:
        print("invalid value, please check your outer program!")
        rate=0
    return rate
   
def calc_total(cart,total):
    print(f"Your Total cart is:")
    for i in range(0, len(cart)):
        print(f" {i+1}-{cart[i]}  | Rs.{total[i]}")
    print(f"Your Total items are {len(cart)} and Rs.{sum(total)}/ ")

def modify(cart,total):
        rem=input(f" Which item for a cart your want to remove? {cart} | please mention the product exactly:")
        item_index=cart.index(rem)
        cart.remove(rem)
        print(rem, "removed from the cart.")

def bucket(cat):
    if cat=="1":
        bucket=["pulses","spices","dairy","rice","wheat"]
    elif cat=="2":
        bucket=["computer","mobile_phone","led","graphic_card","charger"]
    elif cat=="3":
        bucket=["mango","potato","apple","spinach","tomato","green_chilli","grapes","onion"]
    elif cat=="4":
        bucket=["pents","shirt","belt","trouser","hoodie","jackets","muffler"]
    elif cat=="5":
        bucket=["panadol","brufen","bascopan","relief","surbex_z","risek"]
    else:
        print("Invalid input!")
    return bucket

def engine(select,category):
        while True:
            print(f"Welcome to {category} section")
            for i in bucket(select):
                print(f"{bucket(select).index(i)+1}:{i} : {stock.count(i)}")
            var=input("Please mention what your want to buy from above list?").lower()
            if var in stock:
               
                rates=rate_option(var)
                if var in bucket(select):
                    cart.append(var)
                    total.append(rates)
                    print("=" * 60)
                    print(f"bought item {var}, Rs.{rates}, Your Total Items are {cart} and total amount is {sum(total)}")
                    print("=" * 60)
                    rerun=input(f"Do you want to add more from {category}? (yes or no): ").lower()
                    if rerun=="yes":
                        continue
                    else:
                        print("=" * 60)
                        print(f"Ok Thank you for shopping {category}!")
                        break
                else:
                    print("=" * 60)
                    print("item not found in the bucket, Please select from below")
                    continue
            else:
                print(f"This {var} is not in stock!")
                continue



def invent():
    while True:
        default = ["pulses","spices","dairy","rice","wheat","computer","mobile_phone","led","graphic_card","charger","mango","potato","apple","spinach","tomato","green_chilli","grapes","onion","pents","shirt","belt","trouser","hoodie","jackets","muffler","panadol","brufen","bascopan","relief","surbex_z","risek"]
        for i in default:
            print(f"{i}: stock --> {stock.count(i)}")
        print("Add inventory first")
        product=input("Enter a product you want to insert into inventory: ")
        num=int(input(f"How much you want to add {product} into inventory? specify number:"))
        if num>1:
            for i in range(num):
                stock.append(product)
            inventoryList.append(product)
            for i in inventoryList:
                print(f"{i} : Total Count={stock.count(i)}")
                
            rerun=input("Do you want add more product?:").lower()
            if rerun=="yes":
                continue
            else:
                break
        else:
            print("Invalid value! Please add a value of above 1")
            continue



def user():
    while True:
        select=input("Which category you want to buy? \n1.grocery \n2.electronic \n3.fruit and veg \n4.Clothing: \n5.Pharmacy")
        print("=" * 60)
        if select=="1":
            engine(select,"Grocery")
        elif select=="2":
            engine(select,"Electronics")
        elif select=="3":
            engine(select,"Fruit and Vegetable")
        elif select=="4":
            engine(select,"Clothing")
        elif select=="5":
            engine(select,"Pharmacy")
        else:
            print("invalid input!")
            rerun=input("Do you want try again? (yes or no):").lower()
            if rerun=="yes":
                continue
            else:
                print("Thank you! Bye!")
                break
                
        rerun=input("Do you want to add more from store? \n(yes) for Continue to store \n(no) for exiting for the total bill \n(mod) for modifying your cart!: \n:").lower()
        if rerun=="yes":
            continue
        elif rerun=="mod":
            modify(cart,total)
        else:
            print("Thank you for Shopping!")
    
            
        calc_total(cart,total)
        break


def start():
    role = input("Enter your role. (1.Admin, 2.User): ").lower()
    userName = input("Enter your username: ")

    if role == "1" or role == "admin" and userName == "tariq001":
        print(f"Welcome {userName}, to the admin panel")
        invent()
    elif role == "2" or role == "user":
        print(f"Welcome {userName}, to ecomerce store!")
        user()
    else:
        print("Invalid option.")

