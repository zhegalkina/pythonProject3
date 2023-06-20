n = int(input("n: "))
m = int(input("m: "))
k = int(input("k: "))
if k < n*m and k%m==0 or k%n==0:
    print("делится")
else:
    print("не делится")
