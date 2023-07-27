from typing import List, Tuple, Callable
from vector import Vector

Matrix = List[Vector]


def shape(matrix: Matrix) -> Tuple[int, int]:
    rows = len(matrix)
    assert rows > 0, "empty matrix"
    columns = len(matrix[0])
    assert all(columns == len(vector) for vector in matrix), "matrix has irregular size"
    return (rows, columns)


assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)


def get_row(matrix: Matrix, row: int) -> Vector:
    return matrix[row]


assert get_row([[1, 2, 3], [4, 5, 6]], 1) == [4, 5, 6]


def get_column(matrix: Matrix, column: int) -> Vector:
    return [vector[column] for vector in matrix]


assert get_column([[1, 2, 3], [4, 5, 6]], 1) == [2, 5]


def make_matrix(rows: int, columns: int, f: Callable[[int, int], float]) -> Matrix:
    return [[f(row, column) for column in range(columns)] for row in range(rows)]


assert make_matrix(2, 3, lambda row, column: row * 2 + column) == [[0, 1, 2], [2, 3, 4]]


def identity_matix(size: int) -> Matrix:
    return make_matrix(size, size, lambda row, column: 1 if row == column else 0)


assert identity_matix(5) == [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
]
