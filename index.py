game_position = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def start():
    inpt = False
    ans = input('Welcome, Player 1! Choose your shot! X or O? ')

    while inpt == False:
        ans_trim = ans.upper().strip()
        if ans_trim == 'X' or ans_trim == 'O':
            return ans_trim
            inpt == True
        else:
            ans = input('Oops, looks like you entered the wrong answer. ' +
                        'Please choose between X and O. ')

def move_forward(n):
    if n == 'X':
        player = 'Player 1'
    else:
        player = 'Player 2'
    
    #display tic-tac-toe; display_game()
    inpt = input(f'{player} goes first! Pick a position to replace 1-9. ')

    while int(inpt) not in game_position:
        inpt = input(f'Pick a position to replace 1-9. ')
    
    continue_game(inpt, player)

def again(answer):
    if answer == 'Y':
        start()
    else:
        return

#main method
def continue_game(n, player):
    #display_updated_game()
    #with initial append + next player; whats next? //////

    #end
    inpt = ''
    while inpt not in ['Y', 'N']:
        inpt = input('Do you want to play again? [Y/N] ').upper().strip()

    again(inpt)


#every after input, check if X has horizontal or vertical X/O.

###Validations###
#bawal na lagyan yung may laman
#notify when theres a winner or tie
#tie if all full
#game reset?

###QUESTIONS###
#how to input if Player 1 is X/O vice versa?

move_forward(start())

def init():
    i, j = 0 
    while i > 3:
        while j > 5:
            modulus = j % 2
            if modulus == 0:
                print('|')
            else:
                print()
    #print lines and initialize list
    #for loop 3 times
        #for loop 5 times
            #if even
                #print |
            #else
                #if 6, 8, 10
                #lagay list
                #else blank
        #endforloop
        #if loop < 2:
            #print ---------
    #endforloop

#func for insert/ask user
