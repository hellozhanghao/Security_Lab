#!/usr/bin/env python3
# SUTD 50.020 Security Lab 1
# Simple file read in/out
# Quyen, 2014

# Name: Zhang Hao   Student ID: 1000899

# Import libraries
import string
import sys
import argparse


def doStuff(filein, fileout, key, mode):
    # open file handles to both files
    fin = open(filein,'rb')  # by default, read mode
    fout = open(fileout, 'wb')  # write mode
    c = fin.read()  # read in file into c

    key = int(key)
    print("key = ", key)
    print("mode = ", mode)

    # now put your code: convert every second character to upper case
    if key < 1 or key > 255:
        print("Key must be between 1 to 255")
        return

    b = bytearray(c)
    ans = bytearray()

    for byte in b:
        if mode=='e':
            ans.append((byte+key) % 256)
        if mode=='d':
            ans.append((byte-key) % 256)


    fout.write(ans)
    fout.close()


    # and write to fileout


# our main function
if __name__ == "__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='filein', help='input file')
    parser.add_argument('-o', dest='fileout', help='output file')
    parser.add_argument('-k', dest='key', help='how many characters the original letter should be shifted')
    parser.add_argument('-m', dest='mode', help='d: Decryption  e: Encryption')

    # parse our arguments
    # args = parser.parse_args('-i sherlock.txt -o sherlock_locked.txt -k 22 -m e'.split())

    for i in range(256):
        doStuff(filein = "flag", fileout = "flag_unlock/flag_unlocked_"+str(i), key=str(i), mode="d")


    # all done
