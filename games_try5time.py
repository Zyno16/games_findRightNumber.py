import random
n = random.randint(1,30)
try_number=5
while try_number>0:
    try_number -= 1
    b = int(input("enter the number"))
    if b > n :
        print("the number",b ,"is bigger than",n )
    elif b < n :
        print("the number",b ,"is smaller than",n )
    else:
        break

if try_number > 0:
    print("bravo you find the number") 
else:
    print("sorry you tried more than 5 timse")                 

    


   
 


    









