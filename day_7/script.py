import utils.file_reader as file_reader
from timeit import default_timer as timer
import statistics

input_file_path = "input/input.txt"

if __name__ == '__main__':
    start = timer()

    input_lines = file_reader.read_string_file(input_file_path)

    crab_position = [int(i) for i in input_lines[0].split(',')]
    median = statistics.median(crab_position)

    silver_least_fuel = 0
    # gold_least_fuel = 0
    for crab in crab_position:
        silver_least_fuel += abs(crab - median)
        # gold_least_fuel += ( ( abs(crab - median) * (abs(crab - median) + 1) ) / 2 )
        
    
    print ("Silver   -->    Least fuel:", int(silver_least_fuel))
    # print ("Gold   -->    Least fuel:", int(gold_least_fuel))

    print("--- %s seconds ---" % str(timer() - start))
    