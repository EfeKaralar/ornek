class TicTacToe():

    def main():
         board = {'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}
         boardValues = [[0, 0, 0],[0,0,0],[0,0,0]]
         turn = ['X', 1]
         for i in range(10):
            printBoard(board)
            move(turn, board, boardValues)
            x =  whoWins(boardValues, turn)
            if (x):
                again = input('Play Again (y/n)')
                if again == 'y':
                    resBoard()
                else:
                    quit()

    def resBoard(self):
        board = {'1':' ', '2':' ', '3':' ',
                 '4':' ', '5':' ', '6':' ',
                 '7':' ', '8':' ', '9':' ',
                 }
        boardValues = [[0, 0, 0],[0,0,0],[0,0,0]]
        return board
    def printBoard(board):
        print(board['1'] + '|' + board['2'] + '|' + board['3'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
    def changeTurn(t):
        if t[0] == 'X':
            t[0]='O'
            t[1] = t[1] + 1
            return 'X'
        else:
            t[0]='X'
            t[1] = t[1] + 1
            return 'O'
    def move(turn, board, boardValues):
        print(turn[0] +'\'s turn.')
        tile = input('Where do you want to put your character? [1,9]')
        if board[tile] == ' ':
            board[tile] = turn[0]
            num = int(tile)
            changeBV(num, boardValues, turn)
            changeTurn(turn)
        else:
            print('That place is already filled up.')
    def changeBV(num, boardValues, turn):
        i = round(num/3)-1
        j = (num-1)%3
        if turn[0] == 'X':
            boarboardValues[i][j] = 1
        if turn[0] == 'O':
            boarboardValues[i][j] = -1
    def whoWins(boardValues, turn):
        if turn[1] >= 5:
            i = calculateWinner(boardValues)
            if len(i) == 1:
                print(i + ' WINS!!!')
                return True
            elif turn[1] ==9:
                print('IT\'S A TIE')
                return False

    def calculateWinner(boardValues):
        rowsNcolumns = [0,0,0,0,0,0,0,0]
        rowsNcolumns[0] = boardValues[0][0] + boardValues[0][1] + boardValues[0][2] #FirstRow
        rowsNcolumns[1] = boardValues[1][0] + boardValues[1][1] + boardValues[1][2] #SecondRow
        rowsNcolumns[2] = boardValues[2][0] + boardValues[2][1] + boardValues[2][2] #ThirdRow
        rowsNcolumns[3] = boardValues[0][0] + boardValues[1][0] + boardValues[2][0] #FirstColumn
        rowsNcolumns[4] = boardValues[0][1] + boardValues[1][1] + boardValues[2][1] #SecondColumn
        rowsNcolumns[5] = boardValues[0][2] + boardValues[1][2] + boardValues[2][2] #ThirdColumn
        rowsNcolumns[6] = boardValues[0][0] + boardValues[1][1] + boardValues[2][2] #FirstCross
        rowsNcolumns[7] = boardValues[0][2] + boardValues[1][1] + boardValues[2][0] #SecondCross
        for x in rowsNcolumns
            if x == 3:
                return 'X'
            if x == -3:
                return 'O'
            else:
                return ''

