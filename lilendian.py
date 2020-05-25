#!/usr/bin/env python2

import struct, sys

if len(sys.argv) < 2:
  print('program must be run a memory address argument.')
  sys.exit()

if sys.argv[1] == "-":
    address = sys.stdin.readlines()[0]
else:
    address = sys.argv[1]

if not address[0:2] == '0x':
  address = '0x' + address

address = int(address,16)

# 32-bit Little Endian Shell Encoding
try:
    x86 = struct.pack('<I', address)
    x86 = repr(x86).replace("b'","").replace("'","")
    print(x86)
except:
    pass

# 64-bit Little Endian Shell Encoding
try:
    x64 = struct.pack('<Q', address)
    x64 = repr(x64).replace("b'","").replace("'","")
    print(x64)
except:
    pass
