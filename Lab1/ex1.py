#!/usr/bin/env python3
# SUTD 50.020 Security Lab 1
# Simple file read in/out
# Quyen, 2014

# Name: Zhang Hao   Student ID: 1000899

# Import libraries
import string
import sys
import argparse

def doStuff(filein,fileout,key, mode):
    # open file handles to both files
    fin  = open(filein, newline='\n')       # by default, read mode
    fout = open(fileout,'w')  # write mode
    c    = fin.read()         # read in file into c

    key = int(key)
    print("key = ",key)
    print("mode = ",mode)

    # now put your code: convert every second character to upper case

    ans=""
    for char in c:
        if mode=='d':
            char = string.printable[(string.printable.index(char)+key)%100]
        if mode=='e':
            char = string.printable[(string.printable.index(char)-key)%100]
        ans+=char


    fout.write(ans)
    fout.close()



    # print(c.split('\n'))

    # and write to fileout


# our main function
if __name__=="__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='filein',help='input file')
    parser.add_argument('-o', dest='fileout', help='output file')
    parser.add_argument('-k',dest='key', help='how many characters the original letter should be shifted')
    parser.add_argument('-m', dest='mode', help='d: Decryption  e: Encryption')

    # parse our arguments
    # args = parser.parse_args('-i sherlock.txt -o sherlock_locked.txt -k 1 -m e'.split())

    args = parser.parse_args('-i sherlock_locked.txt -o sherlock_unlocked.txt -k 1 -m d'.split())

    filein=args.filein
    fileout=args.fileout
    key = args.key
    mode = args.mode

    # check type
    try:
        int(key)
        if int(key) < 1 or int(key) > 255:
            print("Key must be between 1 to 255")
            exit()
        if type(filein) is not str:
            print("Filein not string")
            exit()
        if type(fileout) is not str:
            print("Fileout not string")
            exit()
        if mode != 'd' and mode != 'e':
            print("Mode can only be e or d")
            exit()
    except:
        print("Key not integer value")
        exit()

    doStuff(filein,fileout,key,mode)

    # all done


