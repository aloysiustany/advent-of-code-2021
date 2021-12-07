import utils.file_reader as file_reader
from timeit import default_timer as timer

input_file_path = "input/input.txt"

def simulate_day(state):
    for i in range(len(state)):
        if state[i] == 0:
            state[i] = 6
            state.append(8)
        else: state[i] -= 1

    return state

if __name__ == '__main__':
    start = timer()

    input_lines = file_reader.read_string_file(input_file_path)

    state = [int(s) for s in input_lines[0].split(',')]

    for day in range(80):
        state = simulate_day(state)
    
    print ("Silver   -->    Number of lanternfish after 80 days:", len(state))

    # for day in range(256 - 80):
    #     state = simulate_day(state)
    
    # print ("Silver   -->    Number of lantern80fish after  days:", len(state))

    print("--- %s seconds ---" % str(timer() - start))