# matrix = """12345
# gABC6
# fHID7
# eGFE8
# dcba9"""


# amount = 2

matrix = """0111101001011111111111110
1100000110010100000000010
1001001011001001011111001
1011010111101010010111101
1011010101111011100100001
1011110101010110100111000
1010000001010101010000111
1011001010001101101111110
1000010001111101100000111
1010001111101100011111010
1000100000101110000001000
1100001110101001101010001
1000010010100010000101101
1111011010110101011110011
0001100100000010100001001
1001101001010111101000101
0011100000110110010110001
0111101010010101001111101
1100100101000101010000101
1011111100000001010111101
1000111101000011010101101
0100000000110011110101101
0100110100011000001001001
1011000011000001100110011
1000100111110100110111000"""


amount = 17


def matrix_to_string(matrix, height):
    strings = int(height / 2)
    lines = []
    for n in range(strings):
        line = ""
        loc = [n, n]
        while True:
            line += matrix[loc[0]][loc[1]]
            if loc[0] == n + 1 and loc[1] == n:
                break
            elif loc[1] == width - 1 - n and loc[0] != height - 1 - n:
                loc[0] += 1
            elif loc[0] == height - 1 - n and loc[1] != n:
                loc[1] -= 1
            elif loc[1] == n and loc[0] != n:
                loc[0] -= 1
            elif loc[0] == n and loc[1] != width - 1 - n:
                loc[1] += 1
        lines.append(line)
        print(line)
        print(len(line))
    lines.append(matrix[strings][strings])
    print(len(lines))
    return lines


def move(line_list):
    changed = []
    for line in lines_list:
        for _ in range(amount):
            line = line[1:] + line[0]
        changed.append(line)
    return changed


def put_it_together(lines, height, width):
    new_matrix = [[0 for x in range(width)] for n in range(height)]
    for n, line in enumerate(lines):
        loc = [n, n]
        for char in line:
            new_matrix[loc[0]][loc[1]] = char
            if loc[1] == width - 1 - n and loc[0] != height - 1 - n:
                loc[0] += 1
            elif loc[0] == height - 1 - n and loc[1] != n:
                loc[1] -= 1
            elif loc[1] == n and loc[0] != n:
                loc[0] -= 1
            elif loc[0] == n and loc[1] != width - 1 - n:
                loc[1] += 1

    return new_matrix


matrix = matrix.splitlines()
height = len(matrix)
width = len(matrix[0])
lines_list = matrix_to_string(matrix, height)
moved = move(lines_list)
matrix = put_it_together(moved, height, width)
qr_string = []
for item in matrix:
    line = ",".join([str(i) for i in item])
    qr_string.append(line)

qr = "\n".join(qr_string)
print(qr)
with open("my_file.csv", "w") as out:
    out.write(qr)
