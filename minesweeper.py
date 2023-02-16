'''
############################################################################################
####    MIT License                                                                     ####
####                                                                                    ####
####    Copyright (c) 2023 marcoserrano1980                                             ####
####                                                                                    ####
####    Permission is hereby granted, free of charge, to any person obtaining a copy    ####
####    of this software and associated documentation files (the "Software"), to deal   ####
####    in the Software without restriction, including without limitation the rights    ####
####    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell       ####
####    copies of the Software, and to permit persons to whom the Software is           ####
####    furnished to do so, subject to the following conditions:                        ####
####                                                                                    ####
####    The above copyright notice and this permission notice shall be included in all  ####
####    copies or substantial portions of the Software.                                 ####
####                                                                                    ####
####    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR      ####
####    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,        ####
####    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE     ####
####    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER          ####
####    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,   ####
####    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE   ####
####    SOFTWARE.                                                                       ####
####                                                                                    ####
####    Developed by Marco Serrano                                                      ####
####    https://www.linkedin.com/in/marco-alexandre-serrano                             ####
####    https://github.com/marcoserrano1980                                             ####
####    marco.a.s.serrano@gmail.com                                                     ####
####                                                                                    ####
############################################################################################

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
clear_spot = []
flaged_spot = []
board_size = 0
remaining_spots = 0
number_of_mines = 0
coordinate_error = False
play_again = False

def cls():
    # Clears the screen in Windows and Linux systems
    pass

def validate_numeric():
    # Requests a numeric input from the user
    # If the input is numeric, returns the value
    # Otherwise, returns an error message and requests a numeric value
    pass

def game_start():
    # Requests game options from the player
    # Validates the board size input
    # If the input is valid, requests the amount of mines
    # If the input is valid, calls the "mine_coordinates()" function to generate the game 2d array
    pass

def game_header():
    # Generates a header for the game
    # Prints the total number of mines, remaining spots, clear spots, and flagged spots
    pass

def mine_coordinates():
    # Generates the game board with mines and their respective numbers
    # Returns the board as a 2d list
    pass

def open_coordinates():
    # Validates and checks the given coordinates
    # Converts the alphabet coordinate to its corresponding numeric value using the "alphabet" list
    # If the input is valid, returns the selected coordinate as a list [row, column]
    # Otherwise, returns an error message
    pass

def player_options():
    # Shows the main menu for the player's coordinates and the option to exit the game
    # Returns the player's option
    pass

def select_action():
    # Controls the player's options for the selected field
    # Shows the options for cleaning, flagging, unflagging, and leaving the field
    # If the input is valid, executes the selected option
    # Otherwise, returns an error message
    pass

def board():
    # Generates the game board
    # Returns the board as a string
    pass

def game_over():
    # Generates an open game board and shows the mines' locations
    # Returns the board as a string
    pass

'''

# import modules
import random
import re
import os

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'] # alphabet list to help coordinates A1, B2........
clear_spot = [] # open column
flaged_spot = [] # flaged column

board_size = 0 # board size
remening_spots = 0 #number of fields
number_of_mines = 0 # select number of mines 
coordinate_error = 0 # error status

play_again = False # control loop on end of game

# clear screen on windows and lixux systems
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Collect and validate the user's numeric data
def validate_numeric(message):
    # Use the loop to validate the  data, exit from loop when received a valid data
    while True:
        user_input = input(message) # input data
        # Validate numeric decima from 0 to 9 and .
        if len(re.sub("[0-9]", '', user_input)) == 0 and user_input != "":
            return int(user_input)
        else:
            cls()
            print("\tInvalid characters, use numbers only!")

# set board size and number of mines
def game_strat():
    
    global board_size
    global number_of_mines
    global remening_spots
    
    while True:
        # request board size
        board_size = validate_numeric("\t\033[91mPlease insert board size [6 to 12] :")
        # check if board size is valid
        if board_size > 5 and board_size < 13:
            # choise amount of mines over 10 mines and less than 50% of board  
            while True:
                # request number of mines
                number_of_mines = validate_numeric(f"\tPlsease select number of mines [{int(board_size*board_size*0.20)} to {int(board_size*board_size*0.5)}] :")
                if number_of_mines > int(board_size*board_size*0.20)-1 and number_of_mines < int(board_size*board_size*0.5)+1:
                    break
                else:
                    # ivalide amount, error message
                    cls()
                    print(f"\tPlease insert board size [6 to 12] : {board_size}")
                    print(f"\t{number_of_mines} is a invalid value")
            # create a minefield 2d array with random positions
            mine_coordinates(number_of_mines)
            remening_spots = board_size*board_size
            break
        else:
            # error on board size
            cls()
            print(f"{board_size} is a invalid value")       

