#print("hello testing one two")
import random
easy = random.randint(1, 10)
hard = random.randint(1, 50)
medium = random.randint(1, 20)

name = input('Hello there, what is your name?')
picked = input("please select easy(e),medium(m),hard(h): ")
picked = picked.lower()


if picked == "e":
    print("well, {} , I'm thinking of a number between 1 and 10 \nWhy don't you take a guess".format(name.upper()))
    for guesscount in range(5):
        number = easy
        guess = int(input())
        if guess < number:
            print("too low, try again")
        elif guess > number:
            print("too high, drop it low")
        else:
            pass

elif picked == "m":
    print("well, {} , I'm thinking of a number between 1 and 50 \nWhy don't you take a guess".format(name.upper()))
    for guesscount in range(3):
        number = medium
        guess = int(input())
        if guess < number:
            print("too low, try again")
        elif guess > number:
            print("too high, drop it low")
        else:
            pass

elif picked == "h":
    print("well, {} , I'm thinking of a number between 1 and 50 \nWhy don't you take a guess".format(name.upper()))
    for guesscount in range(2):
        number = hard
        guess = int(input())
        if guess < number:
            print("too low, try again")
        elif guess > number:
            print("too high, drop it low")
        else:
            pass

else:
    print("please select an appropriate level:")


#for guesscount in hard,medium,easy:
guess = int(input())
if guess < number :
    print("too low, try again")
elif guess > number :
    print("too high, drop it low")
else:
    pass
if guess == number :
    print("Hooray, you got it")
else:
    print("you' maxed out your chances, the number was {}".format(number))