def multiplication(m1, m2):
    l2 = len(m2[0])

    result = []
    for s_m1 in m1:
        s_result = []
        for i_m2 in range(l2):
            e = 0
            i_m1 = -1
            for v_m1 in s_m1:
                i_m1 += 1
                e += v_m1 * m2[i_m1][i_m2]
            s_result.append(e)
        result.append(s_result)
    
    return result

print(multiplication([[1, 2], [3, 4]],[[5, 6], [7, 8]]))
print(multiplication([[1, 2], [3, 4]],[[5], [8]]))