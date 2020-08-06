def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Wybierz operacje. \n1.Dodawanie\n2.Odejmowanie\n3.Mnożenie\n4.Dzielenie")

num1 = float(input("Podaj pierwszą liczbę: "))
while True:

    choice = input("Wybierz operację(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num2 = float(input("Podaj drugą liczbę: "))

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        else:
            result = divide(num1, num2)
        print(result)
        break
    else:
        print("Błędna wartość, podaj poprawną: ")