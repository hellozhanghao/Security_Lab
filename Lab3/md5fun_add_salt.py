import random
import string, hashlib

hashset = \
    {'0d5b558d5f6744deaaf5b016c6c77a57': 'tpoin',
     '1b31905c59f481958d2eb72158c27ac7': 'egunb',
     '1b4baba3ae3be69857b323cf6b7fcd80': 'sso55',
     '644674d142ba2174a80889f833b32563': 'owso9',
     '6e313b70d12de950443527a33d802b76': 'mlhdi',
     '78c1b8edd1bc3ffc438432479289a9e1': 'nized',
     '81466b6bb4be5a48e2230be1338bcde6': 'lou0g',
     '836626589007d7dd5304c8d22815fffc': 'di5gv',
     '96f6065d8f2dd1376eff88fba65d1d83': 'cance',
     'a74edf83748e3c4fa5f31ec10bad79db': 'dsmto',
     'a8218c67a5b4e652e30a59372e07df59': 'hed4e',
     'a92b66a9802704ca8616c4b092378272': 'opmen',
     'd4efdba5e9725e77c9b9051fa8136f0a': 'tthel',
     'ddaafa5d551a582bc924d09cc8d33ee5': 'aseas',
     'de952f5454fb0ee79bca249f80e9fe8f': 'ofror'}


pass6 = open("pass6.txt", 'w')
salted6 = open("salted6.txt",'w')  # write mode
ans1 = ''
ans2 = ''

for password in hashset.values():
    salted_password = password+random.choice(string.ascii_lowercase)
    salted_hash = hashlib.md5(salted_password.encode('ascii')).hexdigest()
    ans1 += salted_password+'\n'
    ans2 += salted_hash+'\n'

ans1=ans1[:-1]
ans2=ans2[:-1]

pass6.write(ans1)
salted6.write(ans2)
