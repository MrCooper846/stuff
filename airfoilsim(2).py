import requests
import json
import numpy as np
import time

import platform    # For getting the operating system name
import subprocess  # For executing a shell command

# address of the xfoil server
__HOSTADDR__ = "10.15.41.143"

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.

    See https://stackoverflow.com/questions/2953462/pinging-servers-in-python
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0


def airfoilsim(B, alpha, Re):
    """
    Obtain force coefficients around an airfoil defined by coordinates `B`, 
    at angle of attack `alpha` (in degrees) and at Reynolds number `Re`.

    The argument `B` is a 2D array with for the x and y coordinates 
    of data points defining the geometry. The first column contains the 
    x values and the second column the y values. The order of the 
    points should start from the trailing edge (included) to the leading 
    edge in clockwise fashion and then back to the trailing edge (included).
    The coordinates should be normalised by the airfoil chord.

    The function returns 
    cl       : float    - the lift coefficient
    cd       : float    - the drag coefficient
    x_lower  : np.array - x coordinates where the pressure coefficient is evaluated at on the lower surface
    x_upper  : np.array - x coordinates where the pressure coefficient is evaluated at on the upper surface
    cp_lower : np.array - the pressure coefficient at `x_lower`
    cp_upper : np.array - the pressure coefficient at `x_upper`

    You need to be connected to the University VPN for this function to 
    work. See bottom of this page 
       https://www.southampton.ac.uk/isolutions/students/away-from-campus.page
    for instructions on how to connect to the University VPN. If you are
    connected to the VPN, but you still see this message, post a message
    in the discussion group on BlackBoard.

    The airfoil simulator uses Mark Drela's XFoil, see

    https://web.mit.edu/drela/Public/web/xfoil/

    for details.
    """

    # number of times 
    maxiter = 5

    # xfoil iteration number
    niter = 200

    # clean up xfoil output folder
    cleanup = True

    # print debug message on the server
    debug   = False

    # check the student is connected to the VPN by testing 
    if ping(__HOSTADDR__) == False:
        raise ValueError("You need to be connected to the University VPN for the "\
            "function `airfoilsim` to work. See bottom of this page " \
            "https://www.southampton.ac.uk/isolutions/students/away-from-campus.page"\
            " for instructions on how to connect to the University VPN. If you are"\
            " connected to the VPN, but you still see this message, post a message"\
            " in the discussion group on BlackBoard.")

    # avoid silly mistakes
    if B.shape[0] > 360:
        raise ValueError("total number of airfoil points should be less or equal than 360")

    if np.abs(alpha) > 12:
        raise ValueError("angle of attack should be in the range [-12, 12]")

    if Re < 0:
        raise ValueError("Reynolds number must be positive")

    # extract coordinates and pass them as list arguments
    x_ = json.dumps(B[:, 0].tolist())
    y_ = json.dumps(B[:, 1].tolist())


    # stop if nudging alpha does not eventually work
    iternum = 0

    # do not change alpha at the first iteration
    nudge = False

    while True:

        # we nudge the angle of attack to avoid convergence failures
        if nudge == True:
            alpha_ = alpha +  (np.random.rand() - 0.5)/1000
        else:
            alpha_ = alpha
    
        # construct payload with arguments for the computations
        payload = { 'alpha'   : alpha_,
                    'Re'      : Re,
                    'debug'   : debug,
                    'cleanup' : cleanup,
                    'niter'   : niter,
                    'x'       : x_, 
                    'y'       : y_}
        
        if debug == True:
            print("alpha = %f" % alpha_)

        # send request for calculation
        r = requests.get("http://%s:5000/" % __HOSTADDR__, json=payload)

        # update iteration number
        iternum += 1

        # parse content and return
        data = json.loads(r.content)
        cl = data["cl"]
        cd = data["cd"]
        x  = np.array(json.loads(data["x"]))
        cp = np.array(json.loads(data["cp"]))

        # the server returns negative cd for failed calculations
        if cd != np.nan:
            break

        if iternum > maxiter:
            break
            # raise ValueError("simulation did not converge at alpha = %f" % alpha)

        # after the first iteration, if needed, we might need to nudge 
        # alpha a little bit to get the solver to convergence
        nudge = True

    # extract lower and upper surfaces by finding first point in `x`
    # which is equal to zero. The first part will be the upper side 
    # and the second part will be the lower side.
    idx = np.where(x == 0)[0][0]
    x_upper, x_lower = x[0:idx+1], x[idx:]
    cp_upper, cp_lower = cp[0:idx+1], cp[idx:]

    return cl, cd, x_lower, x_upper, cp_lower, cp_upper

