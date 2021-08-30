HORIZONTAL = '═'
VERTICAL = '║'
UL_CORNER = '╔'
UR_CORNER = '╗'
DL_CORNER = '╚'
DR_CORNER = '╝'
SHOT = '╳'


class Battleship():

    dir_modifiers = {'N': (0, 1), 'S': (0, -1), 'E': (-1, 0), 'W': (1, 0)}

    @staticmethod
    def build(head, length, direction):
        body = []

        for i in range(length):
            pass

    def __init__(self, body):
        self.body = body


def render_box(width, height, shots):
    shots = set(shots)
    print(' ' + UL_CORNER + HORIZONTAL * width + UR_CORNER)

    for y in range(height):
        row = ""
        for x in range(width):
            row += SHOT if (x, y) in shots else ' '
        print(str(y) + VERTICAL + row + VERTICAL)

    print(' ' + DL_CORNER + HORIZONTAL * width + DR_CORNER)


if __name__ == '__main__':
    shots = []
    while True:
        xstr, ystr = input("Shot coordinates:\n").split(',')
        x, y = int(xstr), int(ystr)
        shots.append((x, y))
        render_box(15, 10, shots)
