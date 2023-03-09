## **NETWORK SECURITY 03**

Per ottenere la flag di questa prima challenge è sufficiente filtrare i pacchetti in base al protocollo, in particolare filtrando solo i pacchetti che utilizzano il protocollo HTTP si troverà la flag in un header personalizzato della richiesta.

Scriviamo sulla barra dei filtri "http" in modo tale da poterci mostrare i pacchetti che hanno come protocollo http:

![Screenshot 2023-03-08 alle 21.07.58.png](https://github.com/EngJohn12/CYBERCHALLENGE2023-UNIME/blob/main/INTRO%20-%20NETWORK%20/images/Screenshot%202023-03-08%20alle%2021.07.58.png)

Andiamo poi nella sezione HTTP dove troveremo la nostra flag:



![Screenshot 2023-03-08 alle 21.12.10.png](https://github.com/EngJohn12/CYBERCHALLENGE2023-UNIME/blob/main/INTRO%20-%20NETWORK%20/images/Screenshot%202023-03-08%20alle%2021.12.10.png)

