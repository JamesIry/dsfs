from matplotlib import pyplot as plt


def core_setup():
    mentions = [500, 505]
    years = [2017, 2018]

    plt.bar(years, mentions, 0.8)
    plt.xticks(years)
    plt.ylabel("# of times I heard someone say 'data science'")

    plt.ticklabel_format(useOffset=False)


# misleading axis
core_setup()
plt.axis([2016.5, 2018.5, 499, 506])
plt.title("Look at that 'Huge' Increase!")
plt.show()

# more sensible axis
core_setup()
plt.axis([2016.5, 2018.5, 0, 550])
plt.title("Not so huge anymore")
plt.show()
