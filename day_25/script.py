import utils.file_reader as file_reader
from timeit import default_timer as timer

input_file_path = "input/input.txt"

mapp = []

def get_my_next_possible_position(pos_row, pos_col):
    global mapp
    object = mapp[pos_row][pos_col]
    if object == '>':
        if pos_col == len(mapp[pos_row]) - 1:
            return pos_row, 0
        return pos_row, pos_col + 1
    if object == 'v':
        if pos_row == len(mapp) - 1:
            return 0, pos_col
        return pos_row + 1, pos_col

def move_me_if_possible(pos_row, pos_col, prev_occupied_positions):
    global mapp
    next_pos_row, next_pos_col = get_my_next_possible_position(pos_row, pos_col)
    if mapp[next_pos_row][next_pos_col] == '.' and (str(next_pos_row) + ":" + str(next_pos_col)) not in prev_occupied_positions:
        object = mapp[pos_row][pos_col]
        mapp[next_pos_row][next_pos_col] = object
        mapp[pos_row][pos_col] = '.'
        return next_pos_row, next_pos_col
    return None, None
        
def do_step(curr_direction):
    global mapp
    prev_occupied_positions = set()
    new_occupied_positions = set()
    num_of_moves = 0
    for row in range(len(mapp)):
        for col in range(len(mapp[row])):
            if mapp[row][col] == curr_direction and (str(row) + ":" + str(col)) not in new_occupied_positions:
                moved_row, moved_col = move_me_if_possible(row, col, prev_occupied_positions)
                if moved_row is not None and moved_col is not None: 
                    new_occupied_positions.add(str(moved_row) + ":" + str(moved_col))
                    prev_occupied_positions.add(str(row) + ":" + str(col))
                    num_of_moves += 1
    return num_of_moves

if __name__ == '__main__':
    start = timer()
    mapp = file_reader.read_matrix_file(input_file_path)
    for step in range(1, 1000):
        moves = 0
        moves += do_step('>')
        moves += do_step('v')
        if moves == 0:
            print("Silver: ", step)
            break

    print("--- %s seconds ---" % str(timer() - start))
