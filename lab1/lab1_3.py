def solve_simple_iteration(matrix, vector_b, precision, max_iterations=1000):
    n = len(matrix)
    x = [0 for _ in range(n)]
    iterations = 0
    while True:
        iterations += 1
        x_new = [0 for _ in range(n)]
        for i in range(n):
            sum = 0
            for j in range(n):
                if j != i:
                    sum += matrix[i][j] * x[j]
            x_new[i] = (vector_b[i] - sum) / matrix[i][i]
        if max(abs(a - b) for a, b in zip(x, x_new)) < precision:
            break
        x = x_new
        if iterations > max_iterations:
            print('Warning: The method of simple iterations did not converge.')
            break
    return x, iterations

def solve_seidel(matrix, vector_b, precision=0.0001, max_iterations=1000):
    n = len(matrix)
    x = [0 for _ in range(n)]
    iterations = 0
    while True:
        iterations += 1
        x_new = [0 for _ in range(n)]
        for i in range(n):
            sum = 0
            for j in range(n):
                if j != i:
                    sum += matrix[i][j] * x[j]
            x_new[i] = (vector_b[i] - sum) / matrix[i][i]
        if max(abs(a - b) for a, b in zip(x, x_new)) < precision:
            break
        x = x_new
        if iterations > max_iterations:
            print('Warning: The Seidel method did not converge.')
            break
    return x, iterations




A = [[21, -6, -9, -4], [-6, 20, -4, 2], [-2, -7, -20, 3], [4, 9, 6, 24]]
b = [127, -144, 236, -5]
eps = 0.000000001

x_iter, count_iter = solve_simple_iteration(A, b, eps)
print("x методом итераций ", x_iter, " кол-во итераций ", count_iter)

x_zeidel, zeid_iter = solve_seidel(A, b, eps)
print("x методом Зейделя ", x_zeidel, " кол-во итераций ", zeid_iter)
