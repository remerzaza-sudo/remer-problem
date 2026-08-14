import random

word = ["sigma", "python", "code", "linux", "online"]
words = random.choice(word)


guesses = ''
attempts = 10
print("Guess words")

while attempts > 0:
    failed = 0
    for ch in words:
        if ch in guesses:
            print(ch, end="")
        else :
            print("_",end="")
            failed +=1

    print()
    if failed == 0:
         print("Win")
         print(f"Word is {words}")
         break

    user = input("Time to guess> ").lower()
    print()


    #check invalid charactor
    if len(user) != 1:
        print("can guess only single charactor")
        continue
    #when user has guesses that char
    if user in guesses :
        print("you have already guess this charactor")
        continue

    guesses += user
    #If user input wrong char turns will -1
    if user not in words:
        attempts -= 1
        print("Your wrong!")
        print(f"your have {attempts} more guess")

        #when user out of turn user lose
        if attempts == 0:
            print("you lose")
            print("The Word was", words)
            break
