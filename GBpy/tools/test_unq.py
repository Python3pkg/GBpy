# Authors: Arash Dehghan Banadaki <adehgha@ncsu.edu>, Srikanth Patala <spatala@ncsu.edu>
# Copyright (c) 2014,  Arash Dehghan Banadaki and Srikanth Patala.
# License: GNU-GPL Style.

import numpy as np
import unique_rows_tol as unq_tol
xin1 = np.random.rand(8,5)
xin2 = xin1 + 1e-08
xin = np.vstack((xin1, xin2))

xout = unq_tol.unique_rows_tol(xin, return_index=True, return_inverse=True)

print xout
