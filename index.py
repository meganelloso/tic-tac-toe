game_position = [''] * 9

def start():
    game_position = [''] * 9

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

def display_board():
    i, j, k = 0, 0, 0
    while i < 3:
        if i == 1:
            j = 3
        elif i == 2:
            j = 6
        
        print(f' {game_position[j]} | {game_position[j + 1]} | {game_position[j + 2]} ')

        if i < 2:
            print('--------')
        
        i += 1

def player_input(n):
    finish = False

    if n == 'X':
        player = 'Player 1'
    else:
        player = 'Player 2'
    
    display_board()
    inpt = int(input(f'{player} goes first! Pick a position to replace 1-9. '))

    while inpt > len(game_position) or inpt == 0:
        inpt = int(input('Invalid number. Pick a position to replace 1-9. '))

    while finish == False:
        next_op = place_marker(inpt, n)
        n = next_op
        check = win_check()
        display_board()

        if check == 'C' and next_op != 'T':
            inpt = int(input(f'Its {next_op}s turn. Pick a position between 1 - 9 to place {next_op} '))
        elif next_op == 'T':
            inpt = int(input('Im sorry. The position you picked is already filled. Pick another number. '))
        elif check == 'F':
            ask = input('Looks like its a draw. Want to play again? ')
            finish = True
        elif check == 'X' or check == 'O':
            ask = input(f'{check} won! Want to play again? ')
            finish = True
        
    while ask.upper().strip() not in ['Y', 'N']:
        inpt = input('Do you want to play again? [Y/N] ').upper().strip()

    if ask == 'Y':
        game_position.clear()
        start()
    else:
        return 'T'

def place_marker(inpt, n):
    indx = inpt - 1

    if(game_position[indx] == ''):
        game_position[indx] = n
        
        if n == 'X':
            n = 'O'
        else: n = 'X'

        return n
    else:
        return 'T' #try again 


def win_check():
    i, j, k, var = 0, 0, 0, 0

    while i < len(game_position):
        if game_position[i] != '':
            var = game_position[i]
            if i == 0:
                if (var == game_position[1] and var == game_position[2]) \
                or (var == game_position[3] and var == game_position[6]) \
                or (var == game_position[4] and var == game_position[8]):
                    j = 1
                    break
            elif i == 1:
                if (var == game_position[4] and var == game_position[7]):
                    j = 1
                    break
            elif i == 2:
                if (var == game_position[5] and var == game_position[8]) \
                or (var == game_position[4] and var == game_position[6]):
                    j = 1
                    break
            elif i == 3:
                if (var == game_position[4] and var == game_position[5]):
                    j = 1
                    break
            elif i == 6:
                if (var == game_position[7] and var == game_position[8]):
                    j = 1
                    break
        else: k += 1
        i += 1
    if j == 1:
        return var
    elif i == 9 and j == 0 and k > 0:
        return 'C' #continue game 
    elif i == 9 and j == 0 and k == 0:
        return 'F' #full and no one won

player_input(start())
