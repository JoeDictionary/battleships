HORIZONTAL = '═'
VERTICAL = '║'
UL_CORNER = '╔'
UR_CORNER = '╗'
DL_CORNER = '╚'
DR_CORNER = '╝'
SHOT = 'x'
SHIP_BODY = '█'
EMPTY = ' '


class Battleship():

    # TODO Move to build method?
    direction_modifiers = {'N': (0, -1), 'S': (
        0, 1), 'E': (1, 0), 'W': (-1, 0)}

    @staticmethod
    def build(head, length, direction):
        body = []
        x_modifier, y_modifier = Battleship.direction_modifiers[direction]
        x_head, y_head = head

        # TODO Use loop or list comprehension?
        for i in range(length):
            x_bodypart = (x_head + x_modifier * i)
            y_bodypart = (y_head + y_modifier * i)
            body.append((x_bodypart, y_bodypart))

        # body = [(x_head + x_modifier * i, y_head + y_modifier * i)
        #         for i in range(length)]
        return body

    def __init__(self, head, length, direction):
        self.body = Battleship.build(head, length, direction)


def render_shots(width, height, shots):
    shots = set(shots)
    print(' ' + UL_CORNER + HORIZONTAL * width + UR_CORNER)

    for y in range(height):
        row = ""
        for x in range(width):
            row += SHOT if (x, y) in shots else ' '
        print(str(y) + VERTICAL + row + VERTICAL)

    print(' ' + DL_CORNER + HORIZONTAL * width + DR_CORNER)


def render_battleships(board_width, board_height, battleships):
    print("-------------")
    # Init empty board
    board = [[EMPTY for _ in range(board_width)] for _ in range(board_height)]

    for ship in battleships:
        for x, y in ship.body:
            board[y][x] = SHIP_BODY

    for row in board:
        print(''.join(row))

    print("-------------")

    # return board


if __name__ == '__main__':

    battleships = [
        Battleship((1, 1), 4, 'S')
    ]

    render_battleships(5, 10, battleships)

    exit(0)

    shots = []
    while True:
        xstr, ystr = input("Shot coordinates:\n").split(',')
        x, y = int(xstr), int(ystr)
        shots.append((x, y))
        render_shots(15, 10, shots)
