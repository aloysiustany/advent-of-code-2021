import utils.file_reader as file_reader
from timeit import default_timer as timer
import statistics

input_file_path = "input/input.txt"

chunk_limiters = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

points_dict = {
    ')': {'error_point': 3, 'correction_point': 1},
    ']': {'error_point': 57, 'correction_point': 2},
    '}': {'error_point': 1197, 'correction_point': 3},
    '>': {'error_point': 25137, 'correction_point': 4},
}

correction_multiplier = 5

if __name__ == '__main__':
    start = timer()
    input_lines = file_reader.read_string_file(input_file_path)

    incomplete_lines = []

    points = 0
    for line in input_lines:
        stack = []
        corrupted_line = False
        for ch in line.strip():
            if ch in chunk_limiters:    # if it is an opening chunk character
                stack.append(ch)
            elif ch != chunk_limiters[stack.pop()]:
                points += points_dict[ch]['error_point']
                corrupted_line = True
                break
        if corrupted_line == False and len(stack) > 0:
            incomplete_lines.append("".join(stack)[::-1])

    print("Silver   -->    Error Score:", points)

    correction_scores = []
    for incomplete_line in incomplete_lines:
        correction_score = 0
        for ch in incomplete_line:
            correction_score = (correction_score * correction_multiplier) + \
                points_dict[chunk_limiters[ch]]['correction_point']
        correction_scores.append(correction_score)

    print("Gold     -->    Correction Score:", statistics.median(correction_scores))

    print("--- %s seconds ---" % str(timer() - start))
