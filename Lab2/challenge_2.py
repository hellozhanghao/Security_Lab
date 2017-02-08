from pwn import remote
import numpy as np

import pprint

pp = pprint.PrettyPrinter(indent=5)

if __name__ == "__main__":
    URL = 'scy-phy.net'
    PORT = 1337
    DELIMITER = '\n'
    conn = remote(URL, PORT)

    cipher = conn.recv()
    conn.send("2\n")

    # cipher = conn.recvuntil("Please send your solution of length 32 now:")
    cipher = conn.recv()
    print(cipher)
    cipher = conn.recv()
    cipher = cipher.decode('ascii')

    cipher = cipher[:-len("\nPlease send your solution of length 32 now:\n")]

    print(cipher)

    cipher = bytearray(cipher.encode('ascii'))
    # for byte in cipher:
    #     print(byte,end=' ')



    # change 1000000 to 1000899
    cipher[15] ^= ord("0") ^ ord("8")
    cipher[16] ^= ord("0") ^ ord("8")
    cipher[17] ^= ord("0") ^ ord("9")

    # change grade from 0 to 4
    cipher[24] ^= ord("0") ^ ord("4")

    # print(cipher.decode('ascii'))
    conn.send(cipher.decode('ascii'))
    message = conn.recvuntil('\n')
    print(message.decode('ascii'), end='')
    message = conn.recvuntil('\n')
    print(message.decode('ascii'), end='')
