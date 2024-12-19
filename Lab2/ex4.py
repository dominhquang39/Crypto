x, y = 0, 1

def gcdExtended(a, b):
    global x, y

    if (a == 0):
        x = 0
        y = 1
        return b

    gcd = gcdExtended(b % a, a)
    x1 = x
    y1 = y

    x = y1 - (b // a) * x1
    y = x1

    return gcd


def modInverse(A, M):

    g = gcdExtended(A, M)
    if (g != 1):
        print("Inverse doesn't exist")

    else:

        res = (x % M + M) % M
        print("Modular multiplicative inverse is ", res)


if __name__ == "__main__":
    A = 65537
    M = 35256

    modInverse(A, M)