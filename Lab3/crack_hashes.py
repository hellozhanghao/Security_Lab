import hashlib

hashlist = set()

fin = open("hashes.txt",  newline='\n')

new = fin.readline()

while new != "":
    new_split = new.split('. ')
    if len(new_split)==2:
        if len(new_split[1].split(" "))==1:
            if len(new_split[1]) == 34:
                hashlist.add(new_split[1][:-2])
            else:
                hashlist.add(new_split[1])

    new = fin.readline()

fin.close()

print("Number of unsoved hashes: ", len(hashlist))

# fin = open("/Users/zhanghao/Downloads/hashesorg251015.txt", 'rb')
# alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = "0123456789"


def append(digit, word):
    # print(digit,word)

    if digit == 0:
        hash = hashlib.md5(word.encode('ascii')).hexdigest()
        if hash in hashlist:
            print(word, hash)
            return
    else:
        for i in alphabet:
            append(digit - 1, word + i)


append(8, '')







# fin = open("/Users/zhanghao/Movies/DCHTPassv1.0.txt")
#
# word = fin.readline()[:-1]
#
# # count = 0
#
# while word != "\n":
#     # count += 1
#
#     # if count % 1000000 == 0:
#     #     print(count)
#
#     if hashlib.md5(word.encode('ascii')).hexdigest() in hashlist:
#         print(word, hashlib.md5(word.encode('ascii')).hexdigest() )
#
#     word = fin.readline()[:-1]