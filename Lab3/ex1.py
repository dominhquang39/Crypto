input_string = "flow"
list_ascii_num = [ord(i) for i in input_string]
target_binary = []
target_number = 0
def get_binary(n):
    binary = []
    while n > 0:
        binary.append(n % 2)
        n = int(n / 2)
    while len(binary) < 8:
        binary.append(0)
    binary.reverse()
    return binary

for i in list_ascii_num:
    target_binary += get_binary(i)

target_binary.reverse()
for i in range(len(target_binary)):
    if (target_binary[i] == 1):
        target_number += pow(2,i)

print(target_number)



