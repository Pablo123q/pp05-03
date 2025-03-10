def nwd(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a

    return a


#print(nwd(120,21))



def nwd_reku(a,b):
    if a == b:
        return a
    elif a >b:
       
        return nwd_reku(a-b,b)
    else:
        return(nwd_reku(a,b-a))


#print(nwd_reku(120,21))


# nwd_modulo_iteracyjne (reszta z dzielenia)
def nwd_modulo_iteracyjnie(a,b):
    while b!=0:
        n = b 
        b = a % b
        a = n

    return a


def nwd_modulo_rekurencyjnie(a,b):
    if b == 0:
        return a
    return nwd_modulo_rekurencyjnie(b, a % b)
    
        
  
   
#print(nwd_modulo_rekurencyjnie(120,21))
        



# nwd_modulo_reku
# i te wszystkie funkcje w petli jednej zrobic
test_values = [ (315, 504), (1230, 528), (28, 8), (12, 18), (10000, 1) ]


for i in range(len(test_values)):
    a,b =test_values[i]
    print("to a",a)
    print("to b",b)

    print("nwd iteracyjnie:",nwd(a,b))
    print("nwd rekurencyjnie:",nwd(a,b))
    print("nwd modulo iteracyjnie:",nwd(a,b))
    print("nwd modulo rekurencyjnie:",nwd(a,b))





