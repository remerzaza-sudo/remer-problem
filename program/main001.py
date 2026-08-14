from random import randint


print()
print("Welcome to game guessing number this prject made for you! \n"
        "I made this mini project for undertand concept loop statement and logic \n"
        "you have a 10 chance to guess number if you guess more than 10 you lose \n"
        "range number in this game is 1 - 100")
print()

guess = 0
chance = 10
min = 1
max = 100

#random number:
ran_num = randint(min,max)

run = True
while run:
    if guess < chance:
        guess += 1
    print("Guessing number :)")
    guessing = (input("\t(q to quit)>"))
    if guessing.lower() == "q":
        break

    guessing = int(guessing)
    if guessing == ran_num:
        print(f"Finally you got it your number is {ran_num} ")
        print(f"Total guess {guess} attempts")
        break
    elif guess >= chance and guess != ran_num:
        print("You lose, you can guess again")
        break
    elif guessing > ran_num:
        print("It's too high")
    elif guessing < ran_num:
        print("It's too low")


print("Thanks for playing my number guessing game! ;)")
