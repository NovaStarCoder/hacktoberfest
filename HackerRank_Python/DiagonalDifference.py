"""Diagonal difference"""

r=int(input())
a=[]
k=[]
l=[]

for i in range (r):
    a.append(input().split())
for j in range(r):
    k.append(int(a[j][j]))
    l.append(int(a[j][-(j+1)]))
    
a=sum(k)
b=sum(l)
if a>b:
    print(a-b)
if b>a:
    print(b-a)
if a==b:
    print("0")