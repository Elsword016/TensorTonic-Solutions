import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.asarray(x)
    num = np.exp(x) - np.exp(-x)
    deno = np.exp(x) + np.exp(-x)

    tanh_x = num/deno 
    return tanh_x