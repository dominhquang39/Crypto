from sympy import mod_inverse
p = 81401
q = 27109
e = 65537
C = 412589464

N = p*q
phi_n = (p-1) * (q-1)
d = mod_inverse(e, phi_n)
M = pow(C, d, N)
input_number = M
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