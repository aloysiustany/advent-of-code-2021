import utils.file_reader as file_reader
from timeit import default_timer as timer
from functools import reduce

input_file_path = "input/input.txt"

class MapPoint:
    def __init__(self, digit):
        self.digit = digit
        self.covered = False

def grab_area(i, j):
    if map[i][j].digit == 9 or map[i][j].covered == True:
        return 0
    map[i][j].covered = True
    area = 1
    if (j != 0):
        area += grab_area(i, j - 1)  # go left
    if (j != len(map[i]) - 1):
        area += grab_area(i, j + 1)  # go right
    if (i != 0):
        area += grab_area(i - 1, j)  # go up
    if (i != len(map) - 1):
        area += grab_area(i + 1, j)  # go down
    return area

if __name__ == '__main__':
    start = timer()

    input_lines = file_reader.read_string_file(input_file_path)
    map = [[MapPoint(int(digit)) for digit in line.strip()]
           for line in input_lines]

    risk = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if ((j == 0 or map[i][j - 1].digit > map[i][j].digit) and
                (j == (len(map[i]) - 1) or map[i][j + 1].digit > map[i][j].digit) and
                (i == 0 or map[i - 1][j].digit > map[i][j].digit) and
                (i == (len(map) - 1) or map[i + 1][j].digit > map[i][j].digit)):
                risk += (map[i][j].digit + 1)

    print("Silver   -->    Risk:", risk)

    basin = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j].digit != 9 and map[i][j].covered == False:
                area_size = grab_area(i, j)
                basin.append(area_size)

    print("Gold     -->    Answer:", reduce(lambda x, y: x * y, sorted(basin)[-3:]))

    print("--- %s seconds ---" % str(timer() - start))
