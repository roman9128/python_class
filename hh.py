from os import system, name
def clear():
	if name == 'nt':
		_ = system('cls')


table = [[7,8,9],[4,5,6],[1,2,3]]
for i in table:
    print(*i)

while (True):
    x_move = int(input("Куда ходит Х? "))
    if x_move == 7 and table[0][0] == 7:
        table[0][0] = "X"
    elif x_move == 8 and table[0][1] == 8:
        table[0][1] = "X"
    elif x_move == 9 and table[0][2] == 9:
        table[0][2] = "X"
    elif x_move == 4 and table[1][0] == 4:
        table[1][0] = "X"
    elif x_move == 5 == table[1][1]:
        table[1][1] = "X"
    elif x_move == 6 == table[1][2]:
        table[1][2] = "X"
    elif x_move == 1 == table[2][0]:
        table[2][0] = "X"
    elif x_move == 2 == table[2][1]:
        table[2][1] = "X"
    elif x_move == 3 == table[2][2]:
        table[2][2] = "X"
    clear()
    for i in table:
        print(*i)
    o_move = int(input("Куда ходит О? "))
    if o_move == 7:
        table[0][0] = "O"
    elif o_move == 8:
        table[0][1] = "O"
    elif o_move == 9:
        table[0][2] = "O"
    elif o_move == 4:
        table[1][0] = "O"
    elif o_move == 5:
        table[1][1] = "O"
    elif o_move == 6:
        table[1][2] = "O"
    elif o_move == 1:
        table[2][0] = "O"
    elif o_move == 2:
        table[2][1] = "O"
    elif o_move == 3:
        table[2][2] = "O"
    clear()
    for i in table:
        print(*i)