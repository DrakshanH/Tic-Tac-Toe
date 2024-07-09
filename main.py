def printBoard(x,z):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)

    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---") 
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ") 
    print()


def sum(a, b, c ):
    return a + b + c


def checkWin(x, z):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(x[win[0]], x[win[1]], x[win[2]]) == 3):
            print("X Won the match")
            return 1
        if(sum(z[win[0]], z[win[1]], z[win[2]]) == 3):
            print("O Won the match")
            return 0
    return -1


if __name__ == "__main__":
    xState=[0,0,0,0,0,0,0,0,0]
    zState=[0,0,0,0,0,0,0,0,0]
    turn = 1 # 1 for X 0 for O
    print("Welcome to Tic Tac Toe Game : ")
    print()
    c=0
    while(True):
        printBoard(xState,zState)

        if(turn == 1):
            print("X's chance!")
            value = int(input("please enter a value: "))
            xState[value] = 1
            c=c+1
        else:
            print("O's chance!")
            value = int(input("please enter a value: "))
            zState[value] = 1
            c=c+1
        
        cwin = checkWin(xState, zState)
        if(cwin != -1):
            print("Match over")
            break
        
        if(c==9): # to check if the board is filled nd yet no wins
            print("\nTIE!!")
            print("Match over")
            break
      
        turn = ~turn

