from math import fmod


"""Since starting this project I have realized that my method of storing sudokus was needlessly complicated and needed to be rewritten
my method was to store each cell as a list containing its x and y coordinates and its values
these lists were then stored inside another list, which made actually accessing that information a nightmare

as such i am starting a v2 which will store the board as an object, allowing way smoother access to information and
allow me to manipulate the board via its own functions
"""
def get_sudoku(width):

    numSquares = width**2
    sudoku = [[None]*3]*numSquares
    i=0
    while i in range(0,numSquares):
        column = int(fmod(i, width))+1 # finds column (x coord) of current square
        row = (i // width)+1 # finds row (y coord) of current square
        #print("DEBUG:\n    column: "+str(column)+"\n    row: "+str(row)) #debug: print squares
        try:
            print("Enter cell "+str(i)+" ("+str(column)+","+str(row)+"), or type \"back\"")
            value = input()

            # decide what to do with user input
            if value.isnumeric():
                # number entered: validate data and add
                value = int(value)

                # data validation...
                if value <= width and value > 0:
                    print("DEBUG 1")
                    # check values in sudoku that have same column or row, and if value is the same reject it
                    passed = True
                    indiciesToCheck=[]
                    for j in range(len(sudoku)):
                        """"""
                        if sudoku[j][0] == column or sudoku[j][1] == row:
                            indiciesToCheck.append(j)
                    for j in range(len(indiciesToCheck)):
                        if sudoku[indiciesToCheck[j]][2] == value:
                            passed = False
                    
                    if passed == True:
                        # Data validation succeded
                        sudoku[i] = [column, row, value]
                        i=i+1
                    else:
                        print("error: number already exists in row/column")

                            
                        #if sudoku[][]
                else:
                    # data validation failed
                    print("error, invalid number entered for cell "+str(i)+" ("+str(column)+","+str(row)+")") # TODO: permanent fix for hard coded cell id number
            elif value == "":
                # nothing entered: add None instead
                sudoku[i] = [column, row, value]
                i=i+1
            elif value == "back" and i != 0:
                # 'back' entered: go back to previous
                print("going back...")
                i = i - 1
            else:
                # something else entered: try again
                print("error 1, invalid input for cell "+str(i)+" ("+str(column)+","+str(row)+")")

        except:
            print("error 2, invalid input for cell "+str(i)+" ("+str(column)+","+str(row)+")")
            #i = i-1
    
    return sudoku


def print_sudoku(sudoku):
    print("printing current sudoku...")
    for i in range(len(sudoku)):
        print("("+str(sudoku[i][0])+","+str(sudoku[i][1])+") = "+str(sudoku[i][2]))

def solve_sudoku(sudoku = None):
    if sudoku == None:
        # if no sudoku supplied, get standard 9x9 sudoku board
        sudoku = get_sudoku(9)
    
    # solve sudoku
    solved_sudoku = []




    return solved_sudoku
    






def main():
    '''main function
    '''

    sud = get_sudoku(9)
    print_sudoku(sud)


if __name__ == '__main__':
    main()