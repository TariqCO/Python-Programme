
#Challenge is to not use "Dictionary" only use "List" to hold data.

cabTypList = ["Mini", "Rickshaw", "Ride A/C" , "Premium"]

def miniOwnersFunc():
    owners = ["Akhtar bhutto","Saleem javed", "Raheel mukhtar"]
    ratings = [4.2, 4.7, 4.8]
    rides = [200, 700, 2000]
    charges = [50, 70, 20]
    cars = ["Suzuki Alto", "Toyota Mira", "Suzuki Cultus"]
    
    return [owners,ratings, rides,charges, cars]

def rickShawOwnersFunc():
    owners = ["Mehmood saab", "Sufiyan muqeem"]
    ratings = [4.2, 4.6]
    rides = [500, 1000]
    charges = [60, 30]
    cars = ["Sazgar", "Rozgar"]
    
    return [owners,ratings, rides,charges,cars]

def rideACOwnersFunc():
    owners = ["Akber junejo", "Saleem rider"]
    ratings = [4.8, 4.9]
    rides = [2500, 1500]
    charges = [20, 40]
    cars = ["Suzuki Cultus", "Suzuki Alto"]
    
    return [owners,ratings, rides,charges, cars]    

def premiumOwnersFunc():
    owners = ["Junaid Akram", "Tariq Rasheed"]
    ratings = [4.0, 4.9]
    rides = [200, 1200]
    charges = [20, 70]
    cars = ["Toyota Corolla", "Honda City"]
    return [owners,ratings,rides,charges, cars]    

 

locations = [
    "Safari Park",        # 0
    "Millennium Mall",    # 1
    "LuckyOne Mall",      # 2
    "Expo Centre Karachi",# 3
    "Dolmen Mall Clifton",# 4
    "Port Grand",         # 5
    "Karachi Zoo",        # 6
    "Jinnah International Airport" # 7
]

def get_ride_details(pickup, dropoff):
    if pickup == locations[0]:  # Safari Park
        if dropoff == locations[1]:
            fare, duration, distance = 313, 13, 4.6
        elif dropoff == locations[2]:
            fare, duration, distance = 325, 10, 5.0
        elif dropoff == locations[3]:
            fare, duration, distance = 280, 11, 4.2
        elif dropoff == locations[4]:
            fare, duration, distance = 410, 20, 8.1
        elif dropoff == locations[5]:
            fare, duration, distance = 370, 17, 6.8
        elif dropoff == locations[6]:
            fare, duration, distance = 180, 7, 2.5
        elif dropoff == locations[7]:
            fare, duration, distance = 620, 28, 13.4
        else:
            fare, duration, distance = 300, 11, 4.2

    elif pickup == locations[1]:  # Millennium Mall
        if dropoff == locations[0]:
            fare, duration, distance = 313, 13, 4.6
        elif dropoff == locations[2]:
            fare, duration, distance = 300, 9, 5.6
        elif dropoff == locations[3]:
            fare, duration, distance = 306, 11, 5.5
        elif dropoff == locations[4]:
            fare, duration, distance = 380, 18, 7.3
        elif dropoff == locations[5]:
            fare, duration, distance = 340, 15, 6.1
        elif dropoff == locations[6]:
            fare, duration, distance = 290, 12, 4.9
        elif dropoff == locations[7]:
            fare, duration, distance = 590, 25, 12.7
        else:
            fare, duration, distance = 300, 11, 4.2

    elif pickup == locations[2]:  # LuckyOne Mall
        if dropoff == locations[0]:
            fare, duration, distance = 325, 10, 5.0
        elif dropoff == locations[1]:
            fare, duration, distance = 300, 9, 5.6
        elif dropoff == locations[3]:
            fare, duration, distance = 322, 15, 5.7
        elif dropoff == locations[4]:
            fare, duration, distance = 430, 22, 9.0
        elif dropoff == locations[5]:
            fare, duration, distance = 390, 19, 7.5
        elif dropoff == locations[6]:
            fare, duration, distance = 310, 13, 5.2
        elif dropoff == locations[7]:
            fare, duration, distance = 640, 30, 14.1
        else:
            fare, duration, distance = 300, 11, 4.2

    elif pickup == locations[3]:  # Expo Centre Karachi
        if dropoff == locations[0]:
            fare, duration, distance = 280, 11, 4.2
        elif dropoff == locations[1]:
            fare, duration, distance = 306, 11, 5.5
        elif dropoff == locations[2]:
            fare, duration, distance = 322, 15, 5.7
        elif dropoff == locations[4]:
            fare, duration, distance = 460, 24, 9.8
        elif dropoff == locations[5]:
            fare, duration, distance = 420, 21, 8.4
        elif dropoff == locations[6]:
            fare, duration, distance = 265, 10, 3.9
        elif dropoff == locations[7]:
            fare, duration, distance = 550, 23, 11.8
        else:
            fare, duration, distance = 300, 11, 4.2

    elif pickup == locations[4]:  # Dolmen Mall Clifton
        if dropoff == locations[0]:
            fare, duration, distance = 410, 20, 8.1
        elif dropoff == locations[1]:
            fare, duration, distance = 380, 18, 7.3
        elif dropoff == locations[2]:
            fare, duration, distance = 430, 22, 9.0
        elif dropoff == locations[3]:
            fare, duration, distance = 460, 24, 9.8
        elif dropoff == locations[5]:
            fare, duration, distance = 220, 9, 3.5
        elif dropoff == locations[6]:
            fare, duration, distance = 395, 19, 7.7
        elif dropoff == locations[7]:
            fare, duration, distance = 700, 33, 15.6
        else:
            fare, duration, distance = 300, 11, 4.2

    elif pickup == locations[5]:  # Port Grand
        if dropoff == locations[0]:
            fare, duration, distance = 370, 17, 6.8
        elif dropoff == locations[1]:
            fare, duration, distance = 340, 15, 6.1
        elif dropoff == locations[2]:
            fare, duration, distance = 390, 19, 7.5
        elif dropoff == locations[3]:
            fare, duration, distance = 420, 21, 8.4
        elif dropoff == locations[4]:
            fare, duration, distance = 220, 9, 3.5
        elif dropoff == locations[6]:
            fare, duration, distance = 355, 16, 6.4
        elif dropoff == locations[7]:
            fare, duration, distance = 480, 21, 10.2
        else:
            fare, duration, distance = 300, 11, 4.2

    elif pickup == locations[6]:  # Karachi Zoo
        if dropoff == locations[0]:
            fare, duration, distance = 180, 7, 2.5
        elif dropoff == locations[1]:
            fare, duration, distance = 290, 12, 4.9
        elif dropoff == locations[2]:
            fare, duration, distance = 310, 13, 5.2
        elif dropoff == locations[3]:
            fare, duration, distance = 265, 10, 3.9
        elif dropoff == locations[4]:
            fare, duration, distance = 395, 19, 7.7
        elif dropoff == locations[5]:
            fare, duration, distance = 355, 16, 6.4
        elif dropoff == locations[7]:
            fare, duration, distance = 600, 27, 13.0
        else:
            fare, duration, distance = 300, 11, 4.2

    elif pickup == locations[7]:  # Jinnah International Airport
        if dropoff == locations[0]:
            fare, duration, distance = 620, 28, 13.4
        elif dropoff == locations[1]:
            fare, duration, distance = 590, 25, 12.7
        elif dropoff == locations[2]:
            fare, duration, distance = 640, 30, 14.1
        elif dropoff == locations[3]:
            fare, duration, distance = 550, 23, 11.8
        elif dropoff == locations[4]:
            fare, duration, distance = 700, 33, 15.6
        elif dropoff == locations[5]:
            fare, duration, distance = 480, 21, 10.2
        elif dropoff == locations[6]:
            fare, duration, distance = 600, 27, 13.0
        else:
            fare, duration, distance = 300, 11, 4.2

    else:
        fare, duration, distance = 500, 15, 5.2

    return [fare, duration, distance]
    

