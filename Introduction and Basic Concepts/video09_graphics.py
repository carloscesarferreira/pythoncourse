import numpy as np
import matplotlib.pyplot as plt
    # imports the libraries

x_values = np.linspace(-2*np.pi, 2*np.pi, 400)
    # define the range of x values

plt.figure(figsize=(8, 6))
plt.plot(x_values, np.sin(x_values), label='sin(x)', color='blue')
plt.title('Sine Function')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()
    # plot sine function

plt.figure(figsize=(8, 6))
plt.plot(x_values, np.cos(x_values), label='cos(x)', color='green')
plt.title('Cosine Function')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.legend()
plt.grid(True)
plt.show()
    # plot cosine function

plt.figure(figsize=(8, 6))
plt.plot(x_values, np.tan(x_values), label='tan(x)', color='red')
plt.title('Tangent Function')
plt.xlabel('x')
plt.ylabel('tan(x)')
plt.ylim(-10, 10)  # limit the y-axis for better visualization
plt.legend()
plt.grid(True)
plt.show()
    # plot tangent function

plt.figure(figsize=(8, 6))
plt.plot(x_values, np.exp(x_values), label='exp(x)', color='purple')
plt.title('Exponential Function')
plt.xlabel('x')
plt.ylabel('exp(x)')
plt.legend()
plt.grid(True)
plt.show()
    # plot exponential function

plt.figure(figsize=(8, 6))
plt.plot(x_values[x_values > 0], np.log(x_values[x_values > 0]), label='log(x)', color='orange')
plt.title('Logarithmic Function')
plt.xlabel('x')
plt.ylabel('log(x)')
plt.legend()
plt.grid(True)
plt.show()
    # plot logaritimic function
