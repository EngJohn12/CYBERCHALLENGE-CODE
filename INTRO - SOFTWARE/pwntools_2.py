from pwn import *

conn = remote("software-18.challs.olicyber.it", 13001)

conn.sendline(b'1')
response = conn.recvline_contains(b'Step')
print(response)

for i in range(101):
    bit = int(response.split(b' ')[-1][:2])

    hex_num = response.split(b' ')[-4]
    #print the type of variable hex
    #print(type(hex_num))

    if bit == 32:
        num = int(hex_num, 16)
        num = p32(num, endian='little')
    elif bit == 64:
        num = int(hex_num, 16)
        num = p64(num, endian='little')

    print(num)
    conn.send(num)

    response = conn.recvline_contains(b'[')
    print(response)