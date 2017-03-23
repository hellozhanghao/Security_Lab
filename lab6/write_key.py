import struct

f = open("key", 'wb')
f.write(b'\x00'*80)
f.close()

print(bytes([10]))