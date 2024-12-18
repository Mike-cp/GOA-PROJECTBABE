
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

index = int(input("შეიყვანეთ ინდექსი: "))


if 0 <= index < len(numbers):
    print("პირდაპირი ინდექსი:", numbers[index])
elif -len(numbers) <= index <= -1:
    print("უარყოფითი ინდექსი:", numbers[index])
else:
    print("მოცემული ინდექსი არ შედის სიის ფარგლებში!")
