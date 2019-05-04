
class Queen:
    def __init__(self):
        self.column = None
        self.row = None

    def location(self):
        return [self.column, self.row]

    def match_location(self, x, y):
        location = self.location()
        location == [x, y]


class Board:
    def __init__(self, size):
        self.queens = []
        self.size = size
        self.starting_row = 0
        self.startng_column = 0
        self.ending_row = self.size - 1
        self.ending_column = self.size - 1 
        self.h_edge = '='
        self.v_edge = "|"
        self.blank = '-'

    def place_queen(self, column=0, row=0):
        queen = Queen()
        queen.column = column
        queen.row = row
        self.queens.append(queen)
        return queen

    def find_queen(self, column, row):
        for queen in self.queens:
            if queen.match_location(column, row):
                return queen

    def remove_queen(self, column, row):
        queen = self.find_queen(column, row)
        if queen:
            queen.column = None
            queen.row = None
            self.queens.remove(queen)

    def display(self):
        print("\n")
        print(f"{self.hedge}" * self.size + 2)
    