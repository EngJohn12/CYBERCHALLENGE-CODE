## **NETWORK SECURITY 02**

In questa challenge viene richiesto di analizzare più nel dettaglio alcuni pacchetti. In particolare la flag è nel seguente formato:

flag{Source_MAC_address/data_bytes_length}

Le informazioni necessarie per le flag sono prese dal frame numero 4, il primo contenente i dati della sessione TCP.

Per ricavare il Source_MAC_address andiamo a guardare nella sezione Ethernet II dove andiamo a ricavare l'indirizzo MAC interessato:

![Screenshot 2023-03-08 alle 19.54.27.png](./images/Screenshot%202023-03-08%20alle%2019.54.27.png)

Poi andare nella sezione Data per ricavare la lunghezza in byte dei dati:




![Screenshot 2023-03-08 alle 20.00.02.png](./images/Screenshot%202023-03-08%20alle%2020.00.02.png)

FLAG ==> flag{26:0e:ad:ef:c6:65/63}
