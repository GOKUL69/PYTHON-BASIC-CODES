a=int(input("ENTER THE FIRST NUMBER  "))
b=int(input("ENTER THE SECOND NUMBER  "))
c=int(input("WHAT YOU WANNA DO 1-ADDITION 2-SUBTRACTION 3-DIVISION 4-MULTIPLICATION  :  "))
if(c==1):
    ans =a+b
    print("THE ADDITION IS   "+str(ans))
    quit()
if(c==2):
    sub=a-b
    print("THE SUBTRACTION IS   "+str(sub))
    quit()
if(c==3):
    div=a/b
    print("THE DIVISION IS   "+str(div))
    quit()
if(c==4):
    mul=a*b
    print("THE MULTIPLY IS  "+str(mul))
    quit()
else:
    print("ERROR GIVE A VALID COMMAND")

   
     
