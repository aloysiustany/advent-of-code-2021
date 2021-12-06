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

class Point:
    def __init__(self, x, y):
        self[0] = x
        self[1] = y
    
    def __getitem__(self, key):
        if key < 0 or key > 1:
            raise Exception("Index out of bounds [key {k}] for Point: {p}".format(p = self.__str__(), k = key))
        return self.x if key == 0 else self.y

    def __setitem__(self, key, value):
        if key < 0 or key > 1:
            raise Exception("Index out of bounds for Point: " + self.__str__())
        if key == 0:
            if (value > map_max_row):
                raise Exception("Input outside map range. " + value)
            self.x = value
        else:
            if (value > map_max_col):
                raise Exception("Input outside map range. " + value)
            self.y = value

    def __str__(self):
        return "[{x},{y}]".format(x=self.x, y=self.y)

class Map:
    def __init__(self):
        self.area = [[0 for col in range(map_max_col)] for row in range(map_max_row)]
        self.overlapping_points = []

    def mark_points(self, points):
        for p in points:
            self.area[p[0]][p[1]] += 1
            if (self.area[p[0]][p[1]] == 2): self.overlapping_points.append(str(p))
    
    def count_overlapping_points(self):
        return len(self.overlapping_points)

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        if p1[0] == p2[0]:
            self.position = LinePosition.horizontal
        elif p1[1] == p2[1]:
            self.position = LinePosition.vertical
        else:
            self.position = LinePosition.diagonal   # assumed as per problem statement
    
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

    lines = [Line(pts[0], pts[1]) for pts in [ 
        [tuple(map(int, item.split(',')))
        for item in line.split('->')]
        for line in input_lines
    ]]

    map = Map()
    for line in lines: map.mark_points(line.get_all_points(False))
    print("Silver   -->   Number of points that overlap:",map.count_overlapping_points())

    map = Map()
    for line in lines: map.mark_points(line.get_all_points(True))
    print("Gold     -->   Number of points that overlap:",map.count_overlapping_points())

    print("--- %s seconds ---" % str(timer() - start))
