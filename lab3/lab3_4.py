import numpy as np

# Заданные точки
x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
y = np.array([0.0, 2.0, 3.4142, 4.7321, 6.0])

# Точка, в которой нужно вычислить производные
X_star = 2.0

# Вычисление первой производной (метод конечных разностей)
dx = x[2] - x[1]
dy_dx = (y[2] - y[1]) / dx  # Первая производная в точке x=0

# Вычисление второй производной (метод конечных разностей)
# Вторая производная в точке x=0

print(f"Первая производная в точке x={X_star}: {dy_dx}")
print(f"Вторая производная в точке x={X_star}: {d2y_dx2}")
