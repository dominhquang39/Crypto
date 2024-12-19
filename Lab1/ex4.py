def get_binary(n):
    binary = []
    while n > 0:
        binary.append(n % 2)
        n = int(n / 2)
    binary.reverse()
    return binary

def major(binary):
    if (binary.count(0) > binary.count(1)):
        return 0
    return 1

X = 513365
Y = 3355443
Z = 7401712

print(bin(X))
bin_x = get_binary(X)
print(get_binary(X)) 
bin_y = get_binary(Y)
print(get_binary(Y))
bin_z = get_binary(Z)
print(get_binary(Z))

print(major(bin_x))
print(major(bin_y))
print(major(bin_z))

