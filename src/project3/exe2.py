def swap(list1, list2):
    print(f"до    {list1}{list2}")

    len1 = len(list1)
    list1.extend(list2)
    list2[:] = list1[:len1]
    del list1[:len1]

    print(f"после {list1}{list2}")

swap([], [])
swap([1, 2, 3], [1, 2, 3, 7, 4, 3])
swap([1, 2, 3], [4, 5, 6])

