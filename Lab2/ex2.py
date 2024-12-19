import math
A = [290345, 218585, 143231, 164172, 155768, 423151, 239707, 153544, 287390, 480837]

count = 0
for i in range(0, len(A)):
    for j in range(i+1, len(A)):
        if math.gcd(A[i], A[j]) == 1:
            count += 1
            print(f"{A[i]} and {A[j]} is coprime")

print(count)