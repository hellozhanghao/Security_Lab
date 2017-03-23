#!/usr/bin/env python3
# ECB wrapper skeleton file for 50.020 Security
# Oka, SUTD, 2014
from present import *
import argparse
import struct

nokeybits = 80
blocksize = 64





def bytearray_to_int(ba):
    # return int.from_bytes(ba, byteorder='little')
    return struct.unpack('<Q', ba)[0]


def ecb(infile, outfile, key, mode):

    f = open(infile, "rb")
    ba = bytearray(f.read())
    print("or",len(ba))
    f.close()
    blocked_data = []
    counter = 0
    block = bytearray()
    for i in range(len(ba)):
        if (counter == 8) or (i == len(ba) - 1):

            blocked_data.append(block)
            block = bytearray()
            block.append(ba[i])
            counter = 1

        else:
            block.append(ba[i])
            counter += 1


    while len(blocked_data[-1])!= 8:
        blocked_data[-1].append(0)



    plain_integer = []
    for block in blocked_data:
        plain_integer.append(bytearray_to_int(block))
    # print(plain_integer)

    cipher_integer =[]
    for block in plain_integer:
        if mode == 'e':
            cipher_integer.append(present(block,key))
        if mode == 'd':
            cipher_integer.append(present_inv(block,key))

    f = open(outfile, "wb")
    counter = 0
    for i in range(len(cipher_integer)):

        block_ba = struct.pack('<Q',cipher_integer[i])
        if i == len(cipher_integer)-1:
            while block_ba[-1]==0:
                block_ba.pop()


        for byte in block_ba:
            f.write(bytes([byte]))
            counter += 1

    f.close()


    print("en",counter)


if __name__ == "__main__":
    # parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    # parser.add_argument('-i', dest='infile',help='input file')
    # parser.add_argument('-o', dest='outfile',help='output file')
    # parser.add_argument('-k', dest='keyfile',help='key file')
    # parser.add_argument('-m', dest='mode',help='mode')
    #
    # args=parser.parse_args()
    # infile=args.infile
    # outfile=args.outfile
    # keyfile=args.keyfile

    ecb("Tux.ppm", "Tux_encrypted.ppm", 0x4353, 'e')
    ecb("Tux_encrypted.ppm", "Tux_reversed.ppm", 0x4353, 'd')
