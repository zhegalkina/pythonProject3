digit = int(input("Число n: "))
for i in range(0, digit+1):
    if i % 2 == 0:
        print(i)


digit = int(input("Число n: "))
for i in range(0, digit+1):
    if digit % i == 0:
        print(i)