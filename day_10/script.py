import utils.file_reader as file_reader
from timeit import default_timer as timer

input_file_path = "input/input.txt"

chunk_limiters = {
    '(':')',
    '[':']',
    '{':'}',
    '<':'>',
}

error_points = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137,
}

if __name__ == '__main__':
    start = timer()
    input_lines = file_reader.read_string_file(input_file_path)

    points = 0
    for line in input_lines:
        stack = []
        for ch in line.strip():
            if ch in chunk_limiters:
                stack.append(ch)
            elif ch != chunk_limiters.get(stack.pop()):
                points += error_points[ch]
                break
    
    print("Silver   -->    Error Score:", points)

    

    # print("Gold     -->    :", )

    print("--- %s seconds ---" % str(timer() - start))
