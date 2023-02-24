#!/usr/bin/env python3

#FUNZIONE PER FARE LO XOR BIT A BIT
def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])


#La flag si ottiene facendo lo xor di due messaggi che ci vengono dati in esadecimale
m1 = '158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf' 
m2 = '73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2'

#bytes.fromhex decodifica da hex a byte
m1 = bytes.fromhex(m1)
m2 = bytes.fromhex(m2)

flag = xor(m1, m2)

print(flag)

# FLAG ==> flag{x0R_f0r_th3_w1n!}
