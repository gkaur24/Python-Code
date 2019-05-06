#import numpy as np


def secant(f, a, b, t):			# store initial values
   	fa = f(a)
    
    	fb = f(b)
   
    	while abs(fx1) < t:			# do calculation
        	a = (a * fb - b * fa) / (fb - fa)		# shift variables (prepare for next loop)
        	a,  b  = b,  c
        	fa, fb = fb, f(c)
    	return b

#print secant(0, 2, 5, 3)

#Stopping criteria: 
#1.	identify when the error   is small enough to stop,
#2.	stop if the error is no longer decreasing or decreasing too slowly, and
#3.	limit the maximum amount of time spent iterating.


#bisection calculation 
#a.	a= 0, b= 3.12; function value= 19.1
#b.	x = 0.567
#c.	a = 1, b = 2*10^2; function value= 0*10^2
#d.	x = 1.00


#newtons method 
def dx(f, x):
    		return abs(0-f(x))
 
def newtons_method(f, df, x0, e):
    	
    c = dx(f, x0)
    	
    while c > e:
        x0 = x0 - f(x0)/df(x0)
        c = dx(f, x0)
    	print ('Root is at: ', x0)

    print ('f(x) at root is: ', f(x0))


