import base64

s = 'ZmxhZ3t3NDF0XzF0c19hbGxfYjE='
decoded_s = base64.b64decode(s)
print(decoded_s)

n = 664813035583918006462745898431981286737635929725
byte_len = (n.bit_length() + 7) // 8  # determina il numero di byte necessari
byte_representation = n.to_bytes(byte_len, byteorder='big')
print(byte_representation)

flag = decoded_s + byte_representation
print(flag.decode())  # decodifica la flag completa in formato testuale

# FLAG ==> flag{w41t_1ts_all_b1ts?_4lw4ys_H4s_b33n}