import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    if abs(np.sum(p) - 1.0) > 1e-6:
        raise ValueError("Probabilities must sum to 1")
    else:
        ex = np.sum(np.dot(x,p))
    return ex 
    
