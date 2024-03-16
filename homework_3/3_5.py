import random
from os import system, name
def clear():
	if name == 'nt':
		_ = system('cls')
		
def print_table(arr):
    clear()
    print("", arr[0],"|", arr[1],"|", arr[2])
    print("───────────")
    print("", arr[3],"|", arr[4],"|", arr[5])
    print("───────────")
    print("", arr[6],"|", arr[7],"|", arr[8])

def is_winner(arr):
    if (arr[0] == arr[1] == arr[2]) and arr[0] != " ":
        print(f"{arr[0]} - winner")
        return True
    elif (arr[3] == arr[4] == arr[5]) and arr[3] != " ":
        print(f"{arr[3]} - winner")
        return True
    elif (arr[6] == arr[7] == arr[8]) and arr[6] != " ":
        print(f"{arr[6]} - winner")
        return True
    elif (arr[0] == arr[3] == arr[6]) and arr[0] != " ":
        print(f"{arr[0]} - winner")
        return True
    elif (arr[1] == arr[4] == arr[7]) and arr[1] != " ":
        print(f"{arr[1]} - winner")
        return True        
    elif (arr[2] == arr[5] == arr[8]) and arr[2] != " ":
        print(f"{arr[2]} - winner")
        return True           
    elif (arr[0] == arr[4] == arr[8]) and arr[0] != " ":
        print(f"{arr[0]} - winner")
        return True           
    elif (arr[2] == arr[4] == arr[6]) and arr[2] != " ":
        print(f"{arr[2]} - winner")
        return True
    return False

def make_x_move(arr, move):
    if move == 7:
        arr[0] = "X"
    elif move == 8:
        arr[1] = "X"
    elif move == 9:
        arr[2] = "X"
    elif move == 4:
        arr[3] = "X"
    elif move == 5:
        arr[4] = "X"
    elif move == 6:
        arr[5] = "X"
    elif move == 1:
        arr[6] = "X"
    elif move == 2:
        arr[7] = "X"
    elif move == 3:
        arr[8] = "X"
    print_table(arr)
    
def make_o_move(arr, move):
    if move == 7:
        arr[0] = "O"
    elif move == 8:
        arr[1] = "O"
    elif move == 9:
        arr[2] = "O"
    elif move == 4:
        arr[3] = "O"
    elif move == 5:
        arr[4] = "O"
    elif move == 6:
        arr[5] = "O"
    elif move == 1:
        arr[6] = "O"
    elif move == 2:
        arr[7] = "O"
    elif move == 3:
        arr[8] = "O"
    print_table(arr)
    
def is_empty(arr, move):
    if (move == 7) and (arr[0] == " "):
        return True
    elif (move == 8) and (arr[1] == " "):
        return True
    elif (move == 9) and (arr[2] == " "):
        return True
    elif (move == 4) and (arr[3] == " "):
        return True
    elif (move == 5) and (arr[4] == " "):
        return True
    elif (move == 6) and (arr[5] == " "):
        return True
    elif (move == 1) and (arr[6] == " "):
        return True
    elif (move == 2) and (arr[7] == " "):
        return True
    elif (move == 3) and (arr[8] == " "):
        return True
    return False

i = 0
table = [" "," "," "," "," "," "," "," "," "]
print_table(table)
while True:
    if is_winner(table) == True:
        break
    if i > 8:
        print("no winner")
        break
    while True:
        x_move = int(input("Куда ходит Х? "))  
        if is_empty(table, x_move) == True:
            make_x_move(table, x_move)
            i += 1
            break
    if is_winner(table) == True:
        break
    if i > 8:
        print("no winner")
        break
    while True:
        o_move = random.randint(1, 9)    
        if is_empty(table, o_move) == True:
            make_o_move(table, o_move)
            i += 1
            break
end = input("Ещё разок?")