print("\n=============== let's Move - At your service ================\n")

#User Details

print("\n---------- Passenger details ---------- \n")
custName = input("Enter your name: ")
custEmail = input("Enter your email: ")
custCont = input("Enter your contact number: ")

while True:
    print("\n---------- Where to & for how much? ------------ \n")
    
    for loc in locations:
        print(f"- {loc}")
    
    print("")
    pickUp = input("From : ")
    dropOff = input("To : ")
    
    print("\nSelect Cab Type: ")
    
    print("")
    for cabTyp in  cabTypList:
        print(f"- {cabTyp}")
    
    selectCabTyp = input(" --------->| ").lower()
    
    selectFair = int(input("\nEnter Fair: "))
     
    find_offers = input("Find Offers (yes/no): ").lower()    
    
    if find_offers == "yes":
        if selectCabTyp == "mini":
            driverDets = miniOwnersFunc()
                
        elif selectCabTyp == "rickshaw":
            driverDets = rickShawOwnersFunc()

        elif selectCabTyp == "rideac":
            driverDets = rideACOwnersFunc()
            
                
        elif selectCabTyp == "premium":
            driverDets = premiumOwnersFunc()
            
        else:
            print("Invalid Cab Type input !")
            
        ride_details = get_ride_details(pickUp, dropOff)    
            
        for i in range(len(driverDets[0])):
            print(f"\n{i + 1}: ")
            print(f"{driverDets[0][i]} ⭐{driverDets[1][i]}  {driverDets[2][i]} rides")
            print(f"{driverDets[4][i]}")     
            print(f"PKR {ride_details[0] + driverDets[3][i]}")


        
        while True:
            selectOffer = int(input("\nSelect offer: "))
            
            if selectOffer >= 1 and selectOffer < (len(driverDets[0]) + 1):
                print("\n======== Ride Reservation Details ========\n")
                print(f"Driver --> {driverDets[0][selectOffer - 1]}")
                print(f"Cab --> {driverDets[4][selectOffer - 1]}")
                print(f"Ride --> {selectCabTyp.capitalize()}")
                print("")
                print(f"Pick Up --> {pickUp}")
                print(f"Drop Down --> {dropOff}")
                print(f"Duration --> {ride_details[1]}mins")
                print(f"Distance --> {ride_details[2]}km")
                print(f"Arriving in {4}mins")
                print(f"Amount Payable --> PKR {ride_details[0] + driverDets[3][selectOffer - 1]}")
                
                print(f"\n======= User Details =======")
                print(f"Name: {custName}") 
                print(f"Email: {custEmail}")
                print(f"Contact: {custCont}")
                
                break
            else:
                print("Select according to the offers!")
                continue

            
            
        break
            
    elif find_offers == "no":
        continue

    else:
        break
