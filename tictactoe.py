upDownLine ="      |     |     \n"
upDownLine+="  1   |  2  |  3  \n"
upDownLine+=" _____|_____|_____\n"
upDownLine+="      |     |     \n"
upDownLine+="   4  |  5  |  6  \n"
upDownLine+=" _____|_____|_____\n"
upDownLine+="      |     |     \n"
upDownLine+="   7  |  8  |  9  \n"
upDownLine+="      |     |     \n"

matrix =[[1,2,3],[4,5,6],[7,8,9]]

def print_board(upDownLine):
    print (upDownLine)
    return upDownLine

def verify_horizontal_lines(matrix):
    length = len(matrix) -1
    for i in range(0,length):
        if (matrix[i][0]==matrix[i][1]):
            if(matrix[i][0]==matrix[i][2]):
                return True,matrix[i][0]
    return False

def verify_vertical_lines(matrix):
    length = len(matrix) -1
    for i in range(0,length):
        if (matrix[0][i]==matrix[1][i]):
            if(matrix[0][i]==matrix[2][i]):
                return True,matrix[0][i]
    return False

def upDownDiagonal(matrix):
    if(matrix[0][0]==matrix[1][1]):
        if(matrix[0][0]==matrix[2][2]):
            return True,matrix[0][0]
    return False

def downUpDiagonal(matrix):
    if(matrix[0][2]==matrix[1][1]):
        if(matrix[0][2]==matrix[2][0]):
            return True,matrix[0][2]
    return False



def mark_X_or_O(tablero,player,cell):
    symbol = ""
    if(player%2==0):
        symbol="O"
    else:
        symbol="X"
    return tablero.replace(str(cell),symbol),symbol

def findElementInMatrix(matrix,cell,mark):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            if(matrix[i][j]==int(cell)):
                matrix[i][j]=mark
    return matrix



if __name__ == "__main__":
    tablero = print_board(upDownLine)
    matriz = matrix
    endGame = True
    turno=1
    while(endGame):
        print(turno)
        num = input()
        tablero,mark = mark_X_or_O(tablero,turno,num)
        matriz = findElementInMatrix(matriz,num,mark)
        verify_horizontal_lines(matriz)
        # verify_vertical_lines(matriz)
        # upDownDiagonal(matriz)
        # downUpDiagonal(matriz)
        print(tablero)
        turno += 1
        