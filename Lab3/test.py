for digit in [0, 1, 2, 3, 4]:
    print(digit)

str = "hello"


def replace(s, digit, number):
    new = list(s)
    new[digit] = number
    return ''.join(new)

print(replace("hello", 1, '0'))