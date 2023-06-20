deg = int(input("Введите температуру: "))
keyword = input("в: ")
def function(deg, keyword):
    if keyword == 'c':
        return deg*1.8+32
    elif keyword == 'f':
        return (deg-32)/1.8
print(function(deg, type))
