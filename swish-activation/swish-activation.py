import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.asarray(x)
    sigma_x = 1/(1+np.exp(-x))
    return x * sigma_x