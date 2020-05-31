import random

while True:
    print('Dice shows : ',random.choice(range(1,7)))

    again = input('Do you want to reroll the dice? press Y(y) for yes and N(n) for no : ')

    if again == 'Y' or again == 'y':
        continue
        
    elif again == 'N' or again == 'n':
        print("Stopping the dice rolling simulator.")
        break
        
    else:
        print("Invalid choice!")
        print("Stopping the dice rolling simulator.")
        break