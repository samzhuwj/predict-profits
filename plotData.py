import matplotlib.pyplot as plt


def plot_data(x, y):
    """
    to display the dataset
    """
    # ===================== Your Code Here =====================
    # Instructions : Plot the training data into a figure using the matplotlib.pyplot
    #                using the "plt.scatter" function. Set the axis labels using
    #                "plt.xlabel" and "plt.ylabel". Assume the population and revenue data
    #                have been passed in as the x and y.
    # Hint : You can use the 'marker' parameter in the "plt.scatter" function to change the marker type (e.g. "x", "o").
    #        Furthermore, you can change the color of markers with 'c' parameter.
    plt.scatter(x, y, c='r', marker="x") # Make a scatter plot of x vs y with color, marker
    plt.xlabel('population of city in 10,000s')
    plt.ylabel('profit in $10,000s')
    plt.show()
