def count_occurrences(main_str, str_to_count):
    
    count = main_str.count(str_to_count)
    
    print("'" + str_to_count + "' appears " + str(count) + " times in the main string.")


main_str = input("Enter the main string: ")
str_to_count = input("Enter the string to count: ")


count_occurrences(main_str, str_to_count)
