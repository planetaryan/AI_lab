import random
import math

# Define the function to be optimized
def f(x):
    return 2*x**2 - 3*x + 7 

# Define the Hill Climbing algorithm
def hill_climbing(max_iterations, step_size, x_min, x_max):
    # Initialize the current state
    x_current = random.uniform(x_min, x_max)
    f_current = f(x_current)

    # Iterate until max_iterations is reached or no better neighbor is found
    for i in range(max_iterations):
        # Generate a random neighbor
        x_neighbor = x_current + random.uniform(-step_size, step_size)
        f_neighbor = f(x_neighbor)

        # If the neighbor is better, move to the neighbor
        if f_neighbor > f_current and x_min <= x_neighbor <= x_max:
            x_current = x_neighbor
            f_current = f_neighbor

    # Return the best state found
    return x_current, f_current

# Set the algorithm parameters
max_iterations = 100000
step_size = 0.1
x_min = -10
x_max = 10

# Run the Hill Climbing algorithm
x_best, f_best = hill_climbing(max_iterations, step_size, x_min, x_max)

# Print the results
print("Best solution found: x = {:.4f}, f(x) = {:.4f}".format(x_best, f_best))

#https://github.com/Jason-Yuan/8PuzzleGameSovler.git
