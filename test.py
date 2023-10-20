from math import fmod
def get_sudoku(width):
    sudoku = []

    numSquares = width**2

    for i in range(0,numSquares):
        row = (i // width)+1 # finds row of current square
        column = int(fmod(i, width)) # find column of current square
        print("DEBUG:\n    row: "+str(row)+"\ncolumn: "+str(column)) #debug: print squares





def main(i, width):
    '''main function
    '''

    get_sudoku(5)


if __name__ == '__main__':
    main(10,9)