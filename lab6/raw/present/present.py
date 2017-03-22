#!/usr/bin/env python3

# Present skeleton file for 50.020 Security
# Oka, SUTD, 2014

#constants
fullround=31

#S-Box Layer
sbox=[0xC,0x5,0x6,0xB,0x9,0x0,0xA,0xD,0x3,0xE,0xF,0x8,0x4,0x7,0x1,0x2]

#PLayer
pmt=[0,16,32,48,1,17,33,49,2,18,34,50,3,19,35,51,\
     4,20,36,52,5,21,37,53,6,22,38,54,7,23,39,55,\
     8,24,40,56,9,25,41,57,10,26,42,58,11,27,43,59,\
     12,28,44,60,13,29,45,61,14,30,46,62,15,31,47,63]

# Rotate left: 0b1001 --> 0b0011
rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

def genRoundKeys(key):
    pass

def addRoundKey(state,Ki):
    pass

def sBoxLayer(state):
    pass

def pLayer(state):
    pass

def present_rounds(plain, key, rounds):
    pass

def present(plain, key):
    return present_rounds(plain, key, fullround)

def present_inv(plain, key):
    pass



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


