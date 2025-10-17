def print_result(func):
    def wrapper(*args, **kwargs):
        print(f"до    {args}")
        result = func(*args, **kwargs)
        print(f"после {args}")
        return result
    return wrapper

def swap(list1, list2):
    len1 = len(list1)
    list1.extend(list2)
    list2[:] = list1[:len1]
    del list1[:len1]

p = print_result(swap)
p([], [])
p([1, 2, 3], [1, 2, 3, 7, 4, 3])
p([1, 2, 3], [4, 5, 6])

