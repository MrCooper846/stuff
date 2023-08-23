# These are functions you have defined in Lab 1. We will be using them again and 
# again, hence it is convenient to put them in a .py file and import them later on.

# import necessary modules and functions
import numpy as np
import matplotlib.pyplot as pl

from scipy.special import binom
from lab_1_tools import rational_bezier
        
def bezier_spline_airfoil(p, q, w_p, w_q, N=21):
    """
    YOUR DOCUMENTATION HERE
    Construct an airfoil geometry using a spline with two rational Bezier curves. The (x, y) geometry
    of the airfoil is defined by control points `p`, for the lower surface, and `q`, for the upper 
    surface, as two 2D arrays. The control points should satisfy a number of properties that are 
    specific to airfoil; a ValueError is returned otherwise. Weights for the rational curves are 
    specified by the 1D arrays `w_p` and `w_q`.
    
    The function returns a 2D array with `(x, y)` coordinates. By default, `N=21` points on each 
    surface are utilised, so that `2N-1 = 41` points are returned.
    END YOUR DOCUMENTATION HERE
    """
    # So, we first check that the spline is closed, i.e. last point of `p` and first point `q` are the same, 
    # and same for the other conditions, i.e. last point of `q` is the same as first point of `p`
    # if they do not match, raise an exception to inform the user of the problem
    if not np.all(p[-1, :] == q[0, :]):
        raise ValueError("invalid control points: spline is not closed")
        
    if not np.all(q[-1, :] == p[0, :]):
        raise ValueError("invalid control points: spline is not closed")
        
    # to make sure we are modelling an airfoil these point should have 
    # coordinates (x, y) equal (0, 0) and (1, 0). Think about the order of 
    # control points we used in the lecture and in the python demo lecture
    if (np.all(p[ 0, :] != (1, 0)) or \
        np.all(p[-1, :] != (0, 0)) or \
        np.all(q[ 0, :] != (0, 0)) or \
        np.all(q[-1, :] != (1, 0))):
        raise ValueError("invalid control points: spline does not satisfy constraints")
        
    # get degree of the bezier curves, i.e. the number of control points minus 1. 
    # For a quadratic curve (degree = 2) I should have three points
    n = p.shape[0] - 1
    m = q.shape[0] - 1 
    
    # now check the smoothneess condition at the leading edge (see lecture 2). Checking 
    # one point, e.g. q_0 should be sufficient, since we already checked continuity.
    if not np.all(q[0, :] == m/(m+n) * q[1, :] + n/(m+n) * p[n-1, :]):
        raise ValueError("invalid control points: spline does not satisfy smoothness condition at the leading edge")
    
    # ok, now lets get the points on the two surfaces of the airfoils. You should use the 
    # function `rational_bezier` you developed in lab 1. Note this is available in the module
    # `lab_1_tools` available on Blackboard.
    
    # YOUR CODE HERE
    # raise NotImplementedError()
    # get points on the lower and upper surface
    B_p = rational_bezier(p, w_p, N)
    B_q = rational_bezier(q, w_q, N)
    
    # pack points and make sure we do not repeat the point at (0, 0)
    B = np.vstack([B_p[0:-1, :], B_q])
    # END YOUR CODE HERE
    
    return B

def plot_airfoil(B, p, q):
    """
    Plot an airfoil given by geometry `B` and its control points `p` and `q`, for the lower and 
    upper surfaces, respectively. All the inputs are 2D arrays of coordinates, with `x` values
    in the first column and `y` values in the second. The function plots the airfoil, the control 
    points and the control polygon for the upper and lower surfaces.
    """
    
    # make a new figure
    pl.figure()

    # YOUR CODE HERE
    # raise NotImplementedError()
    
    # plot control points p and q with circle (red and blue would be nice)
    pl.plot(p[:, 0], p[:, 1], 'ro')
    pl.plot(q[:, 0], q[:, 1], 'bo')

    # plot control polygons by plotting points p and q as straight lines (use same colors here)
    pl.plot(p[:, 0], p[:, 1], 'r')
    pl.plot(q[:, 0], q[:, 1], 'b')

    # plot Bezier spline from the points B (in black)
    pl.plot(B[:, 0], B[:, 1], "k")

    # it's a good idea to add labels to the axes, fix the aspect ratio and add a grid.
    # YOUR CODE HERE
    pl.gca().set_aspect(1)
    pl.grid(1)
    pl.xlabel("x/c")
    pl.ylabel("y/c")
    # END YOUR CODE HERE
    
    return None

def parametric_aerofoil(w, N=21):
    """
    
    Returns the coordinates of the airfoil defined by the control points 
    
    p = np.array([[1.0, 0.0], [0.5, -0.01], [0.0, -0.06], [0.00, 0.00]])
    q = np.array([[0.0, 0.0], [0.0,  0.06], [0.3,  0.12], [1.00, 0.00]])
    
    where the geometry of the lower and upper surfaces are defined by 
    rational Bezier curves. All weights of these curves are unitary, 
    except for the weight of the control point q_2 which as the value
    of the input parameter w.
    
    The function returns the coordinates of the airfoils as a 2D array
    as well as the default control points `p` and `q`. By default, `N=21` 
    points on each surface are utilised, so that `2N-1 = 41` points are 
    returned.
    
    """
    
    # use these points by default. We will return these later on.
    p = np.array([[1.0, 0.0], [0.5, -0.01], [0.0, -0.06], [0.00, 0.00]])
    q = np.array([[0.0, 0.0], [0.0,  0.06], [0.3,  0.12], [1.00, 0.00]])

    # YOUR CODE HERE
    #raise NotImplementedError()
    
    # define weight array
    wp = np.array([1, 1, 1, 1])
    wq = np.array([1, 1, w, 1])

    # call the bezier_spline_airfoil function to get output points B
    B = bezier_spline_airfoil(p, q, wp, wq, N=N)
    # END YOUR CODE HERE
    
    # return the output B, and the default points p and q
    return B, p, q