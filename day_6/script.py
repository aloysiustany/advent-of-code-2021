import utils.file_reader as file_reader
from timeit import default_timer as timer

input_file_path = "input/input.txt"

def simulate_day(ages):
    new_fishes = ages[0]
    for i in range(9):
        if i > 0: ages[i - 1] = ages[i]
    ages[8] = new_fishes
    ages[6] += new_fishes
    return ages

if __name__ == '__main__':
    start = timer()

    input_lines = file_reader.read_string_file(input_file_path)

    init_state = [int(s) for s in input_lines[0].split(',')]
    
    ages = [0] * 9
    for s in init_state:
        ages[s] += 1

    for day in range(80): ages = simulate_day(ages)
    print ("Silver   -->    Number of lanternfish after 80 days:", sum(ages))

    for day in range(256 - 80): ages = simulate_day(ages)
    print ("Gold     -->    Number of lanternfish after 256 days:", sum(ages))

    print("--- %s seconds ---" % str(timer() - start))