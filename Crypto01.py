array = [102, 108, 97, 103, 123, 117, 103, 104, 95, 78, 117, 109, 66, 51, 114, 53, 95, 52, 49, 114, 51, 52, 100, 121, 125]  # esempio di array di numeri
stringa = ""  # inizializzo la stringa vuota

for numero in array:
    carattere = chr(numero)  # converto il numero in un carattere ASCII
    stringa += carattere  # aggiungo il carattere alla stringa

print(stringa)  # stampo la stringa risultante

# FLAG ==> flag{ugh_NumB3r5_41r34dy}