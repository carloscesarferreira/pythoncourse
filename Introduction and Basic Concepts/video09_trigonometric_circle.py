import numpy as np
import matplotlib.pyplot as plt

angle = 2 * np.pi / 3
    # define angle for sine, cosine, and tangent

plt.figure(figsize=(8, 8))
circle = plt.Circle((0, 0), 1, color='black', fill=False)
plt.gca().add_artist(circle)
    # plot the unit circle


points = [(0, 0), (0, 1), (1, 0), (-1, 0), (0, -1)]
for point in points:
    plt.plot(point[0], point[1], 'ro')
    # plot the points (0,0), (0,1), (1,0), (-1,0), (0,-1)

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
    # plot the x-axis and y-axis

plt.text(1.05, 0.1, '1', fontsize=10)
plt.text(-1.15, 0.1, '-1', fontsize=10)
plt.text(0.1, 1.05, '1', fontsize=10)
plt.text(0.1, -1.15, '-1', fontsize=10)
    # mark 1 and -1 on the x-axis and y-axis

plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
    # set equal aspect ratio and limits

plt.axis('off')
    # remove box around the graph

plt.title('Trigonometric Circle')
plt.xlabel('x')
plt.ylabel('y')
    # add title and labels for x and y axes

plt.show()
    # show plot
