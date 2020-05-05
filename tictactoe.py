upDownLine ="      |     |     \n"
upDownLine+="   1  |  2  |  3  \n"
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
    length = len(matrix) 
    for i in range(0,length):
        if (matrix[i][0]==matrix[i][1]):
            if(matrix[i][0]==matrix[i][2]):
                return True
    return False

def verify_vertical_lines(matrix):
    length = len(matrix)
    for i in range(0,length):
        if (matrix[0][i]==matrix[1][i]):
            if(matrix[0][i]==matrix[2][i]):
                return True
    return False

def upDownDiagonal(matrix):
    if(matrix[0][0]==matrix[1][1]):
        if(matrix[0][0]==matrix[2][2]):
            return True
    return False

def downUpDiagonal(matrix):
    if(matrix[0][2]==matrix[1][1]):
        if(matrix[0][2]==matrix[2][0]):
            return True
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

def any_winner(winner,turno):
    if(winner):
        if(turno%2!=0):
            print("Gana el jugador 1 (X)")
            return True
        else:
            print("Gana el jugador 2 (O)")
            return True

def verify_any_winner(matriz,turno):
    list_verificados =[]
    list_verificados.append(verify_horizontal_lines(matriz))
    list_verificados.append(verify_vertical_lines(matriz))
    list_verificados.append(upDownDiagonal(matriz))
    list_verificados.append(downUpDiagonal(matriz))
    for i in range(0,len(list_verificados)):
        if (any_winner(list_verificados[i],turno)):
            return False
    return True


def determinar_jugador(turno):
    if(turno%2!=0):
        return "Turno Jugador 1 (X): "
    else:
        return "Turno Jugador 2 (O): "



if __name__ == "__main__":
    tablero = print_board(upDownLine)
    matriz = matrix
    playGame = True
    turno=1
    while(playGame):
        num = input(determinar_jugador(turno))
        tablero,mark = mark_X_or_O(tablero,turno,num)
        print(tablero)
        matriz = findElementInMatrix(matriz,num,mark)
        playGame = verify_any_winner(matriz,turno)
        turno += 1

        