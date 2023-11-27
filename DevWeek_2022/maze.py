import pandas as pd
import numpy as np
import gc


K = 1
raw = []
columns = []
answer = ['B']
possible_answer = []

def check_sides(x, y):
    if data[x][y] == 'X':
        return
    if x > 0 and data[x-1][y] == '0':
        possible_answer.append('N')
        check_sides(x-1, y)
    elif data[x+1][y] == '0':
        possible_answer.append('S')
        check_sides(x+1, y)
    elif y > 0 and data[x][y-1] == '0':
        possible_answer.append('W')
        check_sides(x, y-1)
    elif data[x][y+1] == '0':
        possible_answer.append('E')
        check_sides(x, y+1)
    else:
        return
    return possible_answer


  
# Text file data converted to integer data type
data = np.loadtxt("maze.txt", dtype=str)
print(data[1][0])
# print(check_sides(1,0))