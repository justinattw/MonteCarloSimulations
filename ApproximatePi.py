import random
import matplotlib.pyplot as plt

n = 10 ** 5

# Approximate Pi
in_circle_points = []
out_circle_points = []
total_points = n

for _ in range(n):
    x, y = random.uniform(0, 1), random.uniform(0, 1)
    hypotenuse = (x ** 2 + y ** 2) ** 0.5
    if hypotenuse <= 1:
        in_circle_points.append((x, y))
    else:
        out_circle_points.append((x, y))

in_circle_x, in_circle_y = zip(*in_circle_points)
out_circle_x, out_circle_y = zip(*out_circle_points)

# Plot
plt.scatter(in_circle_x, in_circle_y, c='r', marker='x', label='1')
plt.scatter(out_circle_x, out_circle_y, c='b', marker='x', label='-1')
plt.title('Approximating Pi')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

pi = 4 * len(in_circle_points) / n

print('Approximate Pi: ', pi)