if __name__ == '__main__':
    # example airfoil
    B = np.array([[ 1.000000e+00,  0.000000e+00],
                       [ 9.791199e-01, -2.670030e-03],
                       [ 9.584792e-01, -5.280240e-03],
                       [ 9.380773e-01, -7.830810e-03],
                       [ 9.179136e-01, -1.032192e-02],
                       [ 8.979875e-01, -1.275375e-02],
                       [ 8.782984e-01, -1.512648e-02],
                       [ 8.588457e-01, -1.744029e-02],
                       [ 8.396288e-01, -1.969536e-02],
                       [ 8.206471e-01, -2.189187e-02],
                       [ 8.019000e-01, -2.403000e-02],
                       [ 7.833869e-01, -2.610993e-02],
                       [ 7.651072e-01, -2.813184e-02],
                       [ 7.470603e-01, -3.009591e-02],
                       [ 7.292456e-01, -3.200232e-02],
                       [ 7.116625e-01, -3.385125e-02],
                       [ 6.943104e-01, -3.564288e-02],
                       [ 6.771887e-01, -3.737739e-02],
                       [ 6.602968e-01, -3.905496e-02],
                       [ 6.436341e-01, -4.067577e-02],
                       [ 6.272000e-01, -4.224000e-02],
                       [ 6.109939e-01, -4.374783e-02],
                       [ 5.950152e-01, -4.519944e-02],
                       [ 5.792633e-01, -4.659501e-02],
                       [ 5.637376e-01, -4.793472e-02],
                       [ 5.484375e-01, -4.921875e-02],
                       [ 5.333624e-01, -5.044728e-02],
                       [ 5.185117e-01, -5.162049e-02],
                       [ 5.038848e-01, -5.273856e-02],
                       [ 4.894811e-01, -5.380167e-02],
                       [ 4.753000e-01, -5.481000e-02],
                       [ 4.613409e-01, -5.576373e-02],
                       [ 4.476032e-01, -5.666304e-02],
                       [ 4.340863e-01, -5.750811e-02],
                       [ 4.207896e-01, -5.829912e-02],
                       [ 4.077125e-01, -5.903625e-02],
                       [ 3.948544e-01, -5.971968e-02],
                       [ 3.822147e-01, -6.034959e-02],
                       [ 3.697928e-01, -6.092616e-02],
                       [ 3.575881e-01, -6.144957e-02],
                       [ 3.456000e-01, -6.192000e-02],
                       [ 3.338279e-01, -6.233763e-02],
                       [ 3.222712e-01, -6.270264e-02],
                       [ 3.109293e-01, -6.301521e-02],
                       [ 2.998016e-01, -6.327552e-02],
                       [ 2.888875e-01, -6.348375e-02],
                       [ 2.781864e-01, -6.364008e-02],
                       [ 2.676977e-01, -6.374469e-02],
                       [ 2.574208e-01, -6.379776e-02],
                       [ 2.473551e-01, -6.379947e-02],
                       [ 2.375000e-01, -6.375000e-02],
                       [ 2.278549e-01, -6.364953e-02],
                       [ 2.184192e-01, -6.349824e-02],
                       [ 2.091923e-01, -6.329631e-02],
                       [ 2.001736e-01, -6.304392e-02],
                       [ 1.913625e-01, -6.274125e-02],
                       [ 1.827584e-01, -6.238848e-02],
                       [ 1.743607e-01, -6.198579e-02],
                       [ 1.661688e-01, -6.153336e-02],
                       [ 1.581821e-01, -6.103137e-02],
                       [ 1.504000e-01, -6.048000e-02],
                       [ 1.428219e-01, -5.987943e-02],
                       [ 1.354472e-01, -5.922984e-02],
                       [ 1.282753e-01, -5.853141e-02],
                       [ 1.213056e-01, -5.778432e-02],
                       [ 1.145375e-01, -5.698875e-02],
                       [ 1.079704e-01, -5.614488e-02],
                       [ 1.016037e-01, -5.525289e-02],
                       [ 9.543680e-02, -5.431296e-02],
                       [ 8.946910e-02, -5.332527e-02],
                       [ 8.370000e-02, -5.229000e-02],
                       [ 7.812890e-02, -5.120733e-02],
                       [ 7.275520e-02, -5.007744e-02],
                       [ 6.757830e-02, -4.890051e-02],
                       [ 6.259760e-02, -4.767672e-02],
                       [ 5.781250e-02, -4.640625e-02],
                       [ 5.322240e-02, -4.508928e-02],
                       [ 4.882670e-02, -4.372599e-02],
                       [ 4.462480e-02, -4.231656e-02],
                       [ 4.061610e-02, -4.086117e-02],
                       [ 3.680000e-02, -3.936000e-02],
                       [ 3.317590e-02, -3.781323e-02],
                       [ 2.974320e-02, -3.622104e-02],
                       [ 2.650130e-02, -3.458361e-02],
                       [ 2.344960e-02, -3.290112e-02],
                       [ 2.058750e-02, -3.117375e-02],
                       [ 1.791440e-02, -2.940168e-02],
                       [ 1.542970e-02, -2.758509e-02],
                       [ 1.313280e-02, -2.572416e-02],
                       [ 1.102310e-02, -2.381907e-02],
                       [ 9.100000e-03, -2.187000e-02],
                       [ 7.362900e-03, -1.987713e-02],
                       [ 5.811200e-03, -1.784064e-02],
                       [ 4.444300e-03, -1.576071e-02],
                       [ 3.261600e-03, -1.363752e-02],
                       [ 2.262500e-03, -1.147125e-02],
                       [ 1.446400e-03, -9.262080e-03],
                       [ 8.127000e-04, -7.010190e-03],
                       [ 3.608000e-04, -4.715760e-03],
                       [ 9.010000e-05, -2.378970e-03],
                       [ 0.000000e+00,  0.000000e+00],
                       [ 9.010000e-05,  2.378970e-03],
                       [ 3.608000e-04,  4.715760e-03],
                       [ 8.127000e-04,  7.010190e-03],
                       [ 1.446400e-03,  9.262080e-03],
                       [ 2.262500e-03,  1.147125e-02],
                       [ 3.261600e-03,  1.363752e-02],
                       [ 4.444300e-03,  1.576071e-02],
                       [ 5.811200e-03,  1.784064e-02],
                       [ 7.362900e-03,  1.987713e-02],
                       [ 9.100000e-03,  2.187000e-02],
                       [ 1.102310e-02,  2.381907e-02],
                       [ 1.313280e-02,  2.572416e-02],
                       [ 1.542970e-02,  2.758509e-02],
                       [ 1.791440e-02,  2.940168e-02],
                       [ 2.058750e-02,  3.117375e-02],
                       [ 2.344960e-02,  3.290112e-02],
                       [ 2.650130e-02,  3.458361e-02],
                       [ 2.974320e-02,  3.622104e-02],
                       [ 3.317590e-02,  3.781323e-02],
                       [ 3.680000e-02,  3.936000e-02],
                       [ 4.061610e-02,  4.086117e-02],
                       [ 4.462480e-02,  4.231656e-02],
                       [ 4.882670e-02,  4.372599e-02],
                       [ 5.322240e-02,  4.508928e-02],
                       [ 5.781250e-02,  4.640625e-02],
                       [ 6.259760e-02,  4.767672e-02],
                       [ 6.757830e-02,  4.890051e-02],
                       [ 7.275520e-02,  5.007744e-02],
                       [ 7.812890e-02,  5.120733e-02],
                       [ 8.370000e-02,  5.229000e-02],
                       [ 8.946910e-02,  5.332527e-02],
                       [ 9.543680e-02,  5.431296e-02],
                       [ 1.016037e-01,  5.525289e-02],
                       [ 1.079704e-01,  5.614488e-02],
                       [ 1.145375e-01,  5.698875e-02],
                       [ 1.213056e-01,  5.778432e-02],
                       [ 1.282753e-01,  5.853141e-02],
                       [ 1.354472e-01,  5.922984e-02],
                       [ 1.428219e-01,  5.987943e-02],
                       [ 1.504000e-01,  6.048000e-02],
                       [ 1.581821e-01,  6.103137e-02],
                       [ 1.661688e-01,  6.153336e-02],
                       [ 1.743607e-01,  6.198579e-02],
                       [ 1.827584e-01,  6.238848e-02],
                       [ 1.913625e-01,  6.274125e-02],
                       [ 2.001736e-01,  6.304392e-02],
                       [ 2.091923e-01,  6.329631e-02],
                       [ 2.184192e-01,  6.349824e-02],
                       [ 2.278549e-01,  6.364953e-02],
                       [ 2.375000e-01,  6.375000e-02],
                       [ 2.473551e-01,  6.379947e-02],
                       [ 2.574208e-01,  6.379776e-02],
                       [ 2.676977e-01,  6.374469e-02],
                       [ 2.781864e-01,  6.364008e-02],
                       [ 2.888875e-01,  6.348375e-02],
                       [ 2.998016e-01,  6.327552e-02],
                       [ 3.109293e-01,  6.301521e-02],
                       [ 3.222712e-01,  6.270264e-02],
                       [ 3.338279e-01,  6.233763e-02],
                       [ 3.456000e-01,  6.192000e-02],
                       [ 3.575881e-01,  6.144957e-02],
                       [ 3.697928e-01,  6.092616e-02],
                       [ 3.822147e-01,  6.034959e-02],
                       [ 3.948544e-01,  5.971968e-02],
                       [ 4.077125e-01,  5.903625e-02],
                       [ 4.207896e-01,  5.829912e-02],
                       [ 4.340863e-01,  5.750811e-02],
                       [ 4.476032e-01,  5.666304e-02],
                       [ 4.613409e-01,  5.576373e-02],
                       [ 4.753000e-01,  5.481000e-02],
                       [ 4.894811e-01,  5.380167e-02],
                       [ 5.038848e-01,  5.273856e-02],
                       [ 5.185117e-01,  5.162049e-02],
                       [ 5.333624e-01,  5.044728e-02],
                       [ 5.484375e-01,  4.921875e-02],
                       [ 5.637376e-01,  4.793472e-02],
                       [ 5.792633e-01,  4.659501e-02],
                       [ 5.950152e-01,  4.519944e-02],
                       [ 6.109939e-01,  4.374783e-02],
                       [ 6.272000e-01,  4.224000e-02],
                       [ 6.436341e-01,  4.067577e-02],
                       [ 6.602968e-01,  3.905496e-02],
                       [ 6.771887e-01,  3.737739e-02],
                       [ 6.943104e-01,  3.564288e-02],
                       [ 7.116625e-01,  3.385125e-02],
                       [ 7.292456e-01,  3.200232e-02],
                       [ 7.470603e-01,  3.009591e-02],
                       [ 7.651072e-01,  2.813184e-02],
                       [ 7.833869e-01,  2.610993e-02],
                       [ 8.019000e-01,  2.403000e-02],
                       [ 8.206471e-01,  2.189187e-02],
                       [ 8.396288e-01,  1.969536e-02],
                       [ 8.588457e-01,  1.744029e-02],
                       [ 8.782984e-01,  1.512648e-02],
                       [ 8.979875e-01,  1.275375e-02],
                       [ 9.179136e-01,  1.032192e-02],
                       [ 9.380773e-01,  7.830810e-03],
                       [ 9.584792e-01,  5.280240e-03],
                       [ 9.791199e-01,  2.670030e-03],
                       [ 1.000000e+00,  0.000000e+00]])
    
    # start = time.time()
    cl, cd, x_lower, x_upper, cp_lower, cp_upper = airfoilsim(B, 1.0, 2000000)
    # end = time.time()
    # print(end - start)
    print(cl, cd)








