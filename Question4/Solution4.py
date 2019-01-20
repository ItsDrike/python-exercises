class DirectionError(Exception):
    def __init__(self, message):
        super().__init__(message)


def main(instructions):
    x = 0
    y = 0
    for instruction in instructions:
        try:
            direction = instruction.split()[0].upper()
            length = instruction.split()[1]
        except IndexError as e:
            if len(instruction) > 0:
                direction = instruction.split()[0].upper()
                if direction == 'STOP':
                    return x, y
                else:
                    raise DirectionError(f'Specified direction: {direction} does not have length argument.')
            raise DirectionError(f'Invalid Direction.')

        if direction == 'FORWARD':
            y += int(length)
        elif direction == 'BACKWARD':
            y -= int(length)
        elif direction == 'RIGHT':
            x += int(length)
        elif direction == 'LEFT':
            x -= int(length)
        else:
            raise DirectionError(f'Specified direction: {direction} is not valid.')
    return x, y


if __name__ == '__main__':
    instructions = []

    while True:
        inp = input('IN: ')
        if inp.upper() == 'STOP':
            break
        instructions.append(inp)
    x, y = main(instructions)
    print(F'X: {x}\nY: {y}')
