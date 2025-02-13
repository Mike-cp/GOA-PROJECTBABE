def append_all(target_list, source_list):
    for item in source_list:
        target_list.append(item)


list1 = [1, 2, 3]
list2 = [4, 5, 6]

append_all(list1, list2)
print(list1)  
