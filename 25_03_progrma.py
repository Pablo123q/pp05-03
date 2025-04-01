# lista = [3,2,1]
# len(lista)>=2
# pivot= 3
# mniejsze =[2,1]
# wikesze = []

# sort = mniejsze + pivot +wikesze

# sort = [2,1]+[3]+[]

# pivot =2
# lista = [2,1]
# miejsze =1
# wieksze =[]
# sort=[1] +[2] +[]

# finish = [1,2]+[] = [1,2,3]

#pseudokod
#funkcja quickSort(arr):
# jezeli ilosc elementow arr<=1
#   zwroc arr
# pivot = piewszy element z listy
# miejsze = lista elementow miejszych od pivoy
# wieksze = lista elementow wiekszych od pivot
# return = quicksort(miejsze) + pivot + quiksort(wieksze)

arr=[1,2,1,2,1,2,1,2,1,2,1,2]

def quickSort(arr:list):
    if len(arr) <= 1 :
        return arr
    mid = len(arr)//2
    pivot = arr[mid]
    miejsze = []
    wieksze = []
    for i in arr[1:]:
        if i < pivot:
            miejsze.append(i) 
            print("MMiejsza list: ",miejsze)
        else:
            wieksze.append(i) 
            print("wieksza lsta: ",wieksze)
    return quickSort(miejsze) + [pivot] + quickSort(wieksze)


#print(quickSort(arr))

import random
def quickSort_random(arr:list):
    if len(arr) <= 1 :
        return arr
    
    pivot = random.choice(arr)
    miejsze = []
    wieksze = []
    for i in arr[1:]:
        if i < pivot:
            miejsze.append(i) 
            print("MMiejsza list: ",miejsze)
        else:
            wieksze.append(i) 
            print("wieksza lsta: ",wieksze)
    return quickSort(miejsze) + [pivot] + quickSort(wieksze)


print(quickSort_random(arr))
    
#mediana 3 wartosci

nums=[5,3,1,16,2,11,7,1]



def quickSort(arr:list[int]):
    if len(arr) <= 1 :
        return arr
    mid = len(arr)//2
    first =arr[0]
    last = arr[-1]

    pivot = arr[mid]
    miejsze = []
    wieksze = []
    for i in arr[1:]:
        if i < pivot:
            miejsze.append(i) 
            print("MMiejsza list: ",miejsze)
        else:
            wieksze.append(i) 
            print("wieksza lsta: ",wieksze)
    return quickSort(miejsze) + [pivot] + quickSort(wieksze)















