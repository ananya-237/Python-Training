def is_anagram(s1, s2):
    l1=[0]*26
    l2=[0]*26
    for i in s1:
        l1[ord(i)-ord('a')]+=1
    for j in s2:            
        l2[ord(j)-ord('a')]+=1
    if l1==l2:
        return True
    else:
        return False

s1="anagram"
s2="nagaram"
if is_anagram(s1,s2):
    print("Anagram")
else:
    print("Not anagram")

