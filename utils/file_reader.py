def read_integer_file(file_path):
    lines = []
    with open(file_path, "r") as f_input:
        for line in f_input.readlines():
            lines.append(int(line))
    return lines

def read_string_file(file_path):
    with open(file_path, "r") as f_input:
        return f_input.readlines()


def read_integer_matrix_file(file_path):
    matrix = []
    with open(file_path, "r") as f_input:
        for line in f_input.readlines():
            matrix_row = []
            for digit in line.strip():
                matrix_row.append(int(digit))
            matrix.append(matrix_row)
    return matrix