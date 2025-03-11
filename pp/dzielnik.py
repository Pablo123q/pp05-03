import timeit
import math
#znjadowanie dzielnikow i sprawdzanie poerwszosci liczby 
#znjadoanie dzielnikow 

#cel: znajdowanie dzielnikow, krire dziela sie przez n bez reszty

#pseldokod

# funkcja znajdz)dzielnik(n:int)
# dla kazdego i od 1 do n+1
#   jezeku n% i == 0
#       return i


def znajdz_dzielnik(n:int)->int:
    lista = []
    for i in range(1,n+1):
        if n % i == 0:
            lista.append(i)
    return lista



def znajdz_dzielnik2(n:int)->int:
    dzielnik =[]
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            dzielnik.append(i)
            dzielnik.append(n/i)

        return dzielnik


# znajdz najwieszky dzielnik

def znajdz_naj_dzielnik(n:int)->int:
    dzielnik= []
    for i in range(1,n+1):
        if n % i == 0:
            dzielnik.append(i)
    return dzielnik[-2]
    

def znajdz_naj_dzielnik2(n:int)->int:
    
    for i in range(n//2, 0,-1):
        if n % i == 0:
            return i
    


#liczby pierwsze 
#pseudokod
#funkcja liczby_pierwsze(n):
# if n<2 to 
#   retrn false
# dla kazdego i od 2 do n 
#   jezeli n modulo i == 0
#        return false
#   else rerutn true


def liczby_pierwsze(n:int):
    if n<2:
        return False
    
    for i in range(2,n):
        if n % i == 0:
            return False
        else:
            return True

# znalezienie luczb pierwszych od 0 do n w formie listy

n=10 ** 8
print(znajdz_naj_dzielnik2(n))
print(liczby_pierwsze(n))


print("najdowanie dizelnikow", timeit.timeit(lambda: znajdz_dzielnik(n), number=1),"sek")
print("najdowanie dizelnikow", timeit.timeit(lambda: znajdz_dzielnik2(n), number=1),"sek")
