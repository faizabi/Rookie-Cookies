arr=[]
a=int(input("Enter the number of elements in the array:"))
for i in range(a):
    x=int(input(f"Enter an array of numbers {i+1}:"))
    arr.append(x)
print(arr[::-1])




