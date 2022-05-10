a=int(input("ENTER THE NUMBER :"))
n,n1=0,1
sum=0
for i in range(0,a):
    print(sum,end=" ")
    n=n1
    n1=sum
    sum=n+n1