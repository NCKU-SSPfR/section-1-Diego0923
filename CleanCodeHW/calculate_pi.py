import random

# Constant settings
RADIUS = 1
NUM_POINTS = 1000000
AREA_FACTOR = 4
SQUARE_EXPONENT = 2
POINT_COUNT_INCREMENT = 1

points_inside_circle = 0

# Randomly generate points and count those inside the circle
for point in range(NUM_POINTS):
    x_coordinate = random.uniform(-RADIUS, RADIUS)
    y_coordinate = random.uniform(-RADIUS, RADIUS)
    if x_coordinate**SQUARE_EXPONENT + y_coordinate**SQUARE_EXPONENT <= RADIUS**SQUARE_EXPONENT:
        points_inside_circle += POINT_COUNT_INCREMENT

# Estimate pi based on the number of points inside the circle
estimated_pi = (points_inside_circle / NUM_POINTS) * AREA_FACTOR

print(f"Estimated value of pi is: {estimated_pi}")
