# Linear Search using python
l1=[1,2,3,4,5,6]
i=0
t=int(input("Enter a number from the list:"))
for x in l1:
    if (x==t):
        print(i)
        break
    i+=1
else:
    print("Not found in the list")
