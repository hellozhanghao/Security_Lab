import string
filein = "secret"
fileout = "unlock secret"

fin = open(filein, newline='\n')  # by default, read mode
c = fin.read()  # read in file into c

freq = dict()
for char in c:
    if char not in freq:
        freq[char] = 1
    else:
        freq[char] += 1


sorted_freq = sorted(freq, key=lambda x : freq[x],reverse=True)

print(sorted_freq)
print(freq)

print()
print(string.printable)



 # original = 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
cipher =     "m*************a******************i************u******** *****************************t*********"


key = 3
ans = ""
for char in c:
    char = cipher[string.printable.index(char)]
    ans += char
print(c)
print(ans)

