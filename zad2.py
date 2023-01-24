# крестики нолики


def show():
    for row in field:
        print(*row)
def is_win():
    # строки
    for row in field:
        if all(x == 'X' for x in row) or all(x == 'O' for x in row):
            return True
    # столбцы
    for row in zip(*field):                         # использовали zip
        if all(x == 'X' for x in row) or all(x == 'O' for x in row):
            return True
    # диагонали
    if all([all([field[r][c] == 'X' for c in range(3) if r == c]) for r in range(3)]) \
        or all([all([field[r][c] == 'O' for c in range(3) if r == c]) for r in range(3)]) \
        or all([all([field[r][c] == 'X' for c in range(3) if 2 - r == c]) for r in range(3)]) \
        or all([all([field[r][c] == 'O' for c in range(3) if 2 - r == c]) for r in range(3)]):
            return True
def is_end():
    # ничья
    return all(all(elem != '.' for elem in row) for row in field)
field = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
show()
is_my_turn = True
while not is_win() and not is_end():
    while 1:
        try:
            row, col = map(lambda x: int(x) - 1, input('row col = ').split())        # использовали map, lambda
            if field[row][col] != '.':
                raise ValueError
            else:
                break
        except (IndexError, ValueError):
            print('Incorrect!')
    field[row][col] = 'X' if is_my_turn else 'O'
    show()
    is_my_turn = not is_my_turn
print('GAME OVER')
if is_end():
    print('DRAW')
else:
    print('O' if is_my_turn else 'X', 'is winner')