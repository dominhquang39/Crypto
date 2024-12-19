B = [99, 100, 126, 120, 101, 56, 105, 120, 115, 122, 126, 101, 113, 59, 121,
126, 57, 122, 85, 58, 100, 85, 96, 58, 127, 120, 100, 57, 115, 119]
k = 10
hidden_numbers = [number ^ k for number in B]
message = [chr(number) for number in hidden_numbers]
for i in range(len(message)):
    print(message[i], end="")
