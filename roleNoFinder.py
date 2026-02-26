
stTariq=352
stRafay=623
stAkber=400

# Dummy user details

# name : Tariq Rasheed
# class : 8
# sec : B

# name : Rafay Shaikh
# class : 10
# sec : C

# name : Akber Ali
# class : 10
# sec : A

print("\n=============== Find your Roll number ===============\n")


while True:
    print("\nSearch --> \n")
    
    fname = input("Enter your First name --> | ").capitalize()
    lname = input("Enter your Last name --> | ").capitalize()
    clss = input("Enter your Class --> | ")
    sec =  input("Enter your Section --> | ").lower()
    
    if (fname == "Tariq") and (lname == "Rasheed") and (clss == "8") and (sec == "b"):
        for i in range(200 , 800 + 1):
            if stTariq == i:
                print(f"\nName: {fname} {lname}, Roll No: {i}")
                break
            else:
                print(f"searching list.... {i}")
                continue
            
        break
    elif (fname == "Rafay") and (lname == "Shaikh") and (clss == "10") and (sec == "c"):
        for i in range(300 , 800 + 1):
            if stRafay == i:
                print(f"Name: {fname} {lname}, Roll No: {i}")
                break
            else:
                print(f"searching list.... {i}")
                continue
            
        break
    elif (fname == "Akber") and (lname == "Ali") and (clss == "10") and (sec == "a"):
        for i in range(300 , 800 + 1):
            if stAkber == i:
                print(f"Name: {fname} {lname}, Roll No: {i}")
                break
            else:
                print(f"searching list.... {i}")
                continue
            
        break
    else:
        print(f"\nThere is no student with these details.\nName: {fname} {lname}\nClass: {clss}\nSection: {sec}")
        again= int(input("\nWant to  Search again? (1.Yes 2.No) --> | "))
        if again == 1:
            continue
        else:
            print("\nExiting.. Thanks!")
            break
    