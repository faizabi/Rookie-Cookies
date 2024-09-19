d=input("Enter a number: ")
#l=[int(i) for i in d]
sum=0
ll=len(d)
for i in d:
    sum+=int(i)**ll
if sum==d:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")