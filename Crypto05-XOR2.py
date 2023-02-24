ciphertext = bytes.fromhex('104e137f425954137f74107f525511457f5468134d7f146c4c')
plaintext = None

# Prova tutte le possibili chiavi non stampabili
for key in range(256):
    # Esegui l'operazione di XOR tra il testo cifrato e la chiave
    candidate = bytes([b ^ key for b in ciphertext])
    # Se il risultato decifrato contiene solo caratteri ASCII stampabili,
    # abbiamo trovato la chiave corretta
    if all(32 <= b <= 126 for b in candidate):
        plaintext = candidate.decode()
        break

if plaintext:
    print("Il messaggio decifrato è:", plaintext)
    print("La flag è:", 'flag{' + plaintext + '}')
else:
    print("Non è stato possibile decifrare il messaggio.")
# FLAG ==> flag{0n3_byt3_T0_ru1e_tH3m_4Ll}