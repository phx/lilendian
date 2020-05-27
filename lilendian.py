#!/usr/bin/env python

import struct, sys

if sys.version_info > (3, 0):
    python3 = True
else:
    python3 = False

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
    if python3:
        print("".join("\\x{:02x}".format(c) for c in x86))
    else:
        print(''.join([ '\\x%02x'% ord(c) for c in x86 ]))
except:
    pass

# 64-bit Little Endian Shell Encoding
try:
    x64 = struct.pack('<Q', address)
    if python3:
        print("".join("\\x{:02x}".format(c) for c in x64))
    else:
        print(''.join([ '\\x%02x'% ord(c) for c in x64 ]))
except:
    pass
