#import pizza                       #1
#from pizza import make_pizza       #2
#from pizza import make_pizza as mp #3
#import pizza as p                  #4
#from pizza import *                 #5
import os
import random

if __name__ == '__main__':
    #pizza.make_pizza(12,'cheese','shrimp','bulgogi') #1
    #make_pizza(12,'cheese','shrimp','bulgogi')       #2
    #mp(12,'cheese','shrimp','bulgogi')               #3
    #p.make_pizza(12,'cheese','shrimp','bulgogi')     #4
    #make_pizza(12,'cheese','shrimp','bulgogi')       #5
    print(os.getcwd()) #파일 호출
    print(random.randint(1,10))