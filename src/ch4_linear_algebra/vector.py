from typing import List
import math

Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be the same size"
    return [x + y for x, y in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def subtract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be the same size"
    return [x - y for x, y in zip(v, w)]


assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "no vectors provided"

    length = len(vectors[0])

    assert all(
        len(vector) == length for vector in vectors
    ), "vectors must all the same size"

    return [sum(vector[i] for vector in vectors) for i in range(length)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(x: float, vector: Vector) -> Vector:
    return [x * n for n in vector]


assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


# Component wise mean of a list of vectors
def vector_mean(vectors: List[Vector]) -> Vector:
    length = len(vectors)
    return scalar_multiply(1 / length, vector_sum(vectors))


assert vector_mean([[1, 2], [3, 4], (5, 6)]) == [3, 4]


def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w), "vectors must be the same size"
    return sum([x * y for x, y in zip(v, w)])


assert dot([1, 2, 3], [4, 5, 6]) == 32  # 1*4 + 2*5 + 3*6 = 5 + 10 + 18 = 32


def sum_of_squares(vector: Vector) -> float:
    return dot(vector, vector)


assert sum_of_squares([1, 2, 3]) == 14  # 1*1 + 2*2 + 3*3 = 1 + 4 + 9 = 14


def magnitude(vector: Vector) -> float:
    return math.sqrt(sum_of_squares(vector))


assert magnitude([3, 4]) == 5


def squared_distance(v: Vector, w: Vector) -> float:
    return sum_of_squares(subtract(v, w))


def distance(v: Vector, w: Vector) -> float:
    math.sqrt(sum_of_squares(v, w))  # equivalently magnitude(subtract(v,w))
