s=input()
k=int(input())
val=k

slen=len(s)
arr=s.split(" ")

l=len(arr)
temp=[]
inital=0
new_str=""

for i in range(slen//k+1):
    substring=""
    substring=s[inital:k]
    #print(substring)
    ar1=substring.split(" ")
    new_str=""
    for i in range(len(ar1)):
        if (arr.count(ar1[i])>= 1):
            new_str=new_str+ " " +ar1[i]
    temp.append(new_str.strip())
    inital=k
    k=k+val
print(temp)
