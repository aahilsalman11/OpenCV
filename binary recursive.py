def binary_search(data, key, low, high):
    low = 0
    high = len(data)+1
    if low > high:
        return -1

    mid = (low + high) // 2

    if data[mid] == key:
        return mid
    elif key < data[mid]:
        return binary_search(data, key, mid - 1)

    else:
        return binary_search(data, key, mid + 1)


data = [3, 5, 7, 12, 23, 47]
key = int(input("Enter key: "))

result = binary_search(data, key, 0, len(data) - 1)

if result == -1:
    print("Not found")
else:
    print("Found at position", result + 1)