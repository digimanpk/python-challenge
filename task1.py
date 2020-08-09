
def find_duplicates(arr):
    container_arr =[]
    for val in arr:
        if val not in container_arr:
            container_arr.append(val)
        else:
            print("Duplicate found for value:" + str(val))


find_duplicates([1, 2, 3, 4, 5, 6, 1])
