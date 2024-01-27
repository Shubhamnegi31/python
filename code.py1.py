
num = int(input("We need you to guess a number: "))

if num == 12:
    print("Excellent, you guessed it right")
else:
    print("No, it's a wrong guess")
    no = int(input("We need you to guess a number again: "))
    
    if no == 12:
        print("Great, your second guess is right")
    else:
        print("No, it's a wrong guess")
        nu = int(input("We need you to guess a number again: "))
        
        if nu == 12:
            print("Bravo, your third guess is right")
        else:
            print("Oops, your guess chances are over. Better luck next time.")
 
