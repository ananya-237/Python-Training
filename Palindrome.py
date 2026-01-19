#Program to check palindrome using two pointers
l1= [1,2,3,4,5,1]
front=0
end=len(l1)-1
while front<=end:
    if (l1[front]!=l1[end]):
        print("Not a palindrome list")
        break
    front+=1
    end-=1
else:
    print("Palindrome list")
