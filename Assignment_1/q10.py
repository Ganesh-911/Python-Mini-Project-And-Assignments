print("Enter the first number and the common ratio of the geometric series.")

a = float(input("Enter the first number : "))

r = float(input("Enter the common ratio : "))

count = 0

term_list = []

while count < 10:
    
    term_list.append((a * (r ** count)))

    count += 1

print("The first 10 numbers in the series are : ",term_list)