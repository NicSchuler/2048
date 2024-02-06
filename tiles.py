from random import randint
from util import GameState

def collapse(list):
    add_points = 0
    # parses list and gets rid of empty cells
    l = [element for element in list if element != ""]

    if len(l) in [0,1]:
        list_processed = l
    
    elif len(l) == 2:
        if l[0] == l[1]:
            add_points += l[0] + l[1]
            list_processed = [l[0] + l[1]]
        else:
            list_processed = l
    
    elif len(l) == 3:
        if l[0] == l[1]:
            add_points += l[0] + l[1]
            list_processed = [l[0] + l[1], l[2]]
        elif l[1] == l[2]:
            add_points += l[1] + l[2]
            list_processed = [l[0], l[1] + l[2]]
        else:
            list_processed = l

    elif len(l) == 4:
        if l[0] == l[1]:
            if l[2] == l[3]:
                add_points += l[0] + l[1] + l[2] + l[3]
                list_processed = [l[0] + l[1], l[2] + l[3]]
            else:
                add_points += l[0] + l[1]
                list_processed = [l[0] + l[1], l[2], l[3]]
        elif l[1] == l[2]:
            add_points += l[1] + l[2]
            list_processed = [l[0], l[1] + l[2], l[3]]
        
        elif l[2] == l[3]:
            add_points += l[2] + l[3]
            list_processed = [l[0], l[1], l[2] + l[3]]
        
        else:
            list_processed = l

    # filles up the list to four items
    list_filled = list_processed + [""] * (4 - len(list_processed))

    return list_filled, add_points

class Tiles:
    def __init__(self, ):
        self.state = GameState.RUNNING
        self._tiles = [
            ["","","",""],
            ["","","",""],
            ["","","",""],
            ["","","",""]
            ]
        self._score = 0
    
    def _get_row(self, row_num):
        assert 0 <= row_num <= 3
        return self._tiles[row_num]
    
    def _set_row(self, row_num, row):
        assert isinstance(row, list)
        assert len(row) == 4
        assert 0 <= row_num <= 3
        self._tiles[row_num] = row
    
    def _get_col(self, col_num):
        assert 0 <= col_num <= 3
        col = [l[col_num] for l in self._tiles]
        return col
    
    def _set_col(self, col_num, col):
        assert isinstance(col, list)
        assert len(col) == 4
        assert 0 <= col_num <= 3
        self._tiles[0][col_num] = col[0]
        self._tiles[1][col_num] = col[1]
        self._tiles[2][col_num] = col[2]
        self._tiles[3][col_num] = col[3]
    
    def _get_empty_cells(self):
        empty_0 = [(0, col) for col,val in enumerate(self._get_row(0)) if val == ""]
        empty_1 = [(1, col) for col,val in enumerate(self._get_row(1)) if val == ""]
        empty_2 = [(2, col) for col,val in enumerate(self._get_row(2)) if val == ""]
        empty_3 = [(3, col) for col,val in enumerate(self._get_row(3)) if val == ""]
        return empty_0 + empty_1 + empty_2 + empty_3

    def left(self):
        for row_num in range(4):
            r = self._get_row(row_num)
            new_r, p = collapse(r)
            self._score += p
            self._set_row(row_num, new_r)
    
    def right(self):
        for row_num in range(4):
            r = self._get_row(row_num)
            new_r, p = collapse(r[::-1])
            self._score += p
            self._set_row(row_num, new_r[::-1])

    def up(self):
        for col_num in range(4):
            c = self._get_col(col_num)
            new_c, p = collapse(c)
            self._score += p
            self._set_col(col_num, new_c)
    
    def down(self):
        for col_num in range(4):
            c = self._get_col(col_num)
            new_c, p = collapse(c[::-1])
            self._score += p
            self._set_col(col_num, new_c[::-1])
    
    def get_score(self):
        return self._score
    
    def get_game_screen(self):
        return (
            f"Current Score: {self.get_score()}",
            "",
            " ______ ______ ______ ______ ",
            "|      |      |      |      |",
            f"| {self._tiles[0][0]:>4} | {self._tiles[0][1]:>4} | {self._tiles[0][2]:>4} | {self._tiles[0][3]:>4} |",
            "|______|______|______|______|",
            "|      |      |      |      |",
            f"| {self._tiles[1][0]:>4} | {self._tiles[1][1]:>4} | {self._tiles[1][2]:>4} | {self._tiles[1][3]:>4} |",
            "|______|______|______|______|",
            "|      |      |      |      |",
            f"| {self._tiles[2][0]:>4} | {self._tiles[2][1]:>4} | {self._tiles[2][2]:>4} | {self._tiles[2][3]:>4} |",
            "|______|______|______|______|",
            "|      |      |      |      |",
            f"| {self._tiles[3][0]:>4} | {self._tiles[3][1]:>4} | {self._tiles[3][2]:>4} | {self._tiles[3][3]:>4} |",
            "|______|______|______|______|",
        )
    
    def add_tile(self):
        # draw value (2 or 4) and draw where to place it
        tile_value = randint(1,2) * 2
        empty_cells = self._get_empty_cells()
        assert len(empty_cells) > 0
        replace_row, replace_col = empty_cells[randint(0, len(empty_cells))-1]

        # replace value
        new_row = self._get_row(replace_row)
        new_row[replace_col] = tile_value
        self._set_row(replace_row, new_row)
    
    def check_finished(self):
        if len(self._get_empty_cells())==0:
            self.state = GameState.FINISHED

if __name__ == "__main__":
    t = Tiles()
    print(t._get_empty_cells())