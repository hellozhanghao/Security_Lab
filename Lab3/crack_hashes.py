import hashlib

hashlist = set()

fin = open("hashes.txt",  newline='\n')
fout = open("result.csv", 'w')

new = fin.readline()
ans = ''

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
            ans += hash_value
            ans += ','
            ans += word
            ans += '\n'

            if hashlib.md5(word.encode('ascii')).hexdigest() != hash_value:
                print("Wrong hash: ", hash_value, word)
            # else:
            #     print("Corect hash: ", hash_value, word)


    new = fin.readline()

fin.close()
fout.write(ans)
fout.close()


# save unsolved hashes:

fout = open("unsolved.txt",'w')

ans =''
for word in hashlist:
    ans += word
    ans += '\n'

fout.write(ans[:-1])
fout.close()


print("Number of unsoved hashes: ", len(hashlist))



# for brute force

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



# for using dictionary

# fin = open("/Users/zhanghao/Movies/DCHTPassv1.0.txt")

# fin = open("/Users/zhanghao/Downloads/wordlist.txt")

# fin = open("/Users/zhanghao/Downloads/hk_hlm_founds.txt")
#
# fin = open("password.txt")

# fin = open("/Users/zhanghao/Downloads/InsideProFull.txt")

# https://hashkiller.co.uk/md5-decrypter.aspx

# fin = open("/Users/zhanghao/Downloads/HyperionOnHackForumsNetRELEASE.txt")

# fin = open("/Users/zhanghao/Downloads/passwords_collection.txt")

# fin = open("/Users/zhanghao/Downloads/Wordlist_82_million.txt")

# fin = open("/Users/zhanghao/Downloads/crackstation-human-only.txt", 'rb')

# fin = open("/Users/zhanghao/Downloads/hashesorg251015.txt", 'rb')

# fin = open("/Users/zhanghao/Downloads/passwords_collection.txt", 'rb')

fin = open("/Users/zhanghao/Downloads/crackstation.txt", 'rb')



# read binary

word = fin.readline()

while word != '':

    word = word[:-1]

    if hashlib.md5(word).hexdigest() in hashlist:
        print(hashlib.md5(word).hexdigest(), word)

    word = fin.readline()




# utf -8

# word = fin.readline()
#
#
#
# while word != "":
#     print(word)
#     # count += 1
#
#     # if count % 1000000 == 0:
#     #     print(count)
#
#     if hashlib.md5(word[:-1].encode('utf-8')).hexdigest() in hashlist:
#         print(word[:-1], hashlib.md5(word.encode('utf-8')).hexdigest() )
#
#     word = fin.readline()