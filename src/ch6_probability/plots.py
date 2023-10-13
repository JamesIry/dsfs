from probability import normal_pdf, normal_cdf, binomial
from matplotlib import pyplot as plt
from collections import Counter
import math

xs = [x / 10.0 for x in range(-50, 50)]

plt.plot(xs, [normal_pdf(x) for x in xs], "-", label="mu=0, sigma=1")
plt.plot(xs, [normal_pdf(x, std_dev=2) for x in xs], "-", label="mu=0, sigma=2")
plt.plot(xs, [normal_pdf(x, std_dev=0.5) for x in xs], "-", label="mu=0, sigma=0.5")
plt.plot(xs, [normal_pdf(x, mean=-1) for x in xs], "-", label="mu=-1, sigma=1")

plt.legend()
plt.title("Various Normal PDFs")
plt.show()


plt.plot(xs, [normal_cdf(x) for x in xs], "-", label="mu=0, sigma=1")
plt.plot(xs, [normal_cdf(x, std_dev=2) for x in xs], "-", label="mu=0, sigma=2")
plt.plot(xs, [normal_cdf(x, std_dev=0.5) for x in xs], "-", label="mu=0, sigma=0.5")
plt.plot(xs, [normal_cdf(x, mean=-1) for x in xs], "-", label="mu=-1, sigma=1")
plt.legend(loc=4)  # bottom right
plt.title("Various Normal CDFs")
plt.show()


def binomial_histogram(p: float, n: int, num_points: int) -> None:
    """Picks points from binomial(n,p) and plots their histogram"""
    data = [binomial(n, p) for _ in range(num_points)]

    # use a bar chart to show actual binomial samples
    histogram = Counter(data)
    plt.bar(
        [x - 0.4 for x in histogram.keys()],
        [v / num_points for v in histogram.values()],
        0.8,
        color="0.75",
    )

    mean = p * n
    std_dev = math.sqrt(n * p * (1 - p))

    # use a line chart to show the normal approximation
    xs = range(min(data), max(data) + 1)
    ys = [
        normal_cdf(i + 0.5, mean, std_dev) - normal_cdf(i - 0.5, mean, std_dev)
        for i in xs
    ]
    plt.plot(xs, ys)
    plt.title("Binomial Distribution vs Normal Approximation")
    plt.show()


binomial_histogram(0.75, 100, 1000)
