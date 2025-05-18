# User Input Number Division ask the user to enter two numbers and divide them. Handle errors like division by zero and non-numeric input.

def divide_numbers():
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        
        result = number1 / number2
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numeric input.")
    except Exception as e:
        print(f"Unexpected error: {e}")

divide_numbers()




def index():
    try:
        my_list = ["apple", "banana", "cherry", "date"]
        user_index = int(input("Enter list index (0-3): "))
        print("Element at index", user_index, "is:", my_list[user_index])
    except IndexError:
        print("the index you put is out of range please re enter")
        return user_index
    except ValueError:
        print("the value you have enter should be int and not str or float please re enter the index value! ")
        return user_index
index()



def dictonary():
    dictonari = {
        "name": "mika",
        "age": 16,
        "iq": 1000,
    }
    try:
        key = input("Please enter the key you want to accses etc(name,age,iq)")
        value = dictonari[key]
        return value
    except KeyError:
        print("The key you provided does not exist anymore or have never existed please re enter the value!")
        return key
dictonary()


#Convert String to Integer Ask the user for a number and convert it to an integer. Handle the error if they enter something that can't be converted.

def converter():
    while True:
        value = input("please enter your value: ")
        try:
            integator = int(value)
            return integator
        
        except ValueError:
            print("❌ Error: That is not a valid integer. Please try again.")

converter()


def greet(greeting_func):
    greeting_func()

def say_hello():
    print("Hello!")

def say_bonjour():
    print("Bonjour!")

greet(say_hello)    
greet(say_bonjour)  


def function(number,numbern):
    max = number * numbern
    return max

def infuctor():
    number = int(input("Enter your number1:  "))
    numbern = int(input("enter your number2:  "))
    function(number,numbern)
    return function