from matplotlib import pyplot as plt


def core_setup():
    test_1_grades = [99, 90, 85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70]

    plt.scatter(test_1_grades, test_2_grades)

    plt.xlabel("test 1 grade")
    plt.ylabel("test 2 grade")


core_setup()
plt.title("Axes Aren't Comparable")
plt.show()

core_setup()
plt.title("Axes Are Compatible")
plt.axis("equal")
plt.show()
