HORIZONTAL = '═'
VERTICAL = '║'
UL_CORNER = '╔'
UR_CORNER = '╗'
DL_CORNER = '╚'
DR_CORNER = '╝'
SHOT = 'x'


class Battleship():

    # TODO Move to build method?
    direction_modifiers = {'N': (0, 1), 'S': (
        0, -1), 'E': (-1, 0), 'W': (1, 0)}

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
    # while True:
    #     xstr, ystr = input("Shot coordinates:\n").split(',')
    #     x, y = int(xstr), int(ystr)
    #     shots.append((x, y))
    #     render_box(15, 10, shots)
    print(Battleship.build((1, 1), 4, 'N'))
