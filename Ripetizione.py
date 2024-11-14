num=int(input("Quante parole vuoi inserire? "))
if num!=0:
    i=0
    aggiunta1=input("Inserisci una parola: ")
    lista = [aggiunta1]
    dict={0:""}
    while (i<num-1):
        aggiunta2=input("Inserisci un'altra parola: ")
        lista.append(aggiunta2)
        i=i+1
    for i in lista:
        x=lista.count(i)
        parola=i
        dict[i]=x
    dict.pop(0)
    print(dict)
    print("FINE!")
else: print("Allora non vuoi giocare!")


    
