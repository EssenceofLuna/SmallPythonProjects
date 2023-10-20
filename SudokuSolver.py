from math import fmod
def get_sudoku(width):
    sudoku = []

    numSquares = width**2

    for i in range(0,numSquares):
        column = int(fmod(i, width))+1 # finds column (x coord) of current square
        row = (i // width)+1 # finds row (y coord) of current square
        print("DEBUG:\n    column: "+str(column)+"\n    row: "+str(row)) #debug: print squares





def main():
    '''main function
    '''

    get_sudoku(9)


if __name__ == '__main__':
    main()