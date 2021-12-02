import utils.file_reader as file_reader

input_file_path = "input/input.txt"

class Instruction:
    def __init__(self, instruction_string):
        instruction_parts = instruction_string.split(" ")
        self.direction = instruction_parts[0]
        self.steps = int(instruction_parts[1])

class Position:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
    
    def move(self, instruction):
        if instruction.direction == "forward":
            self.horizontal += instruction.steps
        elif instruction.direction == "down":
            self.depth += instruction.steps
        elif instruction.direction == "up":
            self.depth -= instruction.steps
        else:
            raise Exception("Unknown Direction " + instruction.direction)
    
    def move_improved(self, instruction):
        if instruction.direction == "forward":
            self.horizontal += instruction.steps
            self.depth += (self.aim * instruction.steps)
        elif instruction.direction == "down":
            self.aim += instruction.steps
        elif instruction.direction == "up":
            self.aim -= instruction.steps
        else:
            raise Exception("Unknown Direction " + instruction.direction)

    def __str__(self):
        return "Horizontal:" + str(self.horizontal) + " Depth:" + str(self.depth) + " Aim:" + str(self.aim)

if __name__ == '__main__':
    input_lines = file_reader.read_string_file(input_file_path)
    pos = Position()
    for line in input_lines:
        instruction = Instruction(line)
        pos.move(instruction)

    print("Silver:", str(pos.horizontal * pos.depth), "[", pos, "]")

    pos = Position()
    for line in input_lines:
        instruction = Instruction(line)
        pos.move_improved(instruction)

    print("Gold:", str(pos.horizontal * pos.depth), "[", pos, "]")
    
