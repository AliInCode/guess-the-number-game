import random
import pyfiglet
print(pyfiglet.figlet_format("Guess Number "))
def guessnumber():
    computer = random.randint(1,20)
    attempts = 0
    print("Welcome to Guess Number game")
    print("Im thinking of a number between 1 and 20")
    while True:
        try:
            player_guess = int(input("Guess  your number :"))
            if player_guess < 1 or player_guess > 20 :
                print(" number must between 1 and 20")
        except ValueError:
            print("Invalid input. please enter a number")
        attempts+=1
        if computer > player_guess:
            print("Too low!")
        elif computer < player_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guess send the number in {attempts} attempts")
            break
        print(f"your attempts : {attempts}")
guessnumber()