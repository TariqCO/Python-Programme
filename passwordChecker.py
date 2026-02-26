

while True:
    password = input("Enter your password: ")
    specialChar = ["#","!","@","$","%","^","&","*"]

    char = False
    
    for i in range(len(specialChar)):
        for j in range(len(password)):
            if (specialChar[i] == password[j]):
                char = True
                break

    
    if len(password) < 8:
        print("Password must be atleast 8 characters long.")
    else:
        if char == True:
            print("Strong password")
            break
        else:
            print("Weak password")
            continue
            
            
            
            
            
            
            
            
            
            
            