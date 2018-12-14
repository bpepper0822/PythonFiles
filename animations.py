import time


def dotsAnimation():  
    dots = "."
    n = 0

    while n < 10: #number of dots in animation
        print(dots * int(n))
        time.sleep(.01)
        n = n+1

    while n > 0:
        print(dots * int(n))
        time.sleep(.01)
        n = n-1