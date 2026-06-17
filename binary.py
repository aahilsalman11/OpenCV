def binary_search(data,key):
    low = 0
    high = len(data)-1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] > key:
            high = mid - 1
        elif data[mid] < key:
            low = mid + 1
        else:
            return mid
    return -1

data = [3,5,7,12,23,47]
key = int(input("Enter a key:"))
result = binary_search(data,key)
if result == -1:
    print("Key not found!")
else:
    print("Key found at ",str(result + 1))




