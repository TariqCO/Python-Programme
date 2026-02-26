def loginSystem():
    
    admin1="tariq001"    
    passAdmin1 = "Helloworld1712#" 
    
    user1="sufiyan002"    
    passUser1 = "Fa108ok31@" 
    
    while True:
        username = input("Enter your username: ")
        
        while True:
            password = input("Enter your password: ")
        
            if len(password) < 8:
                print("Password must be atleast 8 characters long.")
                continue
            elif password == passAdmin1 or password == passUser1:
                break
            else:
                print("Wrong Password..")
                continue
            

        role = int(input("Enter the role: (1. Admin 2. User) -->| "))
        
        if (role == 1):
            if (username == admin1) and (password == passAdmin1):
                print("\n ===== Admin =====")
                print(f"\nWelcome {username}, \nTo the Admin dashboard")
                personRole = "admin"
                break
            elif password != passAdmin1:
                print("\n--- Invalid Details ---")
                print(f"Incorrect Password\n")
                continue
            else:
                print("\n--- Invalid Details ---")
                print(f"There is no Admin registered with these details\n")
                continue
        elif(role == 2):
            if (username == user1) and (password == passUser1 ):   
                print("\n ===== User =====")
                print(f"\nWelcome {username}, \nTo our website.")
                personRole = "user"
                break
            elif password != passUser1:
                print("\n--- Invalid Details ---")
                print(f"Incorrect Password\n")
                continue
            else:
                print("\n--- Invalid Details ---")
                print(f"There is no User registered with these details\n")
                continue
        else:
            print("Invalid Input")
            
    return personRole



loginSystem()