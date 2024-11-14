stringa=input("Inserisci una serie di numeri separati da uno spazio (es. 1 2 3 4...)\n")
lista=stringa.split(" ")
somma=xmax=max=0
min=100000
for i in lista:
    somma=int(i)+somma
    x=lista.count(i)
    if x>xmax: 
        moda=i
        xmax=x
    if int(i)<min: min=int(i)
    if int(i)>max: max=int(i)
if xmax==1: moda = "non cè, tutti i numeri sono presenti nella stessa quantità"
media=somma/len(lista)
mediana=int((min+max)/2)
print("La mediana è:",mediana,"\nLa media",media,"\nLa moda",moda)
