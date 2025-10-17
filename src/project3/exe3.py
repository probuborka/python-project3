def multiplication(m1, m2):

    # Проверка
    # на пустоту
    if not m1 or not m2:
        print("Одна или несколько матриц пустые")
        return
    
    # на количество столбцов в матрице
    check_column_count = lambda m: (lambda first_len=len(m[0]) : all(len(r) == first_len for r in m))()
    if not check_column_count(m1) or not check_column_count(m2):
        print("Количество столбцов должно быть одинаковым для всех строк")
        return
        
    # на количество строк m1 и столбцов m2
    if len(m1[0]) != len(m2):
        print("Число столбцов матрицы 1 не равно числу строк матрицы 2")
        return

    # Создаем матрицу
    col_len = len(m2[0])
    result = [[0] * col_len for _ in range(len(m1))]
    
    # Умножаем
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    
    return result

print(multiplication([],[]))
print(multiplication([[1, 2], [3, 4]],[[5], [8,2]]))
print(multiplication([[1, 2], [3, 4]],[[5, 6], [7, 8]]))
print(multiplication([[1, 2], [3, 4]],[[5], [8]]))