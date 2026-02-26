import random

choices = ["Rock", "Paper", "Scissor"]

def ranRPSfunc():
    return random.choice(choices)

print("-" * 45)
print("Let's play Rock, Paper and Scissor")
print("-" * 45)

userName = input("Enter your name: ")
botName = input("Name your bot: ")


while True:
    
    userScore = 0
    botScore = 0
    
    i = 1
    while i <= 5:
        userInp = input("\nType Rock , Paper or Scissor -->| ").capitalize()
        botInp = ranRPSfunc()
    
        if userInp == botInp:
            print("")
            print("=" * 45)
            print(f"Game Draw --> {userName}: {userInp} | {botName}: {botInp}")
            print("=" * 45)
            userScore += 1
            botScore += 1
            
        elif userInp == "Rock" and botInp == "Paper":
            print("")
            print("=" * 45)
            print(f"{botName} win --> {userName}: {userInp} | {botName}: {botInp}")
            print("=" * 45)
            botScore += 2
            
        elif userInp == "Rock" and botInp == "Scissor":
            print("")
            print("=" * 45)
            print(f"You win --> {userName}: {userInp} | {botName}: {botInp}")
            print("=" * 45)
            userScore += 2
            
        elif userInp == "Paper" and botInp == "Rock":
            print("")
            print("=" * 45)
            print(f"You win --> {userName}: {userInp} | {botName}: {botInp}")
            print("=" * 45)
            userScore += 2
            
        elif userInp == "Paper" and botInp == "Scissor":
            print("")
            print("=" * 45)
            print(f"{botName} win --> {userName}: {userInp} | {botName}: {botInp}")
            print("=" * 45)
            botScore += 2
            
        elif userInp == "Scissor" and botInp == "Rock":
            print("")
            print("=" * 45)
            print(f"{botName} win --> {userName}: {userInp} | {botName}: {botInp}")
            print("=" * 45)
            botScore += 2
            
        elif userInp == "Scissor" and botInp == "Paper":
            print("")
            print("=" * 45)
            print(f"You win --> {userName}: {userInp} | {botName}: {botInp}")
            print("=" * 45)
            userScore += 2
            
        else:
            print("Invalid Input..")
        

        
# =====Continue Game==============================================================================================================
        
        
        if i == 5:
            again = input("\nDo you want to continue or wanna print result? (1. Result 2. Continue): ").capitalize()
            if again == "1" or again == "Result":
                print("\n========== Result ==========")
                if userScore > botScore:
                    print("-" * 20)
                    print(f"{userName} Win")
                    print("-" * 20)
                elif userScore == botScore:
                    print("-" * 20)
                    print(f"Game Draw")
                    print("-" * 20)
                else:
                    print("-" * 20)
                    print(f"{botName} Win")
                    print("-" * 20)
                    
                print(f"\n{userName}'s Score: {userScore} ,{botName}'s Score: {botScore}")
                break
            elif again == "2" or again == "Continue":
                print(f"\n============== Continuing the current game ==============")
                i = 1
                continue
            else:
                print("\nInvalid option selected to continue the game...")
                break
        else:
            i += 1  
        
      
        
# =====Restart Game==============================================================================================================

    restart = input("\nDo you want restart? (1. yes 2. no): ").lower()

    if restart == "1" or restart == "yes":
        print("\n============== Restarting the game ==============")
        continue
    elif restart == "2" or restart == "no":
        print("\nThank You for playing hope you enjoyed it! Exiting....")
        break            
    else:
        print("\nInvalid option selected to restart the game....")
        break
        