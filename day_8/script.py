import utils.file_reader as file_reader
from timeit import default_timer as timer

input_file_path = "input/input.txt"

flatten_list = lambda y:[x for a in y for x in flatten_list(a)] if type(y) is list else [y]

unique_segments = [2, 4, 3, 7]

if __name__ == '__main__':
    start = timer()

    input_lines = file_reader.read_string_file(input_file_path)

    digits = flatten_list([digit_output.split(" ") for digit_output in [lines.split("|")[1].strip() for lines in input_lines]])
    
    unique_digits_count = 0
    for digit in digits:
        l = len(digit)
        if (l in unique_segments):
            unique_digits_count += 1

    print ("Silver   -->    Unique digit count:", unique_digits_count)
    # print ("Gold     -->    Least fuel:", int(gold_least_fuel))

    print("--- %s seconds ---" % str(timer() - start))
    