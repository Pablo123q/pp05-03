def nwd(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a

    return a


print(nwd(120,21))



def nwd_reku(a,b):
    if a == b:
        return a
    elif a >b:
       
        return nwd_reku(a-b,b)
    else:
        return(nwd_reku(a,b-a))


print(nwd_reku(120,21))


# nwd_modulo_iteracyjne (reszta z dzielenia)
# nwd_modulo_reku
# i te wszystkie funkcje w petli jednej zrobic