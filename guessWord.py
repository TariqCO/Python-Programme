
print("\n======= Guess the secret word game =========\n")

print("====== Set the word and the hints for your friend to guess ======\n")
theWord = input("Enter the word: ").lower()

hint1 = input(f"Give 1st hint for the word {theWord}: ")
hint2 = input(f"Give 2nd hint for the word {theWord}: ")
hint3 = input(f"Give 3rd hint for the word {theWord}: ")

guessCount = 5
hintCount = 3

while guessCount >= 1:
    word = input("\nGuess the word: ").lower()
    
    if (word != theWord) and (hintCount >= 1) and (guessCount > 1):
        guessCount -= 1
        print(f"\nNo, its not a {word} {guessCount} guess left")
        
        hint = input(f"\n{hintCount} Hints, Do you want a hint? (yes/no) --> | ").lower()
        if hint == "yes" and hintCount == 1:
            print(f"\n{hint3}")
            hintCount -= 1
            print(f"--> {hintCount} hint left")
            continue
        elif hint == "yes" and hintCount == 2:
            print(f"\n{hint2}")
            hintCount -= 1
            print(f"--> {hintCount} hints left")
            continue
        elif hint == "yes" and hintCount == 3:
            print(f"\n{hint1}")
            hintCount -= 1
            print(f"--> {hintCount} hints left")
            continue        
        else:
            continue
    elif word == theWord:
        print(f"\nYou Got the right word. It's a {theWord}")
        if guessCount == 5:
            if hintCount == 3:
                print(f"You Guess it in on first try without using any hint --> Score: 100")
            elif hintCount == 2:
                print(f"You Guess it in on first try used 1 hint --> Score: 95")
            else:
                print(f"You Guess it in on first try used 2 hints --> Score: 90")
                
        elif guessCount == 4:
            if hintCount == 3:
                print(f"Guess it in on second try without using any hint--> Score: 100")
            elif hintCount == 2:
                print(f"Guess it in on second try used 1 hint --> Score: 90")
            else:
                print(f"Guess it in on second try used 2 hints --> Score: 85")
        elif guessCount == 3:
            if hintCount == 3:
                print(f"Guess it in on third try without using any hint--> Score: 85")
            elif hintCount == 2:
                print(f"Guess it in on third try used 1 hint --> Score: 80")
            else:
                print(f"Guess it in on third try used 2 hints--> Score: 75")
        else:
            if hintCount == 3:
                print(f"Guess it in on fourth try without using any hint--> Score: 80")
            elif hintCount == 2:
                print(f"Guess it in on fourth try used 1 hint --> Score: 75")
            else:
                print(f"Guess it in on fourth try used 2 hints--> Score: 70")
        break  
    else:
        guessCount -= 1
        print(f"\nNo, its not a {word} {guessCount} guess left")
        if guessCount == 0:
            break
        else:
            continue