#!/usr/bin/env python3
# ECB wrapper skeleton file for 50.020 Security
# Oka, SUTD, 2014
from present import *
import argparse
import struct

nokeybits = 80
blocksize = 64


def bytearray_to_int(ba):
    return struct.unpack('<Q', ba)[0]


def ecb(infile, outfile, key, mode):
    f = open(key, 'rb')
    ba = f.read()
    key = int.from_bytes(ba, byteorder='little')
    f.close()

    f = open(infile, "rb")
    ba = bytearray(f.read())
    f.close()
    blocked_data = []
    counter = 0
    block = bytearray()
    for i in range(len(ba)):
        if i == len(ba) - 1:
            block.append(ba[i])
            blocked_data.append(block)
            break

        if (counter == 8):
            blocked_data.append(block)
            block = bytearray()
            block.append(ba[i])
            counter = 1

        else:
            block.append(ba[i])
            counter += 1

    while len(blocked_data[-1]) != 8:
        blocked_data[-1].append(0)
        print("add", blocked_data[-1])

    plain_integer = []
    for block in blocked_data:
        plain_integer.append(bytearray_to_int(block))
    # print(plain_integer)

    cipher_integer = []
    for block in plain_integer:
        if mode == 'e':
            cipher_integer.append(present(block, key))
        if mode == 'd':
            cipher_integer.append(present_inv(block, key))

    f = open(outfile, "wb")
    counter = 0
    for i in range(len(cipher_integer)):

        block_ba = struct.pack('<Q', cipher_integer[i])
        block_ba = bytearray(block_ba)
        if i == len(cipher_integer) - 1:
            print("result",block_ba)


        if i == len(cipher_integer) - 1 and mode == 'd':
            print('before trim', block_ba)

            while block_ba[-1] == 0:
                block_ba.pop()
            print('trim', block_ba)

        for byte in block_ba:
            f.write(bytes([byte]))
            counter += 1

    f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile', help='input file')
    parser.add_argument('-o', dest='outfile', help='output file')
    parser.add_argument('-k', dest='keyfile', help='key file')
    parser.add_argument('-m', dest='mode', help='mode')

    args = parser.parse_args()
    infile = args.infile
    outfile = args.outfile
    keyfile = args.keyfile

    print("En")
    ecb("Tux.ppm", "Tux_encrypted.ppm", 'key', 'e')
    print("De")
    ecb("Tux_encrypted.ppm", "Tux_reversed.ppm", 'key', 'd')

    # python3 -i Tux.ppm -o Tux_encrypted.ppm -k key -m e
    # python3 -i Tux_encrypted.ppm -o Tux_reversed.ppm -k key -m d
