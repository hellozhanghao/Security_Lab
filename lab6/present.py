#!/usr/bin/env python3

# Present skeleton file for 50.020 Security
# Oka, SUTD, 2014

#constants
fullround=31

#S-Box Layer
sbox=[0xC,0x5,0x6,0xB,0x9,0x0,0xA,0xD,0x3,0xE,0xF,0x8,0x4,0x7,0x1,0x2]

#S-Box Layer inverse
sbox_inv=[]
for i in range(16):
    sbox_inv.append(0)
counter = 0
for i in range(16):
    sbox_inv[sbox[i]] = counter
    counter += 1


#PLayer
pmt=[0,16,32,48,1,17,33,49,2,18,34,50,3,19,35,51,\
     4,20,36,52,5,21,37,53,6,22,38,54,7,23,39,55,\
     8,24,40,56,9,25,41,57,10,26,42,58,11,27,43,59,\
     12,28,44,60,13,29,45,61,14,30,46,62,15,31,47,63]


#PLayer inverse
pmt_inv = []
for i in range(len(pmt)):
    pmt_inv.append(0)
counter = 0
for i in range(len(pmt)):
    pmt_inv[pmt[i]] = counter
    counter += 1



# Rotate left: 0b1001 --> 0b0011
rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

def genRoundKeys(key):
    roundkeys = []
    for round in range(1, fullround + 1):  # (K1 ... K32)
        roundkeys.append(key >> 16)
        # 1.Shift
        keycopy = key
        key = 0
        key += keycopy >>19
        key += (keycopy & (2 ** 19 - 1)) << 61
        # 2.Sbox
        keycopy = key
        key = 0
        key += sbox[keycopy >> 76] << 76
        key += keycopy & (2 ** 76 - 1)
        # 3. XOR
        key ^= round << 15
    return roundkeys


def addRoundKey(state,Ki):
    return state ^ Ki

def sBoxLayer(state, mode):
    ans = 0x0
    for i in range(16):
        if mode == 'e':
            ans += sbox[(state >> (i * 4)) & 0xF] << (i * 4)
        if mode == 'd':
            ans += sbox_inv[(state >> (i * 4)) & 0xF] << (i * 4)
    return ans

def pLayer(state, mode):
    ans = 0x0
    for i in range(64):
        if mode == 'e':
            ans += ((state >> i) & 0x01) << pmt[i]
        if mode == 'd':
            ans += ((state >> i) & 0x01) << pmt_inv[i]
    return ans

def present_rounds(plain, key, rounds, mode):
    roundKeys = genRoundKeys(key)
    state = plain
    if mode == 'e':
        for i in range(rounds - 1):
            state = addRoundKey(state, roundKeys[i])
            state = sBoxLayer(state,mode='e')
            state = pLayer(state,mode='e')
        return addRoundKey(state, roundKeys[rounds - 1])
    if mode == 'd':
        for i in range(rounds - 1):
            state = addRoundKey(state, roundKeys[rounds-i-1])
            state = pLayer(state,mode='d')
            state = sBoxLayer(state,mode='d')
        return addRoundKey(state, roundKeys[0])


def present(plain, key):
    return present_rounds(plain, key, fullround,'e')

def present_inv(plain, key):
    return present_rounds(plain, key, fullround,'d')



if __name__=="__main__":

    plain1 = 0x0000000000000000
    key1 = 0x00000000000000000000
    cipher1 = present(plain1,key1)
    plain11 = present_inv(cipher1,key1)
    # print(format(cipher1,'x'))
    # print(format(plain11,'x'))
    assert plain1 == plain11

    plain2 = 0x0000000000000000
    key2 = 0xFFFFFFFFFFFFFFFFFFFF
    cipher2 = present(plain2,key2)
    plain22 = present_inv(cipher2,key2)
    # print(format(cipher2,'x'))
    # print(format(plain22,'x'))
    assert plain2 == plain22

    plain3 = 0xFFFFFFFFFFFFFFFF
    key3 = 0x00000000000000000000
    cipher3 = present(plain3,key3)
    plain33 = present_inv(cipher3,key3)
    # print(format(cipher3,'x'))
    # print(format(plain33,'x'))
    assert plain3 == plain33

    plain4 = 0xFFFFFFFFFFFFFFFF
    key4 = 0xFFFFFFFFFFFFFFFFFFFF
    cipher4 = present(plain4,key4)
    plain44 = present_inv(cipher4,key4)
    # print(format(cipher4,'x'))
    # print(format(plain44,'x'))
    assert plain4 == plain44