# generate game header
def game_header():
    # format header 
    line = f"\tTotal of mines : {number_of_mines}\n"
    line += f"\tRemening spots: {remening_spots-len(flaged_spot)}\n"
    line += f"\tClear stpots: {len(clear_spot)}\n"
    line += f"\tFlaged spots: {len(flaged_spot)}\n"
    # return header
    return line
  
# generates a randon coordinates
def mine_coordinates(number_of_mines):

    global board_positions # create a global list
    board_positions = []
    
    # generate mines on randon coordinates
    while number_of_mines > 0:
    
        # prepare a temporary array (second level)
        if len(board_positions) < board_size:
            temp = []
            for x in range(0, board_size):
                # if random number is 10, 10 = mine
                if random.randint(0,10) == 10:
                    temp.append(10)
                    number_of_mines -= 1
                else:
                    temp.append(0)
            # save second array into main array
            board_positions.append(temp)        
        else:
            # adding remaning mines into arrays
            for i in range(0, board_size):
                for x in range(0, board_size):
                    # if random number is 10, 10 = mine
                    if random.randint(0,10) == 10 and board_positions[i][x] < 10 and number_of_mines > 0:
                        board_positions[i][x] = 10
                        number_of_mines -= 1 
                    
        # process mine count after all mines are in place
        if number_of_mines == 0:
            for row in range(0, board_size):
                for columns in range(0, board_size):
                
                    # process first row level of board
                    if row == 0:                    
                        # process the first column
                        if columns == 0 and board_positions[row][columns] == 10:
                            # process right column of mine on is row
                            if board_positions[row][columns+1]  != 10:                                            
                                board_positions[row][columns+1] += 1
                            # process some column number on next row
                            if board_positions[row+1][columns]  != 10:                                            
                                board_positions[row+1][columns] += 1                             
                            # process right column of mine on next row
                            if board_positions[row+1][columns+1]  != 10:                                            
                                board_positions[row+1][columns+1] += 1                                               
                        elif columns > 0 and columns < (board_size - 1) and board_positions[row][columns] == 10:
                            # process left column of mine on is row
                            if board_positions[row][columns-1]  != 10:                                               
                                board_positions[row][columns-1] += 1
                                # process right column of mine on is row
                            if board_positions[row][columns+1]  != 10:                                            
                                board_positions[row][columns+1] += 1
                            # process left column of mine on next row
                            if board_positions[row+1][columns-1]  != 10:                                               
                                board_positions[row+1][columns-1] += 1
                            # process some column number on next row
                            if board_positions[row+1][columns]  != 10:                                            
                                board_positions[row+1][columns] += 1                             
                            # process right column of mine on next row
                            if board_positions[row+1][columns+1]  != 10:                                            
                                board_positions[row+1][columns+1] += 1                            
                        # process last column on first row
                        elif board_positions[row][columns] == 10:
                            # process left column of mine on is row
                            if board_positions[row][columns-1]  != 10:                                               
                                board_positions[row][columns-1] += 1
                            # process left column of mine on next row
                            if board_positions[row+1][columns-1]  != 10:                                               
                                board_positions[row+1][columns-1] += 1
                            # process some column number on next row
                            if board_positions[row+1][columns]  != 10:                                            
                                board_positions[row+1][columns] += 1                               
                    
                    # process last row level of board
                    elif row == (board_size-1):                    
                        # process the first column
                        if columns == 0 and board_positions[row][columns] == 10:
                            # process right column of mine on is row
                            if board_positions[row][columns+1]  != 10:                                            
                                board_positions[row][columns+1] += 1
                            # process some column number on previous row
                            if board_positions[row-1][columns]  != 10:                                            
                                board_positions[row-1][columns] += 1                             
                            # process right column of mine on previous row
                            if board_positions[row-1][columns+1]  != 10:                                            
                                board_positions[row-1][columns+1] += 1                                               
                        elif columns > 0 and columns < (board_size - 1) and board_positions[row][columns] == 10:
                            # process left column of mine on is row
                            if board_positions[row][columns-1]  != 10:                                               
                                board_positions[row][columns-1] += 1
                                # process right column of mine on is row
                            if board_positions[row][columns+1]  != 10:                                            
                                board_positions[row][columns+1] += 1
                            # process left column of mine on previous row
                            if board_positions[row-1][columns-1]  != 10:                                               
                                board_positions[row-1][columns-1] += 1
                            # process some column number on previous row
                            if board_positions[row-1][columns]  != 10:                                            
                                board_positions[row-1][columns] += 1                             
                            # process right column of mine on previous row
                            if board_positions[row-1][columns+1]  != 10:                                            
                                board_positions[row-1][columns+1] += 1                            
                        
                        # process last column 
                        elif board_positions[row][columns] == 10:
                            # process left column of mine on is row
                            if board_positions[row][columns-1]  != 10:                                               
                                board_positions[row][columns-1] += 1
                            # process left column of mine on previous  row
                            if board_positions[row-1][columns-1]  != 10:                                               
                                board_positions[row-1][columns-1] += 1
                            # process some column number on previous row
                            if board_positions[row-1][columns]  != 10:                                            
                                board_positions[row-1][columns] += 1  

                    # process middle rows of board
                    else:
                       # process the first column
                        if columns == 0 and board_positions[row][columns] == 10:
                            # process right column of mine on is row
                            if board_positions[row][columns+1]  != 10:                                            
                                board_positions[row][columns+1] += 1
                            # process some column number on previous row
                            if board_positions[row-1][columns]  != 10:                                            
                                board_positions[row-1][columns] += 1                             
                            # process right column of mine on previous row
                            if board_positions[row-1][columns+1]  != 10:                                            
                                board_positions[row-1][columns+1] += 1    
                            # process some column number on next row
                            if board_positions[row+1][columns]  != 10:                                            
                                board_positions[row+1][columns] += 1                             
                            # process right column of mine on next row
                            if board_positions[row+1][columns+1]  != 10:                                            
                                board_positions[row+1][columns+1] += 1  
                        
                        # process middle columns
                        elif columns > 0 and columns < (board_size - 1) and board_positions[row][columns] == 10:
                            # process left column of mine on is row
                            if board_positions[row][columns-1]  != 10:                                               
                                board_positions[row][columns-1] += 1
                                # process right column of mine on is row
                            if board_positions[row][columns+1]  != 10:                                            
                                board_positions[row][columns+1] += 1
                            # process left column of mine on previous row
                            if board_positions[row-1][columns-1]  != 10:                                               
                                board_positions[row-1][columns-1] += 1
                            # process some column number on previous row
                            if board_positions[row-1][columns]  != 10:                                            
                                board_positions[row-1][columns] += 1                             
                            # process right column of mine on previous row
                            if board_positions[row-1][columns+1]  != 10:                                            
                                board_positions[row-1][columns+1] += 1
                            #process left column of mine on next row
                            if board_positions[row+1][columns-1]  != 10:                                               
                                board_positions[row+1][columns-1] += 1
                            # process some column number on next row
                            if board_positions[row+1][columns]  != 10:                                            
                                board_positions[row+1][columns] += 1                             
                            # process right column of mine on next row
                            if board_positions[row+1][columns+1]  != 10:                                            
                                board_positions[row+1][columns+1] += 1
                        
                        # process last column
                        elif board_positions[row][columns] == 10:
                            # process left column of mine on is row
                            if board_positions[row][columns-1]  != 10:                                               
                                board_positions[row][columns-1] += 1
                            # process left column of mine on previous  row
                            if board_positions[row-1][columns-1]  != 10:                                               
                                board_positions[row-1][columns-1] += 1
                            # process some column number on previous row
                            if board_positions[row-1][columns]  != 10:                                            
                                board_positions[row-1][columns] += 1  
                            # process left column of mine on next  row
                            if board_positions[row+1][columns-1]  != 10:                                               
                                board_positions[row+1][columns-1] += 1
                            # process some column number on next row
                            if board_positions[row+1][columns]  != 10:                                            
                                board_positions[row+1][columns] += 1   
                                
