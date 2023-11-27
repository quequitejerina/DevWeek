blockers = [
    (3, 5),
]

white_queen = (4, 4)
black_queen = (3, 8)

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (-1, -1),
    (1, -1),
    (-1, 1),
    (1, 1),
]


def movements(position, direction, cels):
    new_pos = (position[0] + direction[0], position[1] + direction[1])
    if new_pos not in blockers and (1 <= new_pos[0] <= 8 and 1 <= new_pos[1] <= 8):
        cels.append(new_pos)
        return movements(new_pos, direction, cels)

    else:
        return position


def get_cells(chess_piece, directions):
    cels = []
    for direction in directions:
        cels.append(movements(chess_piece, direction, cels))
    cels = list(set(cels))
    return cels


black_queen_path = get_cells(black_queen, directions)
last = get_cells(white_queen, directions)
for item in last:
    if item in black_queen_path:
        last.remove(item)
last.remove(white_queen)
print(last)
print(len(last))
