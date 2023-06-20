def read_input():
    in_str = input("Enter the line: ").split()
    x, sing, y = in_str
    return int(x), sing, int(y)
def calculate(x, sign, y)
    if sign== "+":
        return x+y
    elif sign == "-":
        return x-y
    elif sign == "*":
        return x*y
    else:
        if y==0:
            return "ZeroDivision Error"
        else:
            return x/y

if __name__ == "__main__":
    read_input()