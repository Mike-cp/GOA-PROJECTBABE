# 10) Write a function that takes a list and an item, and appends the item to the list.

def appender(list,item):
    list.append(item)
    return list

list = ["apple","Idk","Text","Random fruit","IDONTKNOW"]
item = input("Enter inputer item: ")
print(appender(list,item))