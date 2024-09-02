##guess the number

import random
total=2
sub=1
while True:
    num=int(input("Guess a number from 1 to 10 If you can :"))

   
    ran=random.randint(1,10)
    print( ((f'The random number : {ran}')))
    print((f"you guess number : {num}"))
   
    if ran==num:
        print(f"your guess is correct :Random{ran}=guessed :{num}")
    elif ran!=num and total!=0:
        total=total-sub
        print("you got wrong num so got - 1 : " , total)
    elif total==0:
        print("you are out of game BYE (-_-)")
        quit()   
    else:
        print('no')  
    
    print("total score = ",total)      

