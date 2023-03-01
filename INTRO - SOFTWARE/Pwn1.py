#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *
import re

def main():
    HOST = "software-17.challs.olicyber.it"
    PORT = 13000
    r = remote(HOST, PORT)

    i = 0
    
    # Initialize a flag to indicate whether we're processing the first list
    first_list = True
    
    # Send "y" to indicate that you want to sum numbers
    r.sendline(b"y")
        
    while i < 10:

        # Receive the list of numbers and split it into individual numbers
        num_list = r.recvrepeat(0.9).strip()
        print(num_list)


        integers = [int(match) for match in re.findall(r"[+-]?\b\d+\b", num_list.decode())]

        # Exclude the first three integers from the first list
        if first_list:
            integers = integers[3:]
        # Exclude only the first integer from the second and subsequent lists
        else:
            integers = integers[0:]

        # Start the sum
        total = 0
        for _ in integers:
            int(_)
            total += _
        print(total)
        
        

        # Send the sum back to the server
        r.sendline(str(total).encode())

        # Receive the response from the server
        response = r.recvline().decode()
        print(response)

        first_list = False
        
        i+=1
        

    r.close()


if __name__ == "__main__":
    main()
