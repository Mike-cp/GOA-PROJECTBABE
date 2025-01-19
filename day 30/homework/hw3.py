def upper(list1, list2, list3):
   list = [list1, list2, list3]
   for names in list:
      new = names.upper()
      print(new)
      
   
Enter_names = input("Enter frist list name: ")
Enter_names2 = input("Enter second list name: ")
Enter_names3 = input("Enter third list name: ")

upper(Enter_names, Enter_names2, Enter_names3)
