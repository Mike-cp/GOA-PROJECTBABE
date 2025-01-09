def manual_index(main_string, search_string):
    
    main_length = len(main_string)
    search_length = len(search_string)
    
   
    if search_length > main_length:
        return -1
    
   
    for i in range(main_length - search_length + 1):
        if main_string[i:i + search_length] == search_string:
            return i
    return -1  


main_string = "გამარჯობა, როგორ ხარ?"
search_string = "როგორ"
index = manual_index(main_string, search_string)
print(f"ინდექსზე: {index}")
