import utils.file_reader as file_reader
from timeit import default_timer as timer

input_file_path = "input/input.txt"

row_count = 100
col_count = 100

if __name__ == '__main__':
    start = timer()

    input_lines = file_reader.read_string_file(input_file_path)

    map = []
    for line in input_lines:
        map_row = []
        for digit in line:
            d = digit.strip()
            if d != "":
                map_row.append(int(d))
        map.append(map_row)

    risk = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if ((j == 0 or map[i][j - 1] > map[i][j]) and
                 (j == (len(map[i]) - 1) or map[i][j + 1] > map[i][j]) and
                 (i == 0 or map[i - 1][j] > map[i][j]) and 
                 (i == (len(map) - 1) or map[i + 1][j] > map[i][j])):
                      risk += (map[i][j] + 1)


    print ("Silver   -->    Risk:", risk)


    print("--- %s seconds ---" % str(timer() - start))
    