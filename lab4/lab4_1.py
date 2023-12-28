import numpy as np

# Метод Эйлера
def euler_method(f, x0, y0, h, steps):
    x = x0
    y = y0
    for _ in range(steps):
        y += h * f(x, y)
        x += h
    return y

# Метод Рунге-Кутты 4-го порядка
def runge_kutta_method(f, x0, y0, h, steps):
    x = x0
    y = y0
    for _ in range(steps):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5*h, y + 0.5*k1)
        k3 = h * f(x + 0.5*h, y + 0.5*k2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        x += h
    return y

# Метод Адамса 4-го порядка
def adams_method(f, x0, y0, h, steps):
    x = x0
    y = y0
    y_prev = y0
    f_prev = f(x, y)
    for _ in range(steps):
        x += h
        y_next = y + h * (55*f(x, y) - 59*f_prev + 37*f(x-h, y_prev) - 9*f(x-2*h, y_prev)) / 24
        y_prev = y
        f_prev = f(x, y)
        y = y_next
    return y


# Заданная функция
def f(x, y):
    return (2*x*y - 2*y) / (x**2 - 1)

# Точное решение
def exact_solution(x):
    return x**2 + x + 1

# Значения
x0 = 2
y0 = 7
h = 0.1
steps = int((3 - x0) / h)

# Решение с использованием методов
euler_result = euler_method(f, x0, y0, h, steps)
runge_kutta_result = runge_kutta_method(f, x0, y0, h, steps)
adams_result = adams_method(f, x0, y0, h, steps)

# Оценка погрешности
def runge_romberg(h1, y1, h2, y2, order):
    return y2 + (y2 - y1) / ((h2/h1)**order - 1)

h_half = h / 2
steps_double = int((3 - x0) / h_half)
euler_result_half = euler_method(f, x0, y0, h_half, steps_double)
runge_kutta_result_half = runge_kutta_method(f, x0, y0, h_half, steps_double)
adams_result_half = adams_method(f, x0, y0, h_half, steps_double)

euler_romberg = runge_romberg(h, euler_result, h_half, euler_result_half, 1)
runge_kutta_romberg = runge_romberg(h, runge_kutta_result, h_half, runge_kutta_result_half, 4)
adams_romberg = runge_romberg(h, adams_result, h_half, adams_result_half, 4)

# Сравнение с точным решением
exact_values = [exact_solution(x0 + i*h) for i in range(steps+1)]

print("Метод Эйлера:", euler_result, "Погрешность (Рунге-Ромберг):", euler_romberg)
print("Метод Рунге-Кутты:", runge_kutta_result, "Погрешность (Рунге-Ромберг):", runge_kutta_romberg)
print("Метод Адамса:", adams_result, "Погрешность (Рунге-Ромберг):", adams_romberg)
print("Точное решение:", exact_values)
