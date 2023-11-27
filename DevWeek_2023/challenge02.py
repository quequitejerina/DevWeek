blockers = [
    (13, 55),
    (5, 63),
    (93, 99),
    (15, 98),
    (89, 2),
    (10, 6),
    (41, 23),
    (18, 40),
    (2, 66),
    (41, 11),
    (1, 1),
    (97, 99),
    (5, 63),
    (20, 66),
    (33, 22),
    (71, 65),
    (50, 50),
    (3, 21),
    (93, 98),
    (30, 99),
]

white_queen = (23, 45)
black_queen = (90, 99)

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
    if new_pos not in blockers and (1 <= new_pos[0] <= 100 and 1 <= new_pos[1] <= 100):
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
if white_queen in last:
    last.remove(white_queen)
print(last)
print(len(last))
