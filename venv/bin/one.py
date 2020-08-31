
def openCSV(fileName):
    FileOpen = open(fileName,'r')



    for line in FileOpen:

        line = line.rstrip('\n')
        line = line.strip(' ')
        line = line.split()

        Length = len(line)
        if Length == 1:
            arr = []





        print line


def main():

    openCSV('square.txt')



main()
