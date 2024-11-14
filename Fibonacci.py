risposta="si"
while risposta=="si":
    num=int(input("Inserisci quantità numeri sequenza: "))
    i=0
    lista=[0,1]
    if num==0: 
        lista=["Errore"]
    elif num==1: 
        lista=lista[:-1]
    while i<(num-2):
        somma=lista[i]+lista[i+1]
        lista.append(somma)
        i=i+1
    print("La tua sequenza di fibonacci è:",lista)
    risposta=input("Vuoi inserire un altro numero? Digita si o no: ")
    risposta=risposta.lower()
print("Arrivederci! :)")






    




