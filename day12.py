def is_prime(num):
    if num <= 2:
        return True
    for i in range(2, num-1):
        if num%i == 0:
            return False
    return True


# print(is_prime(75))


# guessing game


#TODO-1: select a number to geuss randomly
import random

number = random.randint(0, 100)


    


#TODO-3: create a the game

def game(number, attempts):

    guess = int(input("enter your guess "))
    attempts -=1
    
    while guess != number and attempts > 0:

        if number > guess:
            print("too low")
            guess = int(input("enter another guess: "))
        elif number < guess:
            print("too high")
            guess = int(input("enter another guess: "))
       

        attempts -= 1
    if guess == number:
        print(f"you got it the number was {number}")

    elif guess != number and attempts == 0:
        print(f"looseeerrr, the number was {number} dumbass")






#TODO-2: select gamemode(easy: 10 attempts or hard: 5 attempts)
mode = input("enter 'eays' or 'hard': ")
if mode == "easy":
   attempts = 10
   
elif mode == "hard":
    attempts = 5

game(number, attempts)



