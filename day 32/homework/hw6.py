def csv_to_list(csv_string):
    return csv_string.split(',')


csv_string = input("Enter a string of comma-separated values: ")
items_list = csv_to_list(csv_string)
print(items_list)
