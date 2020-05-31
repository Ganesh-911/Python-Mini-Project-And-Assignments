start = int(input("Enter starting number of the range : "))

end = int(input("Enter the ending number of the range : "))

list_of_Amstrong_numbers = []

for number in range(start, end):

    s = 0

    t = number
    
    while t > 0:

        r = t % 10

        s += r**3

        t = t//10

    if s == number:

        list_of_Amstrong_numbers.append(number)

print(list_of_Amstrong_numbers)