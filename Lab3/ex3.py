from sympy import mod_inverse
#ex1
p = 251
q = 191
e = 65537
M = 26729

N = p*q
phi_n = (p-1) * (q-1)
d = mod_inverse(e, phi_n)
C = pow(M, e, N)
print(C)

#ex2
# p = 233
# q = 151
# d = 9473
# C = 29600

# N = p*q
# M = pow(C, d, N)
# print(M)
input_number = C
print(bin(input_number))
input_binary = bin(input_number)[2:]
list_input_binary = []
temp_list = []
target_string_list = []

for i in range(-1, -len(input_binary) - 1, -1):
    temp_list.append(input_binary[i])
    if len(temp_list) == 8:
        list_input_binary.append(temp_list)
        temp_list = []

if temp_list:
    while (len(temp_list) < 8):
        temp_list.append(0)
    list_input_binary.append(temp_list)

for binary_number in list_input_binary:
    number = 0
    for i in range(len(binary_number)):
        if int(binary_number[i]) == 1: 
            number += pow(2, i)
    target_string_list.append(chr(number))

print(target_string_list)

print(list_input_binary)
