# Index: 0  1  2  3  4
# Array:[5,10,15,20,25,34]
# arr[2]


# Defing a list(array) in Python
arr = [10,20,30,40,50]

#Access
#print(arr[2])

#Update
arr[2] =55
#print(arr[2])

#insert a value at the end
arr.append(60)

# insert at a specific pos
arr.insert(2, 25)

# delete a value
arr.pop(3)

#print(arr)

#search for a value
if 10 in arr:
    print("found 40")
else :
    print("Empty")