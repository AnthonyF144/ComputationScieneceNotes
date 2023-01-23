# This is the code from lecture 3 but only the inputs are changed


import numpy as np

def bisect(f, a0, b0, k_max, eps_x, eps_f):     # This will be the same for all bisections functions
                                                # You will change what you feed the function though
     
    conv = False                     # flag for convergence
    a = a0
    b = b0
    max_error = 1
    c = 1.0
    
    if (f(a0)*f(b0) < 0):
        return None, None, conv      
                
    for k in range(k_max):
        c = (a+b)/2.0   # cut the interval in half
                        # finds the current midpoint
                        # you make it 2.0 so it doesn't interpert it as int if a and b are int
        
        f_mid = f(c)    # making middle value
                        # evaluate the function at the midpoint
        
                        # Now we want to deterime if it's the left or right we keep
        f_left = f(a)   # this isn't needed you can just do f(a)
                        # evaluate the function f at the left endpoint
    
        if (f_mid * f_left > 0):    # if they are the same sign
            a = c                   # update the left endpoint
        else:
            b = c                   # update the right endpoint otherwise
        
        max_error = abs(b-a)        # max error is the difference between a and b
        res = abs(f_mid)            # residual
            
        print(f'Interation {k+1} and Max error {max_error:.4e}, residual {res:.8f}')        
        
        if (max_error < eps_x) and (res < eps_f):     # a break function if we reach the max error while in a loop
            conv = True                # When it converges we send back true
            break
        
    return c,max_error,conv


def f(x):               # Where we are solving f(x) = 0
    return x**2 - 5     # ONE OF THE FEW THINGS YOU MIGHT HAVE TO CHANGE

# declaring variables
a0 = 2.0
b0 = 3.0
k_max = 100
eps_x = 1.0e-6
eps_f = 1.0

xstar, max_err, conv = bisect(f, a0, b0, k_max, eps_x, eps_f)

if (conv == True):
    print (f'x ={xstar} with maximum error = {max_err}')
else:
    print('Did not Converge')

        
        
        
           
        


