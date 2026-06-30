n = int(input("Enter the number of values in the data: "))
data =[]
for i in range(n):
    item = int(input("Enter items one by one: "))
    data.append(item)
print(data)

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        sorted = False
        for j in range(n-i-1):
             if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
                sorted = True
        print(data)
        if sorted == False:
            break
bubble_sort(data)      

