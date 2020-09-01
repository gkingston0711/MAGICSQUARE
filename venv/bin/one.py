
def sumRow(matrix, col):

    Sum = 0
    Length = len(matrix[col])
    for row in range(Length):
        Sum = Sum + matrix[col][row]
    return Sum


def sumCol(matrix, row):

    Sum = 0
    Length = len(matrix)
    for col in range(Length):
        Sum = Sum + matrix[col][row]
    return Sum

def sumMainDiag(matrix):

    Sum = 0
    Length = matrix[0]
    for row in range(len(Length)):
        Sum = Sum + matrix[row][row]
    return Sum

def sumReverseDiag(matrix):

    Sum = 0
    Length = len(matrix)
    for row in range(Length):
        Sum = Sum + matrix[Length - 1 - i][row]
    return Sum
"""
This function was also taken from external source, in my origianl version i did all calculations 
inside main
"""
def calcAllSum(matrix):

    for i in range(len(matrix)):
        Sum = sumRow(matrix, i)
        print('Sum row: ', Sum)

    for i in range(len(matrix[0])):
        SumCol = sumCol(matrix, i)
        print('sum col: ', SumCol)

    print('sum diagonal: ', sumMainDiag(matrix))
    print('sum of other diagonal: ', sumReverseDiag(matrix))


"""
This "ismagic" function is same as the solution sheet. In my original  I did this and calculate the sum all inside my
main, which got a little messy
"""
def isMagic(matrix):

    sum_t = sumRow(matrix, 0)
    for i in range(1, len(matrix)):
        sum_row = sumRow(matrix, i)
        if sum_row != sum_t:
            return False


    for i in range(len(matrix[0])):
        sum_col = sumCol(matrix, i)
        if sum_col != sum_t:
            return False


    main_diagonal = sumMainDiag(matrix)
    if sum_t != main_diagonal:
        return False

    # Check reverse diagonal
    reverse_diagonal = sumReverseDiag(matrix)
    if sum_t != reverse_diagonal:
        return False


    return True

def printMatrix(matrix):

    for row in matrix:
        for num in row:
            print num

"""
this create row was my biggest issue in my original code, my original was called
helper, since this is a basic helper function, creates an array row in which the 
main append  it to the matrix
"""
def createRow(row_str):

    row = []
    row_str = row_str.rstrip('\n')
    row_str = row_str.split(' ')

    for num in row_str:
        if num != '':
            row.append(int(num))
    return row

"""
Most of the main method was taken from original 
My original logic was the same i just had issue with reading in
first line
"""
def main():

    inFile = open('square.txt', 'r')
    counter = 0

    while(1):
        matrix = []

        size = inFile.readline()
        size = int(size.rstrip('\n'))

        if size == -1:
            return
        print ('size is: ', size)
        counter += 1

        for i in range(size):
            row_str = inFile.readline()
            row = createRow(row_str)
            matrix.append(row)

        print('***** Square  %d *****' % counter)
        printMatrix(matrix)
        calcAllSum(matrix)


        if (isMagic(matrix)):
            print ('magic square')
        else:
            print ('normal square')

        print()


main()



