#!/usr/bin/python3
# -*- coding: utf-8 -*-
# DA 2017

"""
Lab2: Breaking Ciphers

Pwntool client for python3

Install: sudo pip3 install git+https://github.com/arthaud/python3-pwntools.git

Documentation: https://python3-pwntools.readthedocs.io/en/latest/
"""

from pwn import remote
import time

if __name__ == "__main__":

    # NOTE: UPPERCASE names for constants is a (nice) Python convention
    URL = 'scy-phy.net'
    PORT = 1337
    DELIMITER = '\n'
    conn = remote(URL, PORT)

    # NOTE: conn is the connection handler
    # conn.send("GET /\r\n\r\n")

    # NOTE: try to use sendline()
    # conn.sendline("GET /\r\n\r\n")

    # message = conn.recvline()
    # NOTE: try to use recvuntil() with different delimiters ...




    # NOTE: now try to use recv()





    # message = conn.recv()
    # print("received message: {}".format(message))

    # message = conn.recvuntil(DELIMITER)


    message = conn.recv()
    conn.send("2\n")

    message = conn.recv()
    message = conn.recv()
    message = str(message)
    # fout = open("secret", 'w')  # write mode
    # fout.write(message)
    # fout.close()

    print(message)
    print(type(str(message)))

    # for char in
    # print("received message: {}".format(message))





    bytes=b'\x16\x1d\x0cV\x13\x0b\x17I>!EbX\x00QEUYkR\x14\x01\x16EyB\x11],\x0b\x07\x1b'
    print(bytes)

    # conn.close()

