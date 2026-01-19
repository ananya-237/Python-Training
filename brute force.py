def twoSum(num,t):
    x=0
    while(x<len(num)):
        z=x+1
        while(x<len(num)):
            if t==(num[x]+num[z]):
                return [x+z]
            z+=1
        x+=1
num=[18,19,8,7,6,7]
t=15
s= twoSum(num,t)
print(s)

    
