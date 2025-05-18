
list = [i for i in range(1,11)]
print(list)

list1 = [x**2 for x in range(1,6)]
print(list1)

list2 = [n for n in range(1,20) if n % 2 == 0]
print(list2)

words = ["goa" , "basketball" , "nika"]
list3 = [y[0] for y in words]
print(list3)

words2 = ["goa" , "basketball" , "nika"]
list4 = [m.upper() for m in words2]
print(list4)

list5 = [h for h in range(1,51) if h % 3 == 0]
print(list5)

words3 = ["goa" , "txa" , "basketball" , "nika"]
list6 = [u for u in words3 if len(u)<4]
print(list6)

celsius_temps = [0, 20, 37, 1]
fahrenheit_temps = [(c * 9/5) + 32 for c in celsius_temps]
print(celsius_temps)
print(fahrenheit_temps)

words4 = ["nika" , "kjhfg" , "dfrrfva" , "rfg" , "gta"]
list8 = [c for c in words4 if len(c)> 5]
print(list8)