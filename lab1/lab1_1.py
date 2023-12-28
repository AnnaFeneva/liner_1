import numpy as np


def lu_decomposition_with_pivoting(matrix):
    n = len(matrix)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    P = [[0.0] * n for _ in range(n)]
    for i in range(n):
        P[i][i] = 1.0
    for i in range(n):
        max_val = max(abs(matrix[i][j]) for j in range(n))
        if max_val == 0:
            return None, None, None  # Матрица вырожденная
        for j in range(n):
            if i <= j:
                U[i][j] = matrix[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
            if i > j:
                L[i][j] = (matrix[i][j] - sum(L[i][k] * U[k][j] for k in range(j))) / U[j][j]
    return L, U, P


def solve_lu_decomposition(L, U, P, b):
    n = len(L)
    y = np.zeros(n)
    x = np.zeros(n)

    # Решаем Ly = Pb
    for i in range(n):
        y[i] = np.dot(P[i], b)
        for j in range(i):
            y[i] -= L[i][j] * y[j]

    # Решаем Ux = y
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return x



def determinant_from_lu(U, P):
    det_U = 1.0
    for i in range(len(U)):
        det_U *= U[i][i]
    det_P = 1.0
    for i in range(len(P)):
        det_P *= P[i][i]
    return det_U * det_P

def inverse_from_lu(L, U, P):
    n = len(L)
    inv = [[0.0] * n for _ in range(n)]
    for i in range(n):
        b = [0.0] * n
        b[i] = 1.0
        x = solve_lu_decomposition(L, U, P, b)
        for j in range(n):
            inv[j][i] = x[j]
    return inv

# Пример использования
A = [[-5.0, -1.0, -3.0, -1.0], [-2.0, 0.0, 8.0, -4.0], [-7.0, -2.0, 2.0, -2.0], [2.0, -4.0, -4.0, 4.0]]
b = [18.0, -12.0, 6.0, -12.0]

L, U, P = lu_decomposition_with_pivoting(A)
x = solve_lu_decomposition(L, U, P, b)
det = determinant_from_lu(U, P)
inv = inverse_from_lu(L, U, P)

print("Матрица L:")
for row in L:
    print(row)
print("Матрица U:")
for row in U:
    print(row)
print("Решение СЛАУ:")
print(x)
print("Определитель матрицы A:")
print(det)
print("Обратная матрица к матрице A:")
for row in inv:
    print(row)
