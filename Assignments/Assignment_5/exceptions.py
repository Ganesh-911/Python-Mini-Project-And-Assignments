# Raising and Handling Exceptions

#division by zero

p = int(input("\nEnter devidend : "))

while True:

    try:

        q = int(input("\nEnter devisor : "))
        result = p / q

    except ZeroDivisionError:

        print("\nError! You tried to devide by zero.")

    else:

        print("\nNo error occured.\n")
        print("Result = ", result, "\n")
        break

#keyboard interrupt

try:

    inp = input("Press Ctrl + C to interrupt : \n")

except KeyboardInterrupt:

    print("\nCaught the keyboard interrupt error")

else:

    print("\nNo exception occured")

# index error

try:

    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = int(input("\nEnter the index you want to access : "))
    num = mylist[i]

except LookupError:

    print("\nIndex error occured.")

else:
    print("\nNo error occured while accessing the array element.\n")
    print("The array element is : ", num)