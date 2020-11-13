import math

print("The first 10 Harmonic Divisor Numbers are : ")

def find_factors(number):
    
    list_of_factors = []    
    n = 1

    while n <= math.sqrt(number):

        if number % n == 0:

            if number / n == n:
                list_of_factors.append(n)

            else:
                list_of_factors.append(n)
                list_of_factors.append(number / n)

        n += 1
    return list_of_factors
    
num = 1
count = 0

while count != 10:
    s = 0
    l = find_factors(num)

    for k in l:
        s += 1.0 / k

    result = len(l) / s

    if round(result, 6).is_integer():
        print(num)

        count += 1
    num += 1