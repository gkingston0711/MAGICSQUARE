def rowSum(matrix, row):
    Sum = 0
    for i in range(len(matrix[row])):
        Sum = Sum + matrix[row][i]
    return Sum

def colSum(matrix,col):
    Sum = 0
    for i in range(len(matrix)):
        Sum = Sum + matrix[i][col]
    return Sum

def diagSum(matrix):
    Sum = 0
    for i in range(len(matrix[0])):
        Sum = Sum + matrix[i][i]
    return Sum

def oppDiagSum(matrix):
    Sum = 0
    Length = len(matrix)
    for i in range(Length):
        Sum = Sum + matrix[Length - 1 - i][i]
    return Sum

def calcAllSum(matrix):
    """
        Calculate, and print all sum of all rows, column, and diagonal
    """
    for i in range(len(matrix)):
        sum_row = sumRow(matrix, i)
        print('Sum of row: ', sum_row)

    for i in range(len(matrix[0])):
        sum_col = sumCol(matrix, i)
        print('sum of column: ', sum_col)

    print('sum of main diagonal: ', sumMainDiag(matrix))
    print('sum of other diagonal: ', sumReverseDiag(matrix))


def isMagic(matrix):
    """
        Return true if the square is magic, false otherwise
    """

    # Calculate sum at row 0 for comparing all other rows, col, and diagonal
    sum_t = sumRow(matrix, 0)
    # Check all rows
    for i in range(1, len(matrix)):
        sum_row = sumRow(matrix, i)
        if sum_row != sum_t:      # Return false if one of them is not equal
            return False

    # Check all columns
    for i in range(len(matrix[0])):
        sum_col = sumCol(matrix, i)
        if sum_col != sum_t:      # Return false if one of them is not equal
            return False

    # Check main diagonal
    main_diagonal = sumMainDiag(matrix)
    if sum_t != main_diagonal:
        return False

    # Check reverse diagonal
    reverse_diagonal = sumReverseDiag(matrix)
    if sum_t != reverse_diagonal:
        return False

    # Pass all, return True for magic matrix
    return True

def printMatrix(matrix):
    """
        Print all values of a matrix
    """
    for row in matrix:
        for num in row:
            print(num, " ", end)
        print()

def createRow(row_str):
    """
        Return row number matrix from a string row
    """
    row = []
    row_str = row_str.rstrip('\n')
    row_str = row_str.split(' ')
    for num in row_str:
        if num != '':
            row.append(int(num))
    return row



def main():
    Count = 0
    fileOpen = open('square.txt','r')

    while True:
        matrix = []
        size = fileOpen.readline()
        size = int(size.rstrip('\n'))
        if size <= 0:
            return
        print('the size of the square: ', size)
        Count +=1

        for j in range(size):
            rowStr = fileOpen.readline()
            row = createRow(rowStr)
            matrix.append(row)

        print('****square %d*****' %Count)
        printMatrix(matrix)
        calcAllSum(matrix)

        if(isMagic(matrix)==True):
            print('IT IS MAGIC SQUARE')
        else:
            print('IT IS NOT A MAGIC SQUARE')

        print()


main()





