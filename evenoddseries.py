r=int(input("ENTER THE FIRST RANGE :  "))
r1=int(input("ENTER THE SECOND RANGE :  "))
ore=int(input("WHAT SERIES DO YOU WANT TO PRINT : 1-EVEN :2-ODD  "))

if ore==1:
 for i in range (r,r1+1):
    a=i%2
    if a==0:
     print("THE EVEN NUMBERS ARE : " +str(i))
elif ore==2:
 for i in range (r,r1+1):
    a=i%2
    if a!=0:
        print("THE ODD NUMBERS  ARE : " +str(i))

