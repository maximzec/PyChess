class MoveParser(object):

    coords_x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    coords_y = ['1', '2', '3', '4', '5', '6', '7', '8']
    figures = ['k', 'q', 'r', 'b', 'p']

    @staticmethod
    def parse_move(self, move: str):
        move = self.move_to_format(move)
        if len(move) > 5:
            raise SyntaxError("Input's move length must be equal 5")
        if move[0] not in figures:
            raise SyntaxError(
                'First letter should be the first letter of any figure')
        if move[1] not in coords_x or move[2] not in coords_x:
            raise SyntaxError('Row coordinate must be from A to H')
        if move[2] not in coords_y or move[4] not in coords_y:
            raise SyntaxError('Column coordinate must be from 1 to 8')

    def move_to_format(self, move: str):
        return move.lower()
