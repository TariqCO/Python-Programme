cart = []

def addCategorie(name, allItems):
    print(f"\n ==== Add {name} to your cart ====\n")
    items = allItems
    
    for j in items:
        print(f"- {j}")
        
    while True:
        item = input(f"\n Add item: ")
        itemInd = items.index(item)
        
        cart.append(items[itemInd])
        print(f" ✅ {item} added.. ")

        again =input(f" Do you want to add more {name}? (1.yes 2.no): ").lower()
        
        if again == "1" or again == "yes":
            continue
        elif again == "2" or again == "no":
            break
        else:
            print("\n-- Invalid input --")
                

i = 1
while i <= 4:
    if i == 1:
        groceries = ["rice", "wheat", "spices", "oil", "sugar", "lentils"]
        addCategorie("groceries",groceries)
        
    elif i == 2:
        fruits = ["apple", "bannana", "guava", "mango", "strawberry"]
        addCategorie("fruits", fruits)

    elif i == 3:
        clothes = ["shirt", "T-Shirt", "pant", "trouser", "jacket", "upper", "hoodie"]
        addCategorie("clothes",clothes)
        
    elif i == 4:
        accessories = ["head phone", "SSD Card", "graphic card", "keyboard", "mouse"]
        addCategorie("accessories",accessories)
    
    else:
        print("Invalid input..")   
        
    i += 1

print(f"\n-------- Cart({len(cart)}) --------")
print(f"\nThese are the items in your cart: \n")

for i in cart:
    print(f"{i}")
