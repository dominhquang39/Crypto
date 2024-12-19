a = 123
b = 543
aXorb = []
def get_binary(n):
    binary = []
    while n > 0:
        binary.append(n % 2)
        n = int(n / 2)
    binary.reverse()
    return binary

if __name__ == "__main__":
    a_bin = get_binary(a)
    b_bin = get_binary(b)
    max_len = max(len(a_bin), len(b_bin))
    a_bin = [0] * (max_len - len(a_bin)) + a_bin
    b_bin = [0] * (max_len - len(b_bin)) + b_bin
    print(a_bin)
    print(b_bin)
    for bit_a, bit_b in zip(a_bin, b_bin):
        aXorb.append(bit_a ^ bit_b)
    print(aXorb)
