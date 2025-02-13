def manual(main_list, item):
    main_list.insert(len(main_list), item)  
    print(main_list)  

main = ["apple", "p;a", "oidwad", "ah", "di", "blo", "va"]
items = input("Enter value: ")
manual(main, items)

