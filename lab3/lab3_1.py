import numpy as np

# Заданные точки
X = np.array([0.1, 0.5, 0.9, 1.3])
Y = np.log(X) + X
X_star = 0.8

# Интерполяционный многочлен Лагранжа
def lagrange_interpolation(x, X, Y):
    n = len(X)
    result = 0
    for i in range(n):
        term = Y[i]
        for j in range(n):
            if j != i:
                term *= (x - X[j]) / (X[i] - X[j])
        result += term
    return result

lagrange_result = lagrange_interpolation(X_star, X, Y)

# Интерполяционный многочлен Ньютона
def newton_interpolation(x, X, Y):
    n = len(X)
    F = np.zeros((n, n))
    F[:,0] = Y
    for j in range(1, n):
        for i in range(n-j):
            F[i,j] = (F[i+1,j-1] - F[i,j-1]) / (X[i+j] - X[i])
    result = 0
    for j in range(n):
        term = F[0,j]
        for k in range(j):
            term *= (x - X[k])
        result += term
    return result

newton_result = newton_interpolation(X_star, X, Y)

# Вычисление погрешности интерполяции
actual_value = np.log(X_star) + X_star
lagrange_error = abs(actual_value - lagrange_result)
newton_error = abs(actual_value - newton_result)

print("Интерполяционный многочлен Лагранжа в точке X*:", lagrange_result)
print("Погрешность интерполяции для многочлена Лагранжа:", lagrange_error)
print("Интерполяционный многочлен Ньютона в точке X*:", newton_result)
print("Погрешность интерполяции для многочлена Ньютона:", newton_error)
