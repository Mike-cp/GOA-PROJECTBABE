def append_items(original_list, items_to_add):
    for item in items_to_add:
        original_list.append(item)


my_list = [1, 2, 3]
new_items = [4, 5, 6]

append_items(my_list, new_items)
print(my_list)  