from pwn import *

EXE=ELF('sw-19')
conn = remote('software-19.challs.olicyber.it', 13002 )
conn.sendline(b'1')
for i in range(20):
    response=conn.recvuntil(b':')
    #leggi l'ultima parola escludendo l'ultimo carattere e assegnala a function_name
    function_name=response.split(b' ')[-1][:-1]
    print(function_name)

    #trova l'indirizzo della funzione
    function_address=EXE.symbols[function_name]
    print(hex(function_address))
    #manda l'indirizzo della funzione
    conn.sendline(hex(function_address))

#leggi la risposta
response=conn.recvline()
print(response)