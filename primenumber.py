
def single():
 a=int(input("ENTER THE NUMBER :  "))
 count=0
 for i in range(1,a+1):
    
     if (a%i)==0:
        count+=1

 if(count==2):
    print("PRIME")
 else:
    print("NOT A PRIME")

def series():
 b=int(input("ENTER THE STARTING RANGE: "))
 c=int(input("ENTER THE ENDING RANGE: "))
 for number in range (b, c+1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  
                  


getinp=int(input("WHAT YOU WANNA DO: 1-SINGLE 2-SERIES:  "))
if(getinp==1):
     single()
if(getinp==2):
     series()
