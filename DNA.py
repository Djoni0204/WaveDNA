from math import sin
from time import sleep  

sign = '*'
width = 50
occurence = 1 #keeps count of how many times it should make a full line
i = 1 


while True:
    sleep(0.1) # how fast it should move
    i += 0.05 
    occurence += 1
    sinus = sin(i) * width
    
    if (sinus < 0): #makes sure it never gets in the negative
        sinus = sinus * -1
    
    emptySpace = sinus - 2 * 2
    
    if occurence % 2 == 0: #makes a line every 2nd pass through
        line = sign * int(sinus)
    else:
        line = sign * 2 + ' ' * int(emptySpace) + sign * 2

    x = line.center(100, ' ') #centers the DNA
    print(x)
