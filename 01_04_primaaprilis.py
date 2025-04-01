
arr=[1,2,1,2,1,2,1,2,1,2,1,2]

def quickSort(arr:list):
    if len(arr) <= 1 :
        return arr
    pivot = arr[len(arr)//2]
    left=[x for x in arr if x < pivot]
    right=[x for x in arr if x > pivot]
    middle=[x for x in arr if x == pivot]
    return quickSort(left) + middle + quickSort(right)

#test
# sorted_arr = quickSort(arr)
# print("Sorted array:", sorted_arr)

def quicksort_index(arr):
    arr =[(value, index) for index, value in enumerate(arr)]
    print(arr)
    if len(arr) <= 1:
        return [x[0] for x in arr]
    pivot = arr[len(arr)//2]
    left=[x for x in arr if x < pivot]
    right=[x for x in arr if x > pivot]
    middle=[x for x in arr if x == pivot]
    return [x[0] for x in quicksort_index(left) + middle + quicksort_index(right)]



employees = [
    {"first_name": "Anna", "last_name": "Kowalska", "age": 29},
    {"first_name": "Jan", "last_name": "Nowak", "age": 34},
    {"first_name": "Marek", "last_name": "Kowalski", "age": 25},
    {"first_name": "Zofia", "last_name": "Nowak", "age": 29},
]

# last_name, age

# Sort employees by last_name, then by age
#sorted_employees = sorted(employees, key=lambda x: (x["last_name"], x["age"]))

# Print the sorted list
#print("Sorted employees:", sorted_employees)


arr=[2,3,1,2,1,1,7,8]

def counting_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr


print("Sorted array:", counting_sort(arr))

score = [88,92,75,83,90,92,60,85,90]

def student_score_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr


print("Sorted array:", student_score_sort(score))

