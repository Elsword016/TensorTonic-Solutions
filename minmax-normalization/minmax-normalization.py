import numpy as np

def minmax_scale(x, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    x = np.asarray(x)
    max_x = np.max(x,axis=axis,keepdims=True)
    min_x = np.min(x,axis=axis,keepdims=True)
    deno = max_x - min_x 
    deno_abs = np.maximum(deno,eps)

    x_scale = (x-min_x)/deno_abs
    return x_scale 