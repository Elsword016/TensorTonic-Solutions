import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X) 
    N = X.shape[0]
    mean_x = np.mean(X,axis=0,keepdims=True)
    x_center = X - mean_x 

    term = x_center.T @ x_center
    cov_matrix =term/(N-1)

    
    if X.ndim != 2:
        return None
    if N < 2:
        return None 
    return cov_matrix