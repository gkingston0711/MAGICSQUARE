
def openCSV(fileName):
    FileOpen = open(fileName,'r')

    for line in FileOpen:
        line = line.rstrip('\n')
        line = line.strip(' ')
        line = line.split()

        print line


def main():

    openCSV('square.txt')



main()
