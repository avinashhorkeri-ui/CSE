from timeit import default_timer as t 
def binarysearch(s1,key,low,high):
    if low <=high:
        mid=(low+high)//2
        if key==s1[mid]:
            return mid
        elif key<s1[mid]:
            return binarysearch(s1,key,low,mid-1)
        else:
            return binarysearch(s1,key,mid+1,high)
    else:
        return -1 
#main
s1=[11,21,34,44,52,66,73,88]
print("given list=",s1)
key=int(input("enter key  "))
n=len(s1)
start=t()
pos=binarysearch(s1,key,0,n-1)

if pos==-1:
    print("unsuccessfull search:key not found")
else:
    print("successfull search:key found at:",pos)
end=t()
et=(end-start)*1000000
print(f"execution time={et:.2f} micoseconds")

#graph
import matplotlib.pyplot as p 
import math
p.title("binary search-graph for asymptotic notation")
p.xlabel("input size")
p.ylabel("steps")
x=list(range(1,100))
y1=[1 for y in x]
y2=[math.log(y,2)for y in x]
p.plot(x,y1,'r',label='o((1))-best case')
p.plot(x,y2,'y',label='o(log n)-average/worst case')
p.legend()
p.show()  