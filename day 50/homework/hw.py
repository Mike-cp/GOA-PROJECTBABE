# 1) User Input check
try:
    user_input = input("Enter a number: ")
    number = float(user_input)  # ცდილობს ციფრად გადაკეთებას
    print(f"You entered the number: {number}")
except ValueError:
    print("Error: That's not a valid number!")

# 2) IndexError handling
my_list = [10, 20, 30]
try:
    print(my_list[5])  # არარსებული ინდექსი
except IndexError:
    print("Error: List index out of range!")

# 3) TypeError handling
try:
    result = "Hello" + 5  # ჯვრის ოპერაცია განსხვავებული ტიპით
except TypeError:
    print("Error: Cannot add a string and an integer!")

# 5) ერორების დროის ახსნა  
print("\nგამოყენებული ერორები:\n"
      "ValueError - თუ მომხმარებლის შეყვანა ციფრი არ არის\n"
      "IndexError - თუ მცდელობაა სიიდან არარსებული ინდექსის გამოძახება\n"
      "TypeError - როცა ცდის შეერთება განსხვავებული ტიპის მონაცემები, მაგალითად ტექსტი და რიცხვი\n")
