def remove_elements(main_list, indexes_list):
    for index in sorted(indexes_list, reverse=True):
        if 0 <= index < len(main_list):
            main_list.pop(index)  
    return main_list
