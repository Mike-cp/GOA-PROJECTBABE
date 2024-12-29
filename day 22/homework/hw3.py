my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


num1 = int(input("შეიყვანეთ პირველი რიცხვი (num1): "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი (num2): "))


if num1 > num2:
    sliced_list = my_list[num1:num2]  
    print("ახალი სია:", sliced_list)
elif num2 > num1:
    sliced_list = my_list[num2:num1]  
    print("ახალი სია:", sliced_list)
else:
    print("სია ცარიელია: []")
