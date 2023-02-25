from pwn import *
from string import printable
p = remote("padding.challs.cyberchallenge.it", 9030)
def split(msg, BLOCK=32):
  return [msg[i:i+BLOCK] for i in range(0, len(msg), BLOCK)]
def encrypt(msg):
  p.sendline(msg)
  p.recvuntil("password: ")
  return split(p.recvline().strip())
flag = ""
while "}" not in flag:
  for c in printable[:-6]:
    msg = "A" * (31-len(flag)) + flag + c + "A" * (31-len(flag))
    blocks = encrypt(msg)
    if blocks[1] == blocks[3]:
      flag = flag + c
      print(flag)
      break

# FLAG ==> CCIT{r3m3mb3r_th3_3cb_p3ngu1n?}

"""

Il codice è in Python e utilizza la libreria "pwntools" per connettersi a un server remoto e inviare dati. L'obiettivo del codice è quello di effettuare un attacco di padding oracle su un server remoto.

La funzione "split" prende una stringa "msg" e la divide in blocchi di dimensione "BLOCK" (di default 32 byte).

La funzione "encrypt" invia una stringa al server remoto, riceve la risposta e divide la risposta in blocchi di dimensione "BLOCK". La funzione restituisce quindi una lista di blocchi.

Il codice principale utilizza un ciclo while per cercare il flag del server. All'interno del ciclo, viene iterato attraverso tutti i caratteri "printable" ad eccezione degli ultimi 6 (i quali potrebbero causare problemi di decodifica). Viene costruita una stringa "msg" composta da caratteri "A" di riempimento, il flag corrente, il carattere da testare e altri caratteri "A" di riempimento.

La stringa "msg" viene quindi inviata al server utilizzando la funzione "encrypt". Se il secondo e il quarto blocco restituiti dal server sono uguali, allora il carattere testato viene aggiunto al flag corrente e il ciclo ricomincia.

La variabile "flag" contiene il flag del server, che viene stampato ogni volta che un carattere viene aggiunto al flag."""
    