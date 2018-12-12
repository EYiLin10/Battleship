"""
Created on Sun Oct 21 17:40:08 2018

@author: YiLin
"""

from random import randint

#define constants
ROWS = 20           #number of rows
COLS = 60           #number of columns
BEG = 80            #beginner
INT = 50            #intermediate
ADV = 20            #advance
SHIPLENGTH = 5      #length of a ship

#initializing variables
difficulty = 0
boom = 15 
ships = 0
correct_guess = 0

#player board
board = []
for i in range(ROWS):
    board.append(["#"] * COLS)

#genearate ship board                  
ship_board = []
for i in range(ROWS):
    ship_board.append(["#"] * COLS)

def print_board(board):
    
    #print the first line of the map
    print("    ", end = "")
    for i in range(6):
        print("         " + str(i+1), end = "")       
    print("\n", end = "")

    #print the column number
    print("    ", end = "")
    for i in range(60):
        print((i+1)%10, end = "")
    print("\n", end = "")

    for (i, row) in enumerate(board, start = 1):
        if i <= 9:
            print("", i, " ", end = "")
        else:
            print(i, " ", end = "")
        print(("").join(row))
     
    print(" ")
    #to check if board is a 2D list 
    #print(board)
    #print(board[1])
    #print(board[1][1])
    return

#start game		
print("-----------------------------Start-----------------------------")
print("You have total 15 booms. Each ship is of 5 char long." + "\n")	

#choose difficulty level
def get_diff_level():
    
    print("Level of Difficulty: " + "\n" + "1 - Beginner (80 Ships)" + 
          "\n" + "2 - Intermediate (50 Ships)" + "\n" + "3 - Advance (20 Ships)")
    
    while(True):
        try:
            diff = int(input("Please input your option: "))
        except ValueError:
            print("Please input an integer.")
            continue
        else:
            if diff < 1 or diff > 3:
                print ("Meh, invalid option. Please try again.")
            else:
                return diff

difficulty = get_diff_level()

#map difficulty level to number of ships
def set_number_of_ships(diff):
    
    if diff == 1:
        ships = BEG
    elif diff == 2:
        ships = INT
    else:
        ships = ADV

    #print("Number of ships to be generated: " + str(ships))
    return ships

ships = set_number_of_ships(difficulty)
print_board(board)

#generate random row number
def random_row(board):
    return randint(0, len(board) - 1)

#generate random column number
def random_col(board):
    return randint(0, len(board[0]) - 6)

#generate ship
def generate_ship(ship_board):
    
    ship_row_sp = random_row(board)
    ship_col_sp = random_col(board)
    
    previous_col = ship_col_sp-1
    after_col = ship_col_sp+5
    #print("Random generated start point: " + str(ship_row_sp) + ", " + str(ship_col_sp))
    
    if (ship_board[ship_row_sp][previous_col] == "O") or (ship_board[ship_row_sp][after_col] == "O"):
        return False

    for i in range (SHIPLENGTH):
        if ship_board[ship_row_sp][ship_col_sp+i] == "O":
            return False
        else:
            continue
                       
    for i in range(SHIPLENGTH):
            ship_board[ship_row_sp][ship_col_sp+i] = "O"
            
    return True

#generate ships
def generate_ships(ship_board):

    generated = 0
    
    #print_board(ship_board)
    
    while (generated != ships):
        if generate_ship(ship_board) == True:
            generated += 1
        #print("Generated: " + str(generated))
        #print_board(ship_board)

generate_ships(ship_board)
#print("This is ship_board.")
#print_board(ship_board)

#main 
for turn in range(15):
    
    print("Boom(s) left: " + str(boom))
    
    while(True):
        try:
            guess_row = int(input("Guess Row: ")) - 1
        except ValueError:
            print("Not an integer.")
            continue
        else:
            break
    
    while(True):
        try:
            guess_col = int(input("Guess Col: ")) - 1
        except ValueError:
            print("Not an integer.")
            continue
        else:
            break
        
    print()

    #input range checking
    if (guess_row < 0 or guess_row > 19) or (guess_col < 0 or guess_col > 59):
        print("Meh, out of range." + "\n")
    
    #made a correct guess, unmask the ship
    elif ship_board[guess_row][guess_col] == "O":
        board[guess_row][guess_col] = "O"
        correct_guess += 1
        print("Congratulations! You found a ship!" + "\n")
        for i in range (SHIPLENGTH-1):
            if ship_board[guess_row][guess_col-i-1] == "O":
                board[guess_row][guess_col-i-1] = "O"
            if ship_board[guess_row][guess_col+i+1] == "O":
                board[guess_row][guess_col+i+1] = "O"
        #print_board(board)
    else:        
        if(board[guess_row][guess_col] == " "):
            print("You guessed that one already." + "\n")
        else:
            print("Missed, please try again." + "\n")
            board[guess_row][guess_col] = " "
        
    #player unable to destroy 5 ships after 15 trials
    if turn == 14 and correct_guess < 6:
        print ("You’ve no luck today, try again." + "\n")
        
    turn += 1
    boom -= 1
    print_board(board)

    if correct_guess > 4:
        break

if correct_guess > 4:
    print("Congrats! You have destroyed " + str(correct_guess) + " ships.")
    print("Total attempts: " + str(turn))
    if turn < 10:
        print("You have the talent!")
    elif turn > 10 and turn < 12:
        print("Not too bad.")
    else:
        print("You are a novice.")

while(True):
    answer = input("Do you wish to reveal the ship map? (y/n): ")
    if answer == "y":
        print_board(ship_board)
        break
    elif answer == "n":
        break
    else:
        print("Please input either y or n")
        continue
    
print("Thank you for playing! Hope you have enjoyed!")