import utils.file_reader as file_reader

input_file_path = "input/input.txt"

if __name__ == '__main__':
    input_lines = file_reader.read_integer_file(input_file_path)

    count_increases = 0
    for i, item in enumerate(input_lines):
        if i > 0 and item > input_lines[i-1]:
            count_increases += 1
    print("Number of increasing elements:", count_increases)

    input_len = len(input_lines)
    sliding_window = []
    count_sliding_window_increases = 0
    for i, item in enumerate(input_lines):
        if (i + 2) < input_len:
            sliding_window.append(item + input_lines[i+1] + input_lines[i+2])
    for i, item in enumerate(sliding_window):
        if i > 0 and item > sliding_window[i-1]:
            count_sliding_window_increases += 1
    print("Number of increasing sliding windows:", count_sliding_window_increases)