# check cordenates   
def open_coordinates(user_input):
    # global variables to be used out of this function
    global coordinate_error
    global selected_coordinate
    
    # validate alphabet cordenater and convert to numeric by array key (row)
    if user_input[0].upper() in alphabet: 
        # verify if column is a numeric
        if user_input[1:].isnumeric() == True:
            row = alphabet.index(user_input[0].upper())
            column = int(user_input[1:])-1 # add the numeric cordenator (column)
            # validate cordenation
            if row < board_size and column < board_size and column >= 0:
                selected_coordinate = [row, column]
            else:
                coordinate_error = 1 # set error
        else:
            coordinate_error = 1 # set error
    else:
        coordinate_error = 1 # set error

# validate game main menu
def player_options():
    while True:
        player_input = input("\tPlease enter the desired coordinate eg [A1, C5, ...] or 'q' to exit from game: ")
        # check if value is empty
        if player_input.replace(" ", "") == "":
            display()
            print("\tInvalid value")
        else:
            # return value
            return player_input
            

# select action [clear, falag or unflag]
def select_action():
    while True:
        my_action = input('''\tPlease select your action,\n 
            c) 'clean'  - to show field
            f) 'flag'   - to flag field
            u) 'unflag' - to remove flag from field
            l) 'leave'  - to leave this field 
            option: ''')
        # check if value is valid
        if my_action.lower() == "c" or  my_action.lower() == "f" or  my_action.lower() == "u" or  my_action.lower() == "clean" or my_action.lower() == "flag" or my_action.lower() == "unflag":
            # select flag option
            if my_action.lower() == "f" or my_action.lower() == "flag":
                if str(selected_coordinate[0])+","+str(selected_coordinate[1]) in flaged_spot:
                    # flag message
                    display()
                    print("\tThis field is alredy flaged")
                else:
                    # add flag
                    flaged_spot.append(str(selected_coordinate[0])+","+str(selected_coordinate[1]))
                    return my_action[0].lower()
            
            elif my_action.lower() == "c" or my_action.lower() == "clean":
                # verify if field are flaged
                if str(selected_coordinate[0])+","+str(selected_coordinate[1]) in flaged_spot:
                    cls()
                    display()
                    print("\tThis field is flaged do you need unflag before clean")
                else:
                    # return value 'c' to clean field
                    return my_action[0].lower()
            
            elif my_action.lower() == "u" or my_action.lower() == "unflag":
                # remove flag
                flaged_spot.remove(str(selected_coordinate[0])+","+str(selected_coordinate[1]))
                cls()
                display()
                print("\tThis field is unflaged")
                    
        elif my_action.lower() == "l" or  my_action.lower() == "leave":
                return my_action[0].lower() 
        else:
            display()
            print("\tInvalid option")
            
