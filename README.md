![lil endian](https://raw.githubusercontent.com/phx/lilendian/master/lilendian.png)

# lil endian

This program is comptaible with both Python 2 and 3.

It simply returns escaped shell code in Little Endian format for whatever memory address is submitted as the first argument.

It's smart enough to distinguish between addresses with an `0x` prefix and accounts for that.

If the address is only in the 64-bit range, you will only receive the 64-bit output.

If the address can fit in the x86_64 ranges, you will receive both 32 and 64-bit output.

## Install for python3 via PyPI:

`pip3 install lilendian`

## Install for python2 via setup.py:

`python setup.py install`

## Run in place:

`./lilendian [single memory address]`

### Examples

```
$ ./lilendian deadbeef
\xef\xbe\xad\xde
\xef\xbe\xad\xde\x00\x00\x00\x00

$ ./lilendian 0xdeadbeef
\xef\xbe\xad\xde
\xef\xbe\xad\xde\x00\x00\x00\x00

$ ./lilendian 0x00007fffffffd980
\x80\xd9\xff\xff\xff\x7f\x00\x00
```

### Shell script example snippet:

Let's say you wanted to get a piece of 64-bit shellcode for `0xdeadbeef + 0xbadcafe + 0xcafebabe + 0xabadbabe`.

```sh
for addr in {0xdeadbeef,0xbadcafe,0xcafebabe,0xabadbabe}; do
  lilendian $addr | tail -1
done | tr -d "\n"; echo

Output:
\xef\xbe\xad\xde\x00\x00\x00\x00\xfe\xca\xad\x0b\x00\x00\x00\x00\xbe\xba\xfe\xca\x00\x00\x00\x00\xbe\xba\xad\xab\x00\x00\x00\x00  
```

Copy and paste that guy straight into your payload.

### Calling from within `gdb`:

```
(gdb) ! lilendian 0xdeadbeef
\xef\xbe\xad\xde
\xef\xbe\xad\xde\x00\x00\x00\x00
```

### Future:

I might tweak it in the future to take multiple memory addresses, but as of right now, it only outputs a single memory address.

I have kept it short and simple to be easily scriptable, so I'll leave the rest up to you.
