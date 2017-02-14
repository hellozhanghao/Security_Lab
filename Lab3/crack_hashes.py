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
        else:
            hash_value = new_split[1][:-2].split(" ")[0]
            word = new_split[1][33:-2]
            if hashlib.md5(word.encode('ascii')).hexdigest() != hash_value:
                print("Wrong hash: ", hash_value, word)
            # else:
            #     print("Corect hash: ", hash_value, word)


    new = fin.readline()

fin.close()


# save unsolved hashes:

fout = open("unsolved.txt",'w')

ans =''
for word in hashlist:
    ans += word
    ans += '\n'

fout.write(ans[:-1])
fout.close()


print("Number of unsoved hashes: ", len(hashlist))
#
# # fin = open("/Users/zhanghao/Downloads/hashesorg251015.txt", 'rb')
# alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # alphabet = "0123456789"
#
#
# def append(digit, word):
#     # print(digit,word)
#
#     if digit == 0:
#         hash = hashlib.md5(word.encode('ascii')).hexdigest()
#         if hash in hashlist:
#             print(word, hash)
#             return
#     else:
#         for i in alphabet:
#             append(digit - 1, word + i)
#
#
#


# print("alphabut 7")
# append(7, '')
# print("alphabut 8")
# append(8, '')
# print("alphabut 9")
# append(9, '')
#
#





# fin = open("/Users/zhanghao/Movies/DCHTPassv1.0.txt")

# fin = open("/Users/zhanghao/Downloads/wordlist.txt")

# fin = open("/Users/zhanghao/Downloads/hk_hlm_founds.txt")
#
# fin = open("password.txt")

# fin = open("/Users/zhanghao/Downloads/InsideProFull.txt")

# https://hashkiller.co.uk/md5-decrypter.aspx



# fin = open("/Users/zhanghao/Downloads/HyperionOnHackForumsNetRELEASE.txt")


# fin = open("/Users/zhanghao/Downloads/passwords_collection.txt")

fin = open("/Users/zhanghao/Downloads/Wordlist_82_million.txt")
print("Wordlist_82_million")




word = fin.readline()


while word != "":
    # count += 1

    # if count % 1000000 == 0:
    #     print(count)

    if hashlib.md5(word[:-1].encode('utf-8')).hexdigest() in hashlist:
        print(word[:-1], hashlib.md5(word.encode('utf-8')).hexdigest() )

    word = fin.readline()
