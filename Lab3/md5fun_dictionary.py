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

    perms = [''.join(p) for p in permutations(word)]
    for perm in perms:
        wordset.add(perm)
print("set operation finished.")
fin.close()


fin  = open("hash5.txt", newline='\n')
hash_dict = dict()
c = fin.readline()
while c != "":
    hash_dict[c[:-1]] = ''
    c = fin.readline()

count = 0

for word in wordset :
    hash = hashlib.md5(word.encode('ascii')).hexdigest()
    if hash in hash_dict:
        count += 1
        print("hit!",count, word)
        hash_dict[hash] = word


pp.pprint(hash_dict)

print(time.time()-start_time)
#
# {    '0d5b558d5f6744deaaf5b016c6c77a57': 'tpoin',
#      '1b31905c59f481958d2eb72158c27ac7': 'egunb',
#      '1b4baba3ae3be69857b323cf6b7fcd80': '',
#      '644674d142ba2174a80889f833b32563': 'owso9',
#      '6e313b70d12de950443527a33d802b76': 'mlhdi',
#      '78c1b8edd1bc3ffc438432479289a9e1': 'nized',
#      '81466b6bb4be5a48e2230be1338bcde6': 'lou0g',
#      '836626589007d7dd5304c8d22815fffc': 'di5gv',
#      '96f6065d8f2dd1376eff88fba65d1d83': 'cance',
#      'a74edf83748e3c4fa5f31ec10bad79db': 'dsmto',
#      'a8218c67a5b4e652e30a59372e07df59': 'hed4e',
#      'a92b66a9802704ca8616c4b092378272': 'opmen',
#      'd4efdba5e9725e77c9b9051fa8136f0a': 'tthel',
#      'ddaafa5d551a582bc924d09cc8d33ee5': 'aseas',
#      'de952f5454fb0ee79bca249f80e9fe8f': 'ofror'}