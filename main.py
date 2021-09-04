HORIZONTAL = '══'
VERTICAL = '║'
EMPTY = '  '
SHIP_BODY = '██'
NW_CORNER = '╔'  # north-west corner
NE_CORNER = '╗'  # north-east corner
SW_CORNER = '╚'  # south-west corner
SE_CORNER = '╝'  # south-east corner
SHOT = 'x'


class Battleship():

    # TODO Use that (dict with modifiers) or if-elif sequence in build method?
    # TODO Move to build method?
    direction_modifiers = {'n': (0, -1), 's': (
        0, 1), 'e': (1, 0), 'w': (-1, 0)}

    @staticmethod
    def build(head, length, direction):
        body = []
        x_modifier, y_modifier = Battleship.direction_modifiers[direction]
        x_head, y_head = head

        for i in range(length):
            x_bodypart = (x_head + x_modifier * i)
            y_bodypart = (y_head + y_modifier * i)
            body.append((x_bodypart, y_bodypart))

        return body

    def __init__(self, head, length, direction):
        self.body = Battleship.build(head, length, direction)
        self.hits = [False] * len(self.body)


def render_shots(width, height, shots):
    shots = set(shots)
    print(EMPTY + NW_CORNER + HORIZONTAL * width + NE_CORNER)

    for y in range(height):
        row = ""
        for x in range(width):
            row += SHOT if (x, y) in shots else EMPTY
        print(str(y) + VERTICAL + row + VERTICAL)

    print(EMPTY + SW_CORNER + HORIZONTAL * width + SE_CORNER)


def render_battleships(board_width, board_height, ships):
    board = [[EMPTY for _ in range(board_width)]
             for _ in range(board_height)]

    for ship in ships:
        for x, y in ship.body:
            board[y][x] = SHIP_BODY

    print(NW_CORNER + HORIZONTAL * board_width + NE_CORNER)
    for row in board:
        print(VERTICAL + ''.join(row) + VERTICAL)
    print(SW_CORNER + HORIZONTAL * board_width + SE_CORNER)


class Shot():
    def __init__(self, location, is_hit):
        self.location = location
        self.is_hit = is_hit


class GameBoard():

    def __init__(self, width, height, battleships=[], shots=[]):
        self.width = width
        self.height = height
        self.battleships = battleships
        self.shots = shots

    def take_shot(self, shot_location):
        shot_is_hit = None

        for ship in self.battleships:
            if shot_location in ship.body:
                shot_is_hit = True
                hit_index = ship.body.index(shot_location)
                ship.hits[hit_index] = False
            else:
                shot_is_hit = False

        self.shots.append(Shot(shot_location, shot_is_hit))


if __name__ == '__main__':
    battleships = [Battleship((1, 1), 4, 's'), Battleship((3, 5), 2, 'w')]

    render_battleships(15, 15, battleships)
    print(battleships[1].hits)

    exit(0)

    shots = []
    while True:
        xstr, ystr = input("Shot coordinates:\n").split(',')
        x, y = int(xstr), int(ystr)
        shots.append((x, y))
        render_shots(15, 10, shots)
    print(Battleship.build((1, 1), 4, 'N'))
