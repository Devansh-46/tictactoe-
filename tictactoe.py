dashes = '---------'
cells = dashes + '\n' + ('|' + ' ' * 7 + '|\n') * 3 + dashes
occupied_initial = dict()
field_layout = '_________'
x_turn = True


def outline_fields(string_to_process):
    print(dashes)
    for i in range(3):
        print(('| ' + ' '.join([i for i in string_to_process[i*3:(i+1)*3]]) + ' |').replace('_', ' '))
    print(dashes)


for row in range(1, 4):
    for column in range(1, 4):
        if field_layout[(row - 1) * 3 + column - 1] != '_':
            occupied_initial[f'{row}{column}'] = 'Occupied'
        else:
            occupied_initial[f'{row}{column}'] = 'UNoccupied'


def analyze_the_game_state(correct_inp):
    if correct_inp[0] == correct_inp[3] == correct_inp[6] and correct_inp[1] == correct_inp[4] == correct_inp[7]\
            and correct_inp[0] in 'XO':
        print('Impossible')
        return True
    elif correct_inp[0] == correct_inp[3] == correct_inp[6] and correct_inp[0] in 'XO':
        print(correct_inp[0], 'wins')
        return True
    elif correct_inp[1] == correct_inp[4] == correct_inp[7] and correct_inp[1] in 'XO':
        print(correct_inp[1], 'wins')
        return True
    elif correct_inp[2] == correct_inp[5] == correct_inp[8] and correct_inp[2] in 'XO':
        print(correct_inp[2], 'wins')
        return True
    elif correct_inp[0] == correct_inp[4] == correct_inp[8] and correct_inp[0] in 'XO':
        print(correct_inp[0], 'wins')
        return True
    elif correct_inp[2] == correct_inp[4] == correct_inp[6] and correct_inp[2] in 'XO':
        print(correct_inp[2], 'wins')
        return True
    elif correct_inp[0] == correct_inp[1] == correct_inp[2] and correct_inp[0] in 'XO':
        print(correct_inp[0], 'wins')
        return True
    elif correct_inp[3] == correct_inp[4] == correct_inp[5] and correct_inp[3] in 'XO':
        print(correct_inp[3], 'wins')
        return True
    elif correct_inp[6] == correct_inp[7] == correct_inp[8] and correct_inp[6] in 'XO':
        print(correct_inp[6], 'wins')
        return True
    elif correct_inp.count('X') - correct_inp.count('O') > 1:
        print('''elif correct_inp.count('X') - correct_inp.count('O') > 1:''')
        print('Impossible')
    elif correct_inp.count('O') > correct_inp.count('X'):
        print('''elif correct_inp.count('O') > correct_inp.count('X'):''')
        print('Impossible')
    elif '_' in correct_inp:
        print('Game not finished')
    else:
        print('Draw')
        return True


def enter_coordinates(field_layout_now, occupied, _x_turn):
    coordinates = input('Enter the coordinates: ')
    if len(coordinates) == 3:
        for i in coordinates.split():
            if not i.isdigit():
                print('You should enter numbers!')
                enter_coordinates(field_layout_now, occupied, _x_turn)
                break
            elif int(i) > 3:
                print('Coordinates should be from 1 to 3!')
                enter_coordinates(field_layout_now, occupied, _x_turn)
                break
        else:
            if occupied.get(''.join(coordinates.split())) == 'Occupied':
                print('This cell is occupied! Choose another one!')
                enter_coordinates(field_layout_now, occupied, _x_turn)
            else:
                print('coordinates', coordinates)
                _row = int(coordinates.split()[0])
                _column = int(coordinates.split()[1])
                list_correct_inp = list(field_layout_now)
                index_of_what_to_change = (_row - 1) * 3 + _column - 1
                if index_of_what_to_change < 9:
                    print(_x_turn)
                    list_correct_inp[index_of_what_to_change] = 'X' if _x_turn is True else 'O'
                    new_field_layout = ''.join(list_correct_inp)
                    print(new_field_layout)
                    occupied[''.join(coordinates.split())] = 'Occupied'
                    outline_fields(new_field_layout)
                    _x_turn = False if _x_turn is True else True

                    if analyze_the_game_state(new_field_layout) is True:
                        pass
                    else:
                        enter_coordinates(new_field_layout, occupied, _x_turn)
    else:
        enter_coordinates(field_layout_now, occupied, _x_turn)


outline_fields(field_layout)
enter_coordinates(field_layout, occupied_initial, x_turn)