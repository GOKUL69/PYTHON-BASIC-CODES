n=int(input("ENTER THE NUMBER TO BE CHECKED :  "))
sum=0
l=len(str(n))
temp=n
while temp >0:
    digit =temp % 10
    sum += digit**l
    temp =temp // 10
if sum ==n :
    print ("THE NUMBER" +str(n) +"   IS AN ARMSTRONG NUMBER :  " )
elif sum!=n :
    print("IT IS NOT AN ARMSTRONG NUMBER ")
else :
    print("INVALID INPUT")

