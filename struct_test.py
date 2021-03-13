import struct

var= struct.pack('iii', b'x01',2,3)

upvar= struct.unpack('iii',var)
print(upvar)
print(type(upvar))

size=struct.calcsize('iii')
print(size)