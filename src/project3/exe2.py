def swap(list_1, list_2):
    print(f"до    {list_1}{list_2}")

    list_max = list_1
    list_min = list_2
    if len(list_1) < len(list_2):
        list_max = list_2
        list_min = list_1

    min_len = len(list_min)

    for i in range(len(list_max)):
        tmp = list_max[i]
        if min_len > i:
            list_max[i] = list_min[i]
            list_min[i] = tmp
        else:
            list_min.append(tmp)

    del list_max[min_len:]
    print(f"после {list_1}{list_2}")

swap([1, 2, 3], [1, 2, 3, 7, 4, 3])
swap([1, 2, 3], [4, 5, 6])

