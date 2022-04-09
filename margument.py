def incr(l):
    for i in range(len(l)):
        l[i]=l[i]+10
    print("l inside function",l)
    print("id",id(l))

l1=[]
n=int(input("Enter n"))
for i in range(n):
    x=int(input("Enter element"))
    l1.append(x)
incr(l1)
print(l1)
print("id of l1",id(l1))
        
