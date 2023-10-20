from math import fmod
def get_sudoku(width):
    sudoku = []

    numSquares = width**2
    i=0
    while i in range(0,numSquares):
        column = int(fmod(i, width))+1 # finds column (x coord) of current square
        row = (i // width)+1 # finds row (y coord) of current square
        #print("DEBUG:\n    column: "+str(column)+"\n    row: "+str(row)) #debug: print squares
        try:
            print("Enter cell "+str(i)+" ("+str(column)+","+str(row)+")")
            value = input()
            # TODO: add way to go back if an error is made
            #sudoku[i] = [column, row, value]
            
            sudoku.insert(i, [column, row, value])
            i=i+1
        except:
            print("error, invalid input for cell "+str(i)+" ("+str(column)+","+str(row)+")")
            #i = i-1
    
    return sudoku

def print_sudoku(sudoku):
    print("printing current sudoku...")
    for i in range(len(sudoku)):
        print("("+str(sudoku[i][0])+","+str(sudoku[i][1])+") = "+str(sudoku[i][2]))





def main():
    '''main function
    '''

    sud = get_sudoku(3)
    print_sudoku(sud)


if __name__ == '__main__':
    main()