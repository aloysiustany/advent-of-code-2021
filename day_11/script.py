import utils.file_reader as file_reader
from timeit import default_timer as timer

input_file_path = "input/input.txt"
# input_file_path = "input/input.ex"

# to navigate - clock wise from top
DR = [-1, -1, 0, 1, 1, 1,  0,  -1]
DC = [0,  1,  1, 1, 0, -1, -1, -1]

def get_all_adjacent_cells(i, j):
    adj_cells = []
    for dir_i in range(len(DR)):
        cell_i = i + DR[dir_i]
        cell_j = j + DC[dir_i]
        if 0 <= cell_i <= 9 and 0 <= cell_j <= 9:
            adj_cells.append([cell_i, cell_j])
    return adj_cells

mapp = []

def check_and_flash(i, j):
    if mapp[i][j] == -1: return 0
    mapp[i][j] += 1
    flash_count = 0
    if mapp[i][j] > 9:
        flash_count += 1
        mapp[i][j] = -1
        for adj_cell in get_all_adjacent_cells(i, j):
            count = check_and_flash(adj_cell[0], adj_cell[1])
            flash_count += count
    return flash_count

if __name__ == '__main__':
    start = timer()
    mapp = file_reader.read_integer_matrix_file(input_file_path)

    silver_iterations_count = 100
    gold_iterations_count = 1000

    flash_count = 0
    first_all_flash_itr = -1
    for itr in range(gold_iterations_count):
        all_flash_itr = True
        for i in range(10):
            for j in range(10):
                count = check_and_flash(i, j)
                if itr < silver_iterations_count: flash_count += count

        for i in range(10):
            for j in range(10):
                if mapp[i][j] == -1: mapp[i][j] = 0
                elif all_flash_itr: all_flash_itr = False

        if all_flash_itr and first_all_flash_itr == -1:
            first_all_flash_itr = itr + 1              

    print("Silver     -->    Total Flashes:", flash_count)
    print("Gold       -->    All flash step:", first_all_flash_itr)

    print("--- %s seconds ---" % str(timer() - start))
