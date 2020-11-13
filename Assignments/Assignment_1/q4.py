import random

random_number = random.choice(range(1, 26))

chances = 5

print("You have 5 chances to gues the random number which ranges from 1 to 25\n")

while(chances):

    guess = int(input("Enter your guess : "))
    
    print("Your guess is ", guess)

    if guess == random_number:

        print("Congratulations! You have guessed the random number correctly.")

        exit(0)

    elif guess < random_number:

        print("Sorry your guess is smaller than the generated random number.")

    else:

        print("Sorry your guess is larger than the generated random number.")

    chances -= 1
        