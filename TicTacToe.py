global field
field = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]


class player1tic:
    x = int(input("Reihe:"))
    y =  int(input("Spalte:"))
    field[x][y]=1
    print(field[x][y])


player1tic()
#scann1(field)
#player2tic(field)
#scann2(field)
