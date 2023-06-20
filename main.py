digit = int(input("Число: "))
if digit % 4 ==0 and digit % 100 != 0 or digit % 400 == 0:
    print("Високосный")
else:
    print("нет")
