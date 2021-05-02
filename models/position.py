class Position(object):

    row_dict = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E',
        6: 'F',
        7: 'G',
        8: 'H'
    }

    def __init__(self, x, y):
        if x < 0:
            raise ValueError("Figure's row value must be greater than 0")
        if x > 7:
            raise ValueError("Figure's row value must be less than 7")
        if y < 0:
            raise ValueError("Figures's column value must be greater than 0")
        if y > 7:
            raise ValueError("Figure's column value must be less than 7")
        assert y >= 0 and y <= 7
        self.x = x
        self.y = y

    def __str__(self):
        return self.row_dict[self.x + 1] + str(self.y + 1)

    def __eq__(self, position: Position):
        return self.x == position.x and self.y == position.y


pos = Position(-1, 0)
print(pos)
