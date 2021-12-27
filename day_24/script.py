import utils.file_reader as file_reader
from timeit import default_timer as timer
import math

input_file_path = "input/input.txt"

alu = {
    'w':0,
    'x':0,
    'y':0,
    'z':0
}

def isint(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

def alu_reset():
    global alu
    alu = {
        'w':0,
        'x':0,
        'y':0,
        'z':0
    }

def inp(var, val):
    global alu
    alu[var] = int(val)

def add(left, right):
    global alu
    right_val = int(right if isint(right) else alu[right])
    alu[left] = int(alu[left]) + right_val

def mul(left, right):
    global alu
    right_val = int(right if isint(right) else alu[right])
    alu[left] = int(alu[left]) * right_val

def div(left, right):
    global alu
    right_val = int(right if isint(right) else alu[right])
    alu[left] = int(alu[left]) // right_val

def mod(left, right):
    global alu
    right_val = int(right if isint(right) else alu[right])
    alu[left] = int(alu[left]) % right_val

def eql(left, right):
    global alu
    right_val = int(right if isint(right) else alu[right])
    alu[left] = 1 if int(alu[left]) == right_val else 0


if __name__ == '__main__':
    start = timer()
    instr_list = [line.split() for line in file_reader.read_string_file(input_file_path)]

    # model = "99999999999999"
    for m in range (99999999999999, 11111111111111, -1):
    # for m in range (99999999999999, 99999998174456, -1):
        model = str(m)
        if "0" in model: continue
        print("Current model:", model)
        alu_reset()
        loop_cursor = -1
        for instr in instr_list:
            if instr[0] == 'inp': 
                loop_cursor += 1
                inp(instr[1], model[loop_cursor])
            elif instr[0] == 'add': add(instr[1], instr[2])
            elif instr[0] == 'mul': mul(instr[1], instr[2])
            elif instr[0] == 'div': div(instr[1], instr[2])
            elif instr[0] == 'mod': mod(instr[1], instr[2])
            elif instr[0] == 'eql': eql(instr[1], instr[2])
        if (alu['z'] == 0):
            print("Silver:", model)
            break


    print("--- %s seconds ---" % str(timer() - start))