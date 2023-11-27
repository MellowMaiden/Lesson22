# Lesson 22 : Libraries
# Example 1:
import math#This puts the math library into our code
#it gives us more functions

print(math.gcd(12,15))#now we can calcualte gcd , just remember to put math dot infront. math=lirary gcd=function
print(math.factorial(3))
print(math.sin(0))
print(math.asin(0))#asin is sin-1 that is sine inverse
print(math.log(2.7))#base e
print(math.exp(1))#base e^
print(math.pi)
print(math.sqrt(9))
print(math.remainder(10,3))

#Example 2 :
import random
print("you rolled a die and got :")
print(random.randint(1,6))# A random number from 1 to 6
print("you flipped a coin and got:")
flip=random.randint(1,2)
if flip==1:
    print("Heads")
else:
    print("Tails")

#Example 3:
import time
print("Hello please wait 3 seconds")
time.sleep(3)
print("Thank you")

for x in range(1,11):
    print(10-x)
    time.sleep(1)
print("Blast off")

print("Python has a clock inside of it ")
print(time.time())
print("This is the time in python")#numbers of seconds ince 1970

#Example 4:
#Make a game to help your little bro learn GCD
import random
import time
import math

hard=input("Do you want hard game? type 'yes‘ for hard")
if hard.lower()=="yes":
    L=200
    T=30
else:
    L=20
    T=60
score=0
lives=3
time_start=time.time()
time_end=time_start+T
while lives>0 and time_end > time.time():
    print("..........................................")

    #generate numbers
    x=random.randint(1,L)
    y=random.randint(1,L)
    while math.gcd(x,y)==1:
        x = random.randint(1, L)
        y = random.randint(1, L)
    #ask the question
    print(f"what is the GCD of {x} and {y}")
    z=int(input(">"))

    #calculate the anwser
    if z ==math.gcd(x,y):
        print('That is correct')
        score+=1
        print(f"score: {score}")
    else:
        print(f"wrong , the anwser is {math.gcd(x,y)}")
        lives -= 1
        print(f"you have {lives} left")


    #end of game
print(f"that is the end of game your score: {score}")



