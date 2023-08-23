# These are functions you have defined in Lab 1. We will be using them again and
# again, hence it is convenient to put them in a .py file and import them later on.

# import necessary modules
import numpy as np

# needed for the binomial coefficient
from scipy.special import binom

def bernstein(i, n, t):
    """
    Evaluate the `i`-the Bernstein polynomial of order `n` at `t`.
    """
    return binom(n, i) * t**i * (1-t)**(n-i)


def bezier(a, N=21):
    """
    It's a good idea to document your function, so here is the documentation.
    
    Return `N` points (default is 21 points, but can be changed) on a Bezier curve 
    defined by the control points contained in the 2D array `a`. This array should 
    have two columns for the x and y coordinates of the control point and a number 
    of rows equal to the number of control points. 
    
    """
    # find order of curve from number of control points, i.e. number of 
    # rows (if n = 3, for three control points, we have a quadratic bezier curve)
    n = a.shape[0] - 1

    # initialise arrays
    B = np.zeros([N, 2])

    # create an array of N values for t from 0 to 1. t will
    # be the parameter of the curve.
    t = np.linspace(0, 1, N)

    # loop through all t values
    for j in range(len(t)):
        
        # add contribution of the i-th control point 
        for i in range(n+1):
            # YOUR CODE HERE
            # One line of code should be sufficient
            B[j, :] = B[j, :] + a[i,:]*bernstein(i, n, t[j])
            # END YOUR CODE HERE

    # now return
    return B
    
def rational_bezier(a, w, N=21):
    """
    YOUR DOCUMENTATION HERE
    Return `N` points (default is 21 points, but can be changed) on a rational 
    Bezier curve defined by the control points contained in the 2D array `a` and 
    weights in the 1D array `w`. The input array `a` should 
    have two columns for the x and y coordinates of the control point and a number 
    of rows equal to the number of control points. 
    END YOUR DOCUMENTATION HERE
    """
    # find order of curve from number of control points
    n = a.shape[0] - 1

    # initialise arrays
    B = np.zeros([N, 2])
    
    # create an array of N values for t from 0 to 1
    t = np.linspace(0, 1, N)
    
    # loop through all t values
    for j in range(len(t)):
        
        # YOUR CODE HERE
        # raise NotImplementedError()
        
        # You should be able to implement the required functionality in 4 or 5 lines of code

        # construct a list of weights times bernestein polynomials
        wb = [w[i] * bernstein(i, n, t[j]) for i in range(n+1)]

        # add the influence of all control points i=0, 1, ..., n
        for i in range(n+1):
            B[j,:] = B[j,:] + a[i,:] * wb[i]
        
        # normalise with the sum of the list above (check formula in slide 22 of lecture 1)
        B[j, :] /= sum(wb)
        
        # END YOUR CODE HERE
        
    return B