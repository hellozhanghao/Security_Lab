import string
print(string.printable)
print(string.printable.index('\n'))
print(string.printable.index('~'))
print(string.printable[99])

map = []
for char in string.printable:
    print("map[\'"+char+'\'] = \'\'' )

print(map)

print(' ')