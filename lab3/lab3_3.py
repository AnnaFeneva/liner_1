import numpy as np
import matplotlib.pyplot as plt

def find_linear_approximation(x, y):
    A = np.vstack([np.ones_like(x), x]).T
    coeff = np.linalg.lstsq(A, y, rcond=None)[0]
    y_pred = np.dot(A, coeff)
    error = np.sum((y - y_pred)**2)
    return coeff, y_pred, error

def find_quadratic_approximation(x, y):
    A = np.vstack([np.ones_like(x), x, x**2]).T
    coeff = np.linalg.lstsq(A, y, rcond=None)[0]
    y_pred = np.dot(A, coeff)
    error = np.sum((y - y_pred)**2)
    return coeff, y_pred, error

# Заданные точки
x = np.array([0.1, 0.5, 0.9, 1.3, 1.7, 2.1])
y = np.array([-2.2026, -0.19315, 0.79464, 1.5624, 2.2306, 2.8419])

# Нахождение приближающих многочленов
coeff1, y_pred1, error1 = find_linear_approximation(x, y)
coeff2, y_pred2, error2 = find_quadratic_approximation(x, y)

# Построение графиков
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Исходные данные')
plt.plot(x, y_pred1, label=f'Приближающий многочлен 1-ой степени, ошибка = {error1:.4f}')
plt.plot(x, y_pred2, label=f'Приближающий многочлен 2-ой степени, ошибка = {error2:.4f}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Приближаемая функция и приближающие многочлены')
plt.legend()
plt.show()
