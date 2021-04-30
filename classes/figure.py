from abc import ABCMeta
from position import Position
from typing import List


class Figure(object):

    __metaclass__ = ABCMeta
    moves: int = 0
    available_positions: List[Position] = []

    def __init__(self, position: Position):
        self.position = position

    def move(self, position: Position):
        if position in available_positions:
            self.position = position


class Paw(Figure):
    value: int = 0


class Knight(Figure):
    value: int = 3


class Bishop(Figure):
    value: int = 3


class Rook(Figure):
    value: int = 5


class Queen(Figure):
    value: int = 10


class King(Figure):
    value: int = 100
    checkmate_status: bool = False
