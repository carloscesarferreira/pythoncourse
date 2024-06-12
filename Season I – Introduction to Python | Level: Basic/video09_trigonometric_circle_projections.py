import numpy as np
import matplotlib.pyplot as plt

angle = 2 * np.pi / 3
    # define angle for sine, cosine, and tangent

sine_value = np.sin(angle)
cosine_value = np.cos(angle)
tangent_value = np.tan(angle)
    # calculate sine, cosine, and tangent values for the angle

plt.figure(figsize=(8, 8))
circle = plt.Circle((0, 0), 1, color='black', fill=False)
plt.gca().add_artist(circle)
    # plot the unit circle

sin_projection, = plt.plot([0, cosine_value], [sine_value, sine_value], color='blue', linestyle='--')  # projection on x-axis (cos)
cos_projection, = plt.plot([cosine_value, cosine_value], [0, sine_value], color='green', linestyle='--')  # projection on y-axis (sin)
    # plot projections of radius on x-axis and y-axis for sine

tan_projection, = plt.plot([0, cosine_value], [0, sine_value], color='red', linestyle='-')  # projection on circle (tan)
    # plot projection of radius on circle for tangent
plt.plot(cosine_value, sine_value, 'ro')
    # plot the point on the circle for tangent

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

plt.legend([sin_projection, cos_projection, tan_projection], ['sin', 'cos', 'tan'])
    # add legend for the projections

plt.show()
    # show plot
