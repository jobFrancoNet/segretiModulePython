def operazione(scelta, a,b):
    match scelta:
        case 'a':
            return int(a)+int(b)
        case 'd':
            return int(a)-int(b)
        case 'm':
            return int(a)*int(b)
        case 'd':
            if b==0:
                return "Impossibile eseguire la divisione"
            return int(a)/int(b)

print("Operazione a(addizione) d(differenza) m(oltiplicazione) d(ivisione):")
scelta=input("Scelta:")
a=input("Numero:")
b=input("Numero:")
risultato=operazione(scelta,a,b)
print(risultato)