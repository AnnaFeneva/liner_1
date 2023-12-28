import math

def f(x):
    return x * math.exp(x) + x**2 - 1

def f_prime(x):
    return math.exp(x) + x * math.exp(x) + 2 * x

def newton_method(f, f_prime, x0, epsilon, max_iterations):
    iteration = 0
    while True:
        x1 = x0 - f(x0) / f_prime(x0)
        if abs(x1 - x0) < epsilon or iteration >= max_iterations:
            return x1
        x0 = x1
        iteration += 1

def simple_iteration_method(f, x0, epsilon, max_iterations):
    iteration = 0
    while True:
        x1 = math.exp(-x0) * (1 - x0**2)
        if abs(x1 - x0) < epsilon or iteration >= max_iterations:
            return x1
        x0 = x1
        iteration += 1

result_simple_iteration = simple_iteration_method(f, 0.5, 0.01, 10000000)
print(result_simple_iteration)

result_newton = newton_method(f, f_prime, 0.5, 0.01, 10000000)
print(result_newton)
