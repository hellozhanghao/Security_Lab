bytes=b'\x16\x1d\x0cV\x13\x0b\x17I>!EbX\x00QEUYkR\x14\x01\x16EyB\x11],\x0b\x07\x1b'
plain_text = b'Student ID: 1000000 and grade 0.'
target     = b'Student ID: 1000899 and grade 4.'




print(plain_text )
# plain=b'Student ID: 1000000 and grade 0.'
modify =b'00000000000000008990000000000040'
print(plain_text+modify)


plain_arrary = bytearray(plain_text)
print(plain_arrary[1])
print()
