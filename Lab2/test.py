import resource, sys

print(36*35*34*33*32*31)
print(36*36*36*36*36*36)

list = "abcdefghijklmnopqrstuvwxyz0123456789"

count = 0

wordset = []
def append(digit, word):

    if len(wordset) % 100000 ==0:
        print(len(wordset), 36*36*36*36*36*36-len(wordset))

    if digit == 0:
        wordset.append(word)
        return
    for letter in list:
        word += letter
        append(digit-1, word)


# resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
# sys.setrecursionlimit(0x100000)

word = ''
append(5, word)

print(len(wordset))



