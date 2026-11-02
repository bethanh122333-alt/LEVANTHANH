def phantich(n):
    i = 2
    while n > 1:
        if n % i == 0:
            print(i,end=" ")
            n = n // i
        else:
            i += 1
n = int(input("Nhập n: "))
print("Các thừa số nguyên tố: ", end=" ")
phantich(n)