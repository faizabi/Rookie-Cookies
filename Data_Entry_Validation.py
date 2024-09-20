pos_nos=[]
a=0
while a>=0:
    a=int(input("Enter a positive number: "))
    if a>=0:
        pos_nos.append(a)
    else:
        break

print(pos_nos)     
#if a<0:
#   print("You entered a negative number. Exiting the loop")