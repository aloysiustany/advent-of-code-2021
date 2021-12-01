def read_integer_file(file_path):
    lines = []
    with open(file_path, "r") as f_input:
        for line in f_input.readlines():
            lines.append(int(line))
    return lines

def read_string_file(file_path):
    with open(file_path, "r") as f_input:
        return f_input.readlines()