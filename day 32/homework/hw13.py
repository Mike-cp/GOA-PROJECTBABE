def insert_at_end(lst, item):
    lst.insert(len(lst), item)


my_list = [1, 2, 3]
insert_at_end(my_list, 4) 
print(my_list)  