# generates and managmen a board game
def board():
    sq1 = "\t+------"
    sq2 = "\t|******"
    sq3 = "\t|      "
    sq4 =  " "
    
    # generate a graphic board
    line = ""
    for i in range(0, board_size):
        
        # top line
        line += sq1*board_size+"+\n"
        line += "\t"
        for x in range(0, board_size):
            # on clean field
            if str(i)+","+str(x) in clear_spot:
                if x < (board_size -1):
                    line += "|       "
                else:
                    line += "|      "
            elif str(i)+","+str(x) in flaged_spot: # on flaged
                if x < (board_size -1):
                    line += "|///////"
                else:
                    line += "|//////"
            else: # on start
                if x < (board_size -1):
                    line += "|*******"
                else:
                    line += "|******"
                
        # middle line
        line += "|\n\t"
        for x in range(0, board_size):
            # on clean field
            if str(i)+","+str(x) in clear_spot and  x < (board_size-1):
                line += "|"+sq4*3+ str(board_positions[i][x])+ sq4*(4- len(str(board_positions[i][x])))
            elif str(i)+","+str(x) in clear_spot:
                line += "|"+sq4*3+ str(board_positions[i][x])+ sq4*(3- len(str(board_positions[i][x])))
            elif x < (board_size-1): # on strat
                field_id = alphabet[i]+str(x+1)
                line += "|"+sq4*2+ field_id + sq4*(5- len(field_id))
            else:
                field_id = alphabet[i]+str(x+1)
                line += "|"+sq4*2+ alphabet[i]+str(x+1)+ sq4*(4- len(field_id))
        
        # bottom line  
        line += "|\n\t"
        for x in range(0, board_size):
            # on clean field
            if str(i)+","+str(x) in clear_spot:
                if x < (board_size -1):
                    line += "|       "
                else:
                    line += "|      "
            elif str(i)+","+str(x) in flaged_spot: #on flag field
                if x < (board_size -1):
                    line += "|///////"
                else:
                    line += "|//////"
            else:
                if x < (board_size -1): # on strat
                    line += "|*******"
                else:
                    line += "|******"
        line += "|\n"
    line += sq1*board_size+"+\n"
    return line

# generate a clear menu after game is over
def game_over():
    sq1 = "\t+------"
    sq2 = "\t|######"
    sq3 = "\t|      "
    sq4 =  " "
    # create a board
    line = ""
    for i in range(0, board_size):
    
        # top line
        line += sq1*board_size+"+\n"
        line += "\t"
        for x in range(0, board_size):
            if x < (board_size-1):
                if board_positions[i][x] == 10: # field with mine
                    line += "|#######"
                else:
                    line += "|       " # clean field
            else:
                if board_positions[i][x] == 10:
                    line += "|######"
                else:
                    line += "|      " 
        # middle line
        line += "|\n\t"
        for x in range(0, board_size):
            if x < (board_size-1):         
                if board_positions[i][x] == 10:
                    line += "|#######"
                elif board_positions[i][x] > 0:
                    line += "|"+sq4*3+ str(board_positions[i][x])+ sq4*(4- len(str(board_positions[i][x]))) # number of mines on close field
                else:
                    line += "|       "
            else:
                if board_positions[i][x] == 10:
                    line += "|######"
                elif board_positions[i][x] > 0:
                    line += "|"+sq4*3+ str(board_positions[i][x])+ sq4*(3- len(str(board_positions[i][x]))) # number of mines on close field
                else:
                    line += "|      "        
        # bottom line
        line += "|\n\t"
        for x in range(0, board_size):
            if x < (board_size-1):       
                if board_positions[i][x] == 10:
                    line += "|#######"
                else:
                    line += "|       "
            else:
                if board_positions[i][x] == 10:
                    line += "|######"
                else:
                    line += "|      "
        line += "|\n"
    line += sq1*board_size+"+\n"
    # return board
    return line

# main display
def display():
    cls()
    #print("\n".join(map(str, board_positions))+"\n") # just to test - print array
    #print(clear_spot) # just to test - print array
    #print(flaged_spot) # just to test - print array
    print(game_header())
    print(board())

# exit from game
def exit_():
    cls()
    print("\n\33[97mThanks for playing minesweeper, this game has been developed by Marco Serrano - Good bye!")
    exit()
 
# clean screen
cls()

# starts game
while True:
    game_strat()
    
    # Starts game
    while True:
        #show game display
        display()
           
        if coordinate_error == 1:
            print("\tInvalid coordinate") # error message
            coordinate_error = 0 # clear error
            
        # user inputs
        while True:
            user_input = player_options()
            # user can type 'q' to exit from game
            if user_input.lower() == "q":
                exit_()
            else:
                open_coordinates(user_input)
                # check if coordinate is correct
                if coordinate_error == 1:
                    break # out from process if any error on cordenate
                else:
                    display()
                    # select if it's to clear spot or flaged
                    action = select_action()
                    #break
                        
                # if user clear a spot with number "10" 10 reprecentes a mine, game over      
                if action == "c" and board_positions[selected_coordinate[0]][selected_coordinate[1]] == 10:
                    # clear screen a show game over screen
                    cls()
                    print(game_header()) # show header 
                    print(game_over()) # show all board
                    while True:
                        # show game over message and request next step (play again or exit)
                        option = input("\tBUM!!\n\tGAME OVER! - Please type 'a' to play again or 'q' to exit: ")
                        # exit from game
                        if option.lower() == "q":
                            exit_()
                        elif option.lower() == "a":
                            play_again = True # set to play again
                            clear_spot.clear() # clear list
                            flaged_spot.clear() # clear list
                            break
                        else:
                            # show error on option
                            cls()
                            print(game_header())
                            print(game_over())
                            print("\tInvalid option")
                elif action == "c":
                    clear_spot.append(str(selected_coordinate[0])+","+str(selected_coordinate[1])) # add to clear list
                    remening_spots -= 1 # remaning fields
                      
                    #Check if remening filds it's = number of mines
                    if remening_spots == number_of_mines:
                        cls()
                        print(game_header())
                        print(game_over())
                        while True:
                            # show winning message and give optios, new game or exit
                            winner_option = input("\tCongratulations you win this game\n\tPlease type 'a' to play again or 'q' to exit: ")
                            # exit from game
                            if winner_option.lower() == "q":
                                exit_()
                            elif winner_option.lower() == "a":
                                play_again = True # set to play again
                                clear_spot.clear() # clear list
                                flaged_spot.clear() # clear list
                                break
                            else:
                                cls()
                                print(game_header())
                                print(game_over())
                                print("\tInvalid option")
                    else:
                        display()                      
                elif action == "f":
                    display()
                elif action == "l":
                    break
                
            if play_again == True:
                break
                    
        # prepare next game
        if play_again == True:
            play_again = False
            break
