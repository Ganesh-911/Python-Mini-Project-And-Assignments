def main():

    size = int(input("Enter the size of the matrix : "))

    matrix = []
    
    row = 0
    column = 0

    while row < size:
        
        rowlist = []

        while column < size:

            print("Enter the number at position : ", row, column)
            rowlist.append(int(input()))
            column += 1

        matrix.append(rowlist)

        row += 1
        column = 0

    print("\nYou entered the matrix :\n")

    for i in matrix:
        print(i)

    U = [[0 for x in range(size)] for y in range(size)]

    L = [[0 for x in range(size)] for y in range(size)]

    for i in range(size):

        for k in range(i, size):

            sums = 0

            for j in range(i):

                sums += L[i][j] * U[j][k]

            U[i][k] = matrix[i][k] - sums

        for k in range(i, size):

            if i == k:

                L[i][i] = 1

            else:

                sums = 0

                for j in range(i):

                    sums += L[k][j] * U[j][i]

                L[k][i] = int(((matrix[k][i] - sums) / U[i][i]))

    print("\nL is :\n")

    for i in L:
        print(i)
        
    print("\nU is :\n")

    for i in U:
        print(i)

main()