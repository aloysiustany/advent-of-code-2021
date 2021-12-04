import utils.file_reader as file_reader

input_file_path = "input/input.txt"

class BingoBoardNode:
    def __init__(self, number):
        self.number = number
        self.marked = False

    def mark(self):
        self.marked = True
    
    def is_marked(self):
        return self.marked
    
    def __str__(self):
        return "[Number:" + str(self.number) + ",Marked:" + str(self.marked) + "]"

class BingoBoard:
    def __init__(self):
        self.board = []
    
    def add_row(self, row):
        self.board.append([BingoBoardNode(x) for x in row])

    def __len__(self):
        return len(self.board)

    def play(self, drawn_number):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].number == drawn_number:
                    self.board[i][j].mark()
                    return self.check_if_current_row_or_column_is_full(i, j)
        return False

    def check_if_current_row_or_column_is_full(self, row_idx, col_idx):
        row_full = True
        col_full = True
        for i in range(len(self.board)):
            if self.board[i][col_idx].is_marked() == False:
                row_full = False
                break
        for j in range(len(self.board[row_idx])):
            if self.board[row_idx][j].is_marked() == False:
                col_full = False
                break
        return row_full == True or col_full == True
    
    def calc_score(self, winning_number):
        sum = 0
        for node in [node for row in self.board for node in row]:
            if node.is_marked() == False:
                sum += node.number
        return winning_number * sum
        

    def __str__(self):
        return " ".join([str(y) for x in self.board for y in x])


if __name__ == '__main__':
    input_lines = file_reader.read_string_file(input_file_path)
    
    draw = [int(x) for x in input_lines[0].split(",")]
    boards = []
    board = BingoBoard()
    for input in input_lines[1:]:
        if (input.strip() == ""):
            if len(board) > 0: 
                boards.append(board)
                board = BingoBoard()
            continue
        board.add_row([int(number) for number in input.split()])

    winners = []
    for drawn_number in draw:
        for board_idx, board in enumerate(boards):
            if any(winning_board['Board'] == board_idx for winning_board in winners): continue
            result = board.play(drawn_number)
            if (result == True):
                winners.append({'Board':board_idx, 'WinningScore':boards[board_idx].calc_score(drawn_number), 'WinningNumber':drawn_number})

    print("Silver    --->   Score:", winners[0]['WinningScore'], "\t[Board", winners[0]['Board'], "won first]", "\tWinning Number:", winners[0]['WinningNumber'])
    print("Gold      --->   Score:", winners[-1]['WinningScore'], "\t[Board", winners[-1]['Board'], "won last]", "\tWinning Number:", winners[-1]['WinningNumber'])
