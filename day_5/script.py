from sympy import *
import enum
import utils.file_reader as file_reader
from timeit import default_timer as timer

input_file_path = "input/input.txt"

map_max_row = 1000
map_max_col = 1000

class LinePosition(enum.Enum):
    vertical = 1
    horizontal = 2
    diagonal = 3

class Map:
    def __init__(self):
        self.area = [[0 for col in range(map_max_col)] for row in range(map_max_row)]

    def mark_points(self, points):
        for p in points:
            self.area[p[0]][p[1]] += 1
    
    def count_overlapping_points(self):
        count = 0
        for i in range(map_max_row):
            for j in range(map_max_col):
                if self.area[i][j] > 1:
                    count += 1
        return count

class SpecialLine:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        if p1[0] == p2[0]:
            self.position = LinePosition.horizontal
        elif p1[1] == p2[1]:
            self.position = LinePosition.vertical
        else:
            self.position = LinePosition.diagonal   # assumed as per problem statement

    @staticmethod
    def is_vertical_or_horizontal(p1, p2):
        return p1[0] == p2[0] or p1[1] == p2[1]
    
    def get_all_points(self, consider_diagonal_line):
        if self.position == LinePosition.horizontal:
            inc_factor = -1 if self.p1[1] > self.p2[1] else 1
            return [Point(self.p1[0], p) for p in range(self.p1[1], self.p2[1] + inc_factor, inc_factor)]
        if self.position == LinePosition.vertical:
            inc_factor = -1 if self.p1[0] > self.p2[0] else 1
            return [Point(p, self.p1[1]) for p in range(self.p1[0], self.p2[0] + inc_factor, inc_factor)]
        if consider_diagonal_line == True and self.position == LinePosition.diagonal:
            inc_factor = -1 if self.p1[0] > self.p2[0] else 1
            x_range = [x for x in range(self.p1[0], self.p2[0] + inc_factor, inc_factor)]
            inc_factor = -1 if self.p1[1] > self.p2[1] else 1
            y_range = [y for y in range(self.p1[1], self.p2[1] + inc_factor, inc_factor)]
            if (len(x_range) != len(y_range)):
                raise Exception("Diagonal line not at 45 degrees")
            return [Point(x_range[i], y_range[i]) for i in range(len(x_range))]
        return []   # for silver
    
    def __str__(self):
        return "[{p00},{p01}] -> [{p10},{p11}]".format(p00 = self.p1[0], p01 = self.p1[1], p10 = self.p2[0], p11 = self.p2[1])

if __name__ == '__main__':
    start = timer()

    input_lines = file_reader.read_string_file(input_file_path)

    lines = []
    for input in input_lines:
        points_parts = [int(prt) for pt in input.split(" -> ") for prt in pt.split(",")]
        p1 = Point(points_parts[0], points_parts[1])
        p2 = Point(points_parts[2], points_parts[3])
        if points_parts[0] > map_max_row or points_parts[2] > map_max_row or points_parts[1] > map_max_col or points_parts[3] > map_max_col:
            raise Exception("Input output map range. " + input)
        line = SpecialLine(p1, p2)
        lines.append(line)

    map = Map()
    for line in lines:
        all_points_on_line = line.get_all_points(False)
        map.mark_points(all_points_on_line)
    
    print("Silver   -->   Number of points that overlap:",map.count_overlapping_points())

    map = Map()
    for line in lines:
        all_points_on_line = line.get_all_points(True)
        map.mark_points(all_points_on_line)
    
    print("Gold     -->   Number of points that overlap:",map.count_overlapping_points())

    print("--- %s seconds ---" % str(timer() - start))
