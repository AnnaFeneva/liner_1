import numpy as np

# Функция для вычисления значения функции y = x^2 / (x^4 + 256)
def f(x):
    return x**2 / (x**4 + 256)

# Метод прямоугольников
def rectangle_method(f, a, b, h):
    n = int((b - a) / h)
    integral = h * sum(f(a + i*h + h/2) for i in range(n))
    return integral

# Метод трапеций
def trapezoidal_method(f, a, b, h):
    n = int((b - a) / h)
    integral = h/2 * (f(a) + 2*sum(f(a + i*h) for i in range(1, n)) + f(b))
    return integral

# Метод Симпсона
def simpsons_method(f, a, b, h):
    n = int((b - a) / h)
    x = np.linspace(a, b, n+1)
    integral = h/3 * (f(a) + 4*sum(f(x[i]) for i in range(1, n, 2)) + 2*sum(f(x[i]) for i in range(2, n-1, 2)) + f(b))
    return integral

# Значения шагов
h1 = 0.5
h2 = 0.25

# Вычисление интегралов
I_rectangle_h1 = rectangle_method(f, 0, 2, h1)
I_trapezoidal_h1 = trapezoidal_method(f, 0, 2, h1)
I_simpsons_h1 = simpsons_method(f, 0, 2, h1)

I_rectangle_h2 = rectangle_method(f, 0, 2, h2)
I_trapezoidal_h2 = trapezoidal_method(f, 0, 2, h2)
I_simpsons_h2 = simpsons_method(f, 0, 2, h2)

# Оценка погрешности методом Рунге-Ромберга
p = 2  # Порядок точности метода Симпсона
error_rectangle = (I_rectangle_h1 - I_rectangle_h2) / (2**p - 1)
error_trapezoidal = (I_trapezoidal_h1 - I_trapezoidal_h2) / (2**p - 1)
error_simpsons = (I_simpsons_h1 - I_simpsons_h2) / (2**p - 1)

# Вывод результатов
print("Метод прямоугольников:")
print(f"Значение интеграла с шагом h1: {I_rectangle_h1}, погрешность: {error_rectangle}")
print(f"Значение интеграла с шагом h2: {I_rectangle_h2}")

print("\nМетод трапеций:")
print(f"Значение интеграла с шагом h1: {I_trapezoidal_h1}, погрешность: {error_trapezoidal}")
print(f"Значение интеграла с шагом h2: {I_trapezoidal_h2}")

print("\nМетод Симпсона:")
print(f"Значение интеграла с шагом h1: {I_simpsons_h1}, погрешность: {error_simpsons}")
print(f"Значение интеграла с шагом h2: {I_simpsons_h2}")
