import math
import random


def uniform_pdf(x: float) -> float:
    return x if 0 <= x < 1 else 0


def uniform_cdf(x: float) -> float:
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1


SQRT_TWO_PI = math.sqrt(2 * math.pi)


def normal_pdf(x: float, mean: float = 0, std_dev: float = 1) -> float:
    return math.exp(-((x - mean) ** 2) / 2 / std_dev**2) / (SQRT_TWO_PI * std_dev)


def normal_cdf(x: float, mean: float = 0, std_dev: float = 1) -> float:
    return (1 + math.erf((x - mean) / math.sqrt(2) / std_dev)) / 2


def inverse_normal_cdf(
    p: float, mean: float = 0, std_dev: float = 1, tolerance: float = 0.00001
) -> float:
    if mean != 0 or std_dev != 1:
        return mean + std_dev * inverse_normal_cdf(p, tolerance=tolerance)
    low_z = -10.0  # normal_cdf(-10) is very close to 0
    hi_z = 10.0  # normal_cdf(10) is very close to 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2  # conside the mid point
        mid_p = normal_cdf(mid_z)  # and the cdf value there
        if mid_p < p:
            low_z = mid_p  # mid point too low, search above it
        else:
            hi_z = mid_p  # mid point too high, search below it

    return mid_z


def bernoulli_trial(p: float) -> int:
    """Returns 1 with probability p and 0 with probability 1"""
    return 1 if random.random() < p else 0


def binomial(n: int, p: float) -> int:
    """Returns the sum of n bernoulli(p) trials"""
    return sum(bernoulli_trial(p) for _ in range(n))
