x = input("Enter a Sentence: ")
list1 = x.split(" ")
list1=[word.strip(",.!?") for word in list1]

dict1 = {}
for i in list1:
    count=0
    for j in list1:
        if(i==j):
            count = count + 1
            dict1[f"count_of_{i}"] = count
        
print(dict1)            