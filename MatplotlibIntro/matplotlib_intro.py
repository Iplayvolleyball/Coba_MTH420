# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
Iris Coba
04/26Z/2025
MTH420
"""

import numpy as np
from matplotlib import pyplot as plt

# Problem 1
def var_of_means(n):
    """ Create an (n x n) array of values randomly sampled from the standard
    normal distribution. Compute the mean of each row of the array. Return the
    variance of these means.

    Parameters:
        n (int): The number of rows and columns in the matrix.

    Returns:
        (float) The variance of the means of each row.
    """
    data = np.random.normal(size=(n, n))
    row_means = np.mean(data, axis=1) 
    return np.var(row_means)


def prob1():
    ns = np.arange(100, 1001, 100)
    variances = [var_of_means(n) for n in ns]

    plt.plot(ns, variances, marker='o')
    plt.title("Variance of Row Means vs. Matrix Size")
    plt.xlabel("n (Matrix Size n x n)")
    plt.ylabel("Variance of Row Means")
    plt.grid(True)
    plt.show()



# Problem 2
def prob2():
    """ Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_arctan = np.arctan(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y_sin, label='sin(x)')
    plt.plot(x, y_cos, label='cos(x)')
    plt.plot(x, y_arctan, label='arctan(x)')

    plt.title("Plots of sin(x), cos(x), and arctan(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()



# Problem 3
def prob3():
    """ Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    x_left = np.linspace(-2, 0.99, 500)
    x_right = np.linspace(1.01, 6, 500)

    y_left = 1 / (x_left - 1)
    y_right = 1 / (x_right - 1)

    plt.figure(figsize=(10, 6))
    plt.plot(x_left, y_left, 'm--', lw=4)
    plt.plot(x_right, y_right, 'm--', lw=4)

    plt.xlim(-2, 6)
    plt.ylim(-6, 6)

    plt.title("Plot of f(x) = 1 / (x - 1) with discontinuity at x = 1")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)

    plt.show()


    
# Problem 4
def prob4():
    """ Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi], each in a separate subplot of a single figure.
        1. Arrange the plots in a 2 x 2 grid of subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    x = np.linspace(0, 2 * np.pi, 1000)

    y1 = np.sin(x)
    y2 = np.sin(2 * x)
    y3 = 2 * np.sin(x)
    y4 = 2 * np.sin(2 * x)

    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    axs[0, 0].plot(x, y1, 'g-')
    axs[0, 0].set_title("sin(x)")
    axs[0, 0].axis([0, 2*np.pi, -2, 2])

    axs[0, 1].plot(x, y2, 'r--')
    axs[0, 1].set_title("sin(2x)")
    axs[0, 1].axis([0, 2*np.pi, -2, 2])

    axs[1, 0].plot(x, y3, 'b--')
    axs[1, 0].set_title("2 sin(x)")
    axs[1, 0].axis([0, 2*np.pi, -2, 2])

    axs[1, 1].plot(x, y4, 'm:')
    axs[1, 1].set_title("2 sin(2x)")
    axs[1, 1].axis([0, 2*np.pi, -2, 2])

    fig.suptitle("Variations of the Sine Function", fontsize=16)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


    
# Problem 5
def prob5():
    """ Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    data = np.load("FARS.npy")
    hours = data[:, 0]
    longitudes = data[:, 1]
    latitudes = data[:, 2]
    
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    axs[0].plot(longitudes, latitudes, 'k,')
    axs[0].set_title("Crash Locations")
    axs[0].set_xlabel("Longitude")
    axs[0].set_ylabel("Latitude")
    axs[0].set_aspect("equal")

    axs[1].hist(hours, bins=np.arange(25) - 0.5, edgecolor='black')  # 24 bins for 0–23
    axs[1].set_title("Crash Counts by Hour of Day")
    axs[1].set_xlabel("Hour (Military Time)")
    axs[1].set_ylabel("Number of Crashes")
    axs[1].set_xlim(-0.5, 23.5)
    axs[1].set_xticks(np.arange(0, 24, 1))

    plt.tight_layout()
    plt.show()



# Problem 6
def prob6():
    """ Plot the function g(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of g, and one with a contour
            map of g. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Include a color scale bar for each subplot.
    """
    x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
    y = np.linspace(-2 * np.pi, 2 * np.pi, 400)
    X, Y = np.meshgrid(x, y)

    with np.errstate(divide='ignore', invalid='ignore'):
        G = np.sin(X) * np.sin(Y) / (X * Y)
        G[np.isnan(G)] = 1

    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    heatmap = axs[0].pcolormesh(X, Y, G, shading='auto', cmap='viridis')
    axs[0].set_title("Heat Map of g(x, y)")
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("y")
    axs[0].set_xlim(-2 * np.pi, 2 * np.pi)
    axs[0].set_ylim(-2 * np.pi, 2 * np.pi)
    fig.colorbar(heatmap, ax=axs[0])

    contour = axs[1].contourf(X, Y, G, levels=30, cmap='plasma')
    axs[1].set_title("Contour Map of g(x, y)")
    axs[1].set_xlabel("x")
    axs[1].set_ylabel("y")
    axs[1].set_xlim(-2 * np.pi, 2 * np.pi)
    axs[1].set_ylim(-2 * np.pi, 2 * np.pi)
    fig.colorbar(contour, ax=axs[1])

    plt.tight_layout()
    plt.show()

