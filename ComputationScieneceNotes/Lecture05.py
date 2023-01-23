
#  Bisection code as programmed in Lecture 3 (by G. Lewis and attending students)
#  Input: function f, starting points a0 and b0,
#    also need max iteration k_max, tolerances eps_x, eps_f

import numpy as np
import matplotlib.pyplot as plt

def bisect(f,a0,b0,k_max,eps_x,eps_f):
    
    conv = False                        # flag for convergence, default is "not converged"
    
    if ( f(a0)*f(b0) > 0):              # check to see whether we can guarantee convergence via IVT condition
        print('Error. f(a0) f(b0) > 0: Starting condition not satisfied.')
        return None, None, conv         # abort and print message if we can't guarantee convergence
    
    a = a0
    b = b0
    iteration_history = []              # to hold a list of the interation information
    
    for k in range(k_max):              # loop over at most k_max bisection steps
        c = (a + b)/2.0                 # find the current midpoint
        f_mid = f(c)                    # compute the function value at the midpoint
        f_left=f(a)                     # compute the function value at the current left boundary
        if (f_mid*f_left > 0):          # if they have the same sign...
            a=c                         # update the left boundary, otherwise...
        else:
            b=c                         # update the right boundary
        max_err = abs(b-a)              # compute the maximal error and the residual
        res = abs(f_mid)
  
        print(f'iteration {k+1}, err={max_err:.4e} and res={res:.4e}')  # Since k starts at 0, I added 1 to k to make the first iteration 1
        
        iteration_history.append([k+1, c, max_err, res])
        
        if (max_err < eps_x) and (res < eps_f):          # if both are less than their tolerance, stop iterations
            conv = True                                  # set the convergence flag to "converged"
            break
        
    if (conv==False):                   # print warning if the iterations did not converge
        print(f'No convergence after {k_max} interations')

    it_hist = np.array(iteration_history)               # changes the list into a numpy array
                                                        # We need to do this for ploting
    
    return c, it_hist, conv               # return the approximate solution, maximal error and convergence flag


def f(x):                               # function definition of f(x), where we are solving f(x)=0
    return np.exp(x)-x**3-3/2

a0 = 0.0                                # left end-point
b0 = 1.0                                # right end-point
k_max = 100                               # maximum number of iterations
eps_x = 1.0e-4                          # tolerance on x
eps_f = 1.0                             # tolerance of function value

xstar, it_hist, conv=bisect(f,a0,b0,k_max,eps_x,eps_f)

if (conv):
    print(f'\n x* = {xstar}')
else:
    print('did not converge')

xx = it_hist[:,0]
yy = it_hist[:,1]
# yy = np.log10(it_hist[:,1])

plt.semilogy(xx,yy, 'o-')

#plt.plot(xx, yy, 'o-')
plt.show()
