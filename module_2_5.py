def get_matrix(n, m, value):
    matrix = []
    for k in range(n):
        inner_list = []
        matrix.append(inner_list)
        for x in range(m):
            inner_list.append(value)
    return matrix
result1 = get_matrix(6, 4, 1)
result2 = get_matrix(2, 4, 17)
result3 = get_matrix(5, 5, 20)
print(result1)
print(result2)
print(result3)