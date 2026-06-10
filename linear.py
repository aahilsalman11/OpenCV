data = [5,7,6,13,57,34]
key = int(input("Enter the key to search: "))
key_found = False

for i in range(len(data)):
    if data[i] == key:
        print("Key found at",i + 17)
        key_found = True
        break

if key_found == False:
    print("Key not found")

    

