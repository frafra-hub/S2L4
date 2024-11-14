risposta=input("Ciao, vuoi calcolare il perimetro di una figura geometrica? Digita si o no: ").lower()
if risposta=="si":
    figura=input("Seleziona la figura dla menù:\nDigita 1 per il quadrato\nDigita 2 per il cerchio\nDigita 3 per il rettangolo\n")
    if figura=="1":
        lato=int(input("Inserisci lato quadrato: "))
        perimetro=lato*4
        print("il perimetro del quadrato è: ",perimetro)
    elif figura=="2":
        raggio=int(input("Inserisci il raggio del cerchio: "))
        perimetro=raggio*3,14*2
        print("il perimetro del cerchio è: ",perimetro)
    elif figura=="3":
        base=int(input("Inserici la base del rettangolo: "))
        altezza=int(input("Inserisci l'altezza del rettangolo: "))
        perimetro=base*2+altezza*2
        print("il perimetro del rettangolo è: ",perimetro)
    else:
        print("Mi dispiace ma il numero inserito non è valido")
else: print("Arrivederci!")

