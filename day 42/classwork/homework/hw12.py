

def dictonari_calculator(dictonari1):
    total = 0
    for i in dictonari1.values():
        if isinstance(i,(int,float)):
            total += i

    return total

dictonari1 = {
    "name": "mika",
    "number": 10,
    "number2": 2.5,
}

print(dictonari_calculator(dictonari1))

