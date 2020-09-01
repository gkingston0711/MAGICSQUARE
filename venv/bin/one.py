
def sumRow(matrix, row):
    """
        Return the sum of the values in the given row
    """
    sum_t = 0
    for i in range(len(matrix[row])):
        sum_t = sum_t + matrix[row][i]
    return sum_t

def sumCol(matrix, col):
    """
        Return the sum of the valus in the given col
    """
    sum_t = 0
    for i in range(len(matrix)):
        sum_t = sum_t + matrix[i][col]
    return sum_t

def sumMainDiag(matrix):
    """
        Return the sum of the values in the main diagonal
    """
    sum_t = 0
    for i in range(len(matrix[0])):
        sum_t = sum_t + matrix[i][i]
    return sum_t

def sumReverseDiag(matrix):
    """
        Return the sum of the value in the reverse diagonal
    """
    sum_t = 0
    len_t = len(matrix)
    for i in range(len_t):
        sum_t = sum_t + matrix[len_t - 1 - i][i]
    return sum_t

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
            print num


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

    inFile = open('square.txt', 'r')
    counter = 0
    while(1):
        matrix = []
        # Read the size of the matrix
        size = inFile.readline()
        size = int(size.rstrip('\n'))
        if size == -1:
            return
        print ('The size of the square is: ', size)
        counter += 1
        for i in range(size):
            row_str = inFile.readline()
            row = createRow(row_str)
            matrix.append(row)
        print('***** Square  %d *****' % counter)
        printMatrix(matrix)
        calcAllSum(matrix)
        # Check matrix is magic ?
        if (isMagic(matrix)):
            print ('It is a magic square')
        else:
            print ('It is a normal square')

        print()


main()



