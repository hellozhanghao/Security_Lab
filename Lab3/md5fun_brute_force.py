import hashlib, time
import pprint

pp = pprint.PrettyPrinter(indent=5)

start_time = time.time()

fin = open("hash5.txt", newline='\n')
hash_dict = dict()
c = fin.readline()
while c != "":
    hash_dict[c[:-1]] = ''
    c = fin.readline()

fin.close()

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"


def append(digit, word):
    # print(digit,word)

    if '' not in hash_dict.values():
        return

    if digit == 0:
        hash = hashlib.md5(word.encode('ascii')).hexdigest()
        if hash in hash_dict:
            print("hit!", word, hash)
            hash_dict[hash] = word
            return
    else:
        for i in alphabet:
            append(digit - 1, word + i)


append(9, '')
print("Time used: ", round(time.time() - start_time, 2),"seconds")
pp.pprint(hash_dict)
