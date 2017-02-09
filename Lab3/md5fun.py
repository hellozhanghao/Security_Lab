import timeit
import hashlib
from itertools import permutations
import pprint
import time
import copy

pp = pprint.PrettyPrinter(indent=5)

def replace(s, digit, number):
    new = list(s)
    new[digit] = number
    return ''.join(new)

start_time = time.time()

m = hashlib.md5()
m.update("hello".encode('ascii'))
ha = m.hexdigest()
#
# print(hashlib.md5("hello".encode('ascii')).hexdigest())


fin  = open("words5.txt", newline='\n')
wordlist = []
c = fin.readline()
while c != "":
    wordlist.append(c[:-1])
    c = fin.readline()

wordset = set()

count = 0

for word in wordlist:

    count += 1

    if count % 10000 == 0 :
        print("Set operation progress: ",count, "  size: ", len(wordset))

    # print(word)
    perms = [''.join(p) for p in permutations(word)]
    for perm in perms:
        wordset.add(perm)
print("set operation finished.")
fin.close()

count = 0

print("adding numbers....")
word_with_number = set()
for word in wordset:
    for digit in [0, 1, 2, 3, 4]:
        for number in ['0','1','2','3','4','5','6','7','8','9','0']:
            new_word = replace(word, digit, number)
            if new_word not in wordset:
                print("adding ", new_word)
                count += 1

                if count % 10000 == 0:
                    print("adding numbers progress: ", count, "%  size: ", len(wordset))
                word_with_number.add(new_word)



fin  = open("hash5.txt", newline='\n')
hash_dict = dict()
c = fin.readline()
while c != "":
    hash_dict[c[:-1]] = ''
    c = fin.readline()
#
# print(wordset)
# print(hash_dict)

count = 0

for word in wordset:
    hash = hashlib.md5(word.encode('ascii')).hexdigest()
    if hash in hash_dict:
        count += 1
        print("hit!",count, word)
        hash_dict[hash] = word


pp.pprint(hash_dict)

print(time.time()-start_time)