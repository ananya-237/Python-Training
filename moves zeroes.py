n=[0,1,0,3,12]
j=0
for i in range(0,len(n)):
    if(n[i]!=0):
        n[i],n[j]=n[j],n[i]
        j+=1
print(n)