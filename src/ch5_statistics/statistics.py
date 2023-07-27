from ..ch4_linear_algebra import vector
from ..ch4_linear_algebra.vector import Vector
from collections import Counter
from . import test_data
import math


def mean(xs: Vector) -> float:
    return sum(xs) / len(xs)


assert mean([1, 2, 3]) == 2


def median(xs: Vector) -> float:
    sorted_v = sorted(xs)
    mid = len(sorted_v) // 2
    if len(sorted_v) % 2:
        return sorted_v[mid]
    else:
        return (sorted_v[mid - 1] + sorted_v[mid]) / 2


assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (9 + 2) / 2


def quantile(xs: Vector, percentile: float) -> float:
    p_index = int(percentile * len(xs))
    return sorted(xs)[p_index]


assert quantile(test_data.num_friends, 0.10) == 1
assert quantile(test_data.num_friends, 0.25) == 3
assert quantile(test_data.num_friends, 0.75) == 9
assert quantile(test_data.num_friends, 0.90) == 13


def mode(xs: Vector) -> float:
    counts = Counter(xs)
    max_count = max(counts.values())
    return [value for value, count in counts.items() if count == max_count]


assert set(mode(test_data.num_friends)) == {1, 6}


def data_range(xs: Vector) -> float:
    return max(xs) - min(xs)


assert data_range(test_data.num_friends) == 99


def de_mean(xs: Vector) -> Vector:
    m = mean(xs)
    return [x - m for x in xs]


def variance(xs: Vector) -> float:
    assert len(xs) >= 2, "variance requires at least 2 elements"

    length = len(xs)
    deviations = de_mean(xs)
    return vector.sum_of_squares(deviations) / (length - 1)


assert 81.54 < variance(test_data.num_friends) < 81.55


def std_deviation(xs: Vector) -> float:
    return math.sqrt(variance(xs))


assert 9 < std_deviation(test_data.num_friends) < 9.04


def interquartile_range(xs: Vector) -> float:
    return quantile(xs, 0.75) - quantile(xs, 0.25)


assert interquartile_range(test_data.num_friends) == 6


def covariance(xs: Vector, ys: Vector) -> float:
    assert len(xs) == len(ys), "xs and ys must have the same number of elements"
    return vector.dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)


assert 22.42 <= covariance(test_data.num_friends, test_data.daily_minutes) < 22.43
assert (
    22.42 / 60 <= covariance(test_data.num_friends, test_data.daily_hours) < 22.43 / 60
)


def correlation(xs: Vector, ys: Vector) -> float:
    std_dev_x = std_deviation(xs)
    std_dev_y = std_deviation(ys)

    if std_dev_x > 0 and std_dev_y > 0:
        return covariance(xs, ys) / std_dev_x / std_dev_y
    else:
        return 0


assert 0.24 <= correlation(test_data.num_friends, test_data.daily_minutes) < 0.25
assert 0.24 <= correlation(test_data.num_friends, test_data.daily_hours) < 0.25
