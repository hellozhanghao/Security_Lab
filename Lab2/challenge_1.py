from pwn import remote

import  pprint

pp = pprint.PrettyPrinter(indent=5)

if __name__ == "__main__":

    URL = 'scy-phy.net'
    PORT = 1337
    DELIMITER = '\n'
    conn = remote(URL, PORT)

    cipher = conn.recv()
    conn.send("1\n")

    cipher = conn.recvuntil("Please send your solution of length 7408 now:\n")

    cipher = cipher.decode('ascii')
    cipher = cipher[len('Welcome to challenge "Substitution" of length 7408: '):-len(
        "\nPlease send your solution of length 7408 now:\n")]

    cipher_freq = dict()
    cipher_fixed = []
    for char in cipher:
        if char in cipher_freq:
            cipher_freq[char] += 1
        else:
            cipher_freq[char] = 1

        if char not in cipher_fixed:
            cipher_fixed.append(char)

    cipher_order = sorted(cipher_freq, key=lambda x: cipher_freq[x], reverse=True)


    fin = open('sherlock.txt', 'rb')  # by default, read mode
    sherlock = fin.read()  # read in file into c
    sherlock = sherlock.decode('ascii')
    sherlock = sherlock.lower()

    sherlock_freq = dict()
    for char in sherlock:
        if char in sherlock_freq:
            sherlock_freq[char] += 1
        else:
            sherlock_freq[char] = 1

    sherlock_order = sorted(sherlock_freq, key=lambda x: sherlock_freq[x], reverse=True)

    map = dict()
    map['0'] = ''
    map['1'] = ''
    map['2'] = ''
    map['3'] = ''
    map['4'] = ''
    map['5'] = ''
    map['6'] = ''
    map['7'] = ''
    map['8'] = ''
    map['9'] = ''
    map['a'] = cipher_fixed[10]
    map['b'] = cipher_fixed[22]
    map['c'] = cipher_fixed[9]
    map['d'] = cipher_fixed[7]
    map['e'] = cipher_fixed[4]
    map['f'] = cipher_fixed[26]
    map['g'] = cipher_fixed[20]
    map['h'] = cipher_fixed[17]
    map['i'] = cipher_fixed[2]
    map['j'] = cipher_fixed[30]
    map['k'] = cipher_fixed[24]
    map['l'] = cipher_fixed[1]
    map['m'] = cipher_fixed[16]
    map['n'] = cipher_fixed[14]
    map['o'] = cipher_fixed[13]
    map['p'] = cipher_fixed[11]
    map['q'] = cipher_fixed[28]
    map['r'] = cipher_fixed[6]
    map['s'] = cipher_fixed[19]
    map['t'] = cipher_fixed[3]
    map['u'] = cipher_fixed[15]
    map['v'] = cipher_fixed[21]
    map['w'] = cipher_fixed[18]
    map['x'] = ''
    map['y'] = cipher_fixed[23]
    map['z'] = ''
    map['A'] = ''
    map['B'] = ''
    map['C'] = ''
    map['D'] = ''
    map['E'] = ''
    map['F'] = ''
    map['G'] = ''
    map['H'] = ''
    map['I'] = ''
    map['J'] = ''
    map['K'] = ''
    map['L'] = ''
    map['M'] = ''
    map['N'] = ''
    map['O'] = ''
    map['P'] = ''
    map['Q'] = ''
    map['R'] = ''
    map['S'] = ''
    map['T'] = ''
    map['U'] = ''
    map['V'] = ''
    map['W'] = ''
    map['X'] = ''
    map['Y'] = ''
    map['Z'] = ''
    map['!'] = ''
    map['"'] = cipher_fixed[31]
    map['#'] = ''
    map['$'] = ''
    map['%'] = ''
    map['&'] = ''
    map["'"] = cipher_fixed[29]
    map['('] = ''
    map[')'] = ''
    map['*'] = ''
    map['+'] = ''
    map[','] = cipher_fixed[25]
    map['-'] = cipher_fixed[8]
    map['.'] = cipher_fixed[27]
    map['/'] = ''
    map[':'] = ''
    map[';'] = ''
    map['<'] = ''
    map['='] = ''
    map['>'] = ''
    map['?'] = cipher_fixed[32]
    map['@'] = ''
    map['['] = ''
    map['\\'] = ''
    map[']'] = ''
    map['^'] = ''
    map['_'] = ''
    map['`'] = ''
    map['{'] = ''
    map['|'] = ''
    map['}'] = ''
    map['~'] = ''
    map[' '] = cipher_fixed[5]  # cipher_order[0]
    map['\t'] = cipher_order[32]
    map['\n'] = cipher_order[13]
    map['\r'] = ''
    map['\x0b'] = ''
    map['\x0c'] = ''





    ans = ''
    wrong = 0
    for char in cipher:
        written = False
        for key in map:
            if map[key] == char:
                ans += key
                written = True
                break
        if written == False:
            wrong += 1
            ans += '***********'+char
    print(ans)

    # # for params tuning

    # for char1 in range(len(cipher_fixed)):
    #     for char2 in range(len(cipher_order)):
    #         if cipher_fixed[char1] == cipher_order[char2]:
    #             print("Mapping ",char2, char1)

    #
    #
    # for char in range(len(cipher_order)):
    #     print(char, sherlock_order[char], cipher_order[char])

    # for i in range(len(cipher_fixed)):
    #     print(i, cipher_fixed[i])

    conn.send(ans)
    print(conn.recv().decode('ascii'))

    #
    # pp.pprint(cipher_freq)
    # pp.pprint(cipher_order)

    conn.close()



