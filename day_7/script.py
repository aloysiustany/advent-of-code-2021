import utils.file_reader as file_reader
from timeit import default_timer as timer
import statistics
import sys

input_file_path = "input/input.txt"

if __name__ == '__main__':
    start = timer()

    input_lines = file_reader.read_string_file(input_file_path)

    crab_position = [int(i) for i in input_lines[0].split(',')]
    median = statistics.median(crab_position)

    silver_least_fuel = 0
    [silver_least_fuel := silver_least_fuel + abs(crab - median) for crab in crab_position][-1]

    gold_least_fuel = sys.maxsize
    for i in range (min(crab_position), max(crab_position)):
        dist = 0
        [dist := dist + ( ( abs(crab - i) * (abs(crab - i) + 1) ) / 2 ) for crab in crab_position][-1]
        gold_least_fuel = dist if gold_least_fuel > dist else gold_least_fuel
    
    print ("Silver   -->    Least fuel:", int(silver_least_fuel))
    print ("Gold     -->    Least fuel:", int(gold_least_fuel))

    print("--- %s seconds ---" % str(timer() - start))
    