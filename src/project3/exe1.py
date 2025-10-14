def check(list_1, list_2):

    list_tmp_2 = list_2.copy()
    
    for item_1 in list_1:
        try:
            index = list_tmp_2.index(item_1)  
            list_tmp_2.pop(index)
        except ValueError:
            return False
        
    return True

print(check([1, 2, 3, 3, 4], [1, 2, 3, 7, 4, 3]))
print(check([1, 2, 3, 3, 4, 3], [1, 2, 3, 7, 4, 3]))
print(check([1, 2, 3, 3, 8, 4], [1, 2, 3, 7, 4, 3]))
print(check([1, 2, 3, '3', 4] , [1, 2, 3, 7, 4, 3]))