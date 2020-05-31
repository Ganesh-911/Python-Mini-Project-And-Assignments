import math

print("The First 10 pairs of amicable numbers are : ")

def find_sum_of_factors(number):

    i = 2

    sum = 0

    while i <= math.sqrt(number):

        if number % i == 0:

            if number / i == i:
                sum += i 

            else:
                sum += number / i
                sum += i
        
        i += 1

    return sum + 1

list_of_pairs_of_amicable_numbers = []

num = 2

count = 0

while count != 10:

    first_sum = find_sum_of_factors(num)
    next_sum = find_sum_of_factors(first_sum)

    if (next_sum == num) and (num != first_sum):

        list_of_pairs_of_amicable_numbers.append((num, int(first_sum)))
        
        count += 1

    num += 1

    for k in list_of_pairs_of_amicable_numbers:

        if (num == k[0]) or (num == k[1]):

            num += 1

for pair in list_of_pairs_of_amicable_numbers:

    print(pair)