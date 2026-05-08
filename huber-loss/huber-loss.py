import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    e = y_true - y_pred
    e_abs = np.abs(y_true-y_pred) # np.where(condition, value_if_true, value_if_false)

    loss = np.where(e_abs<=delta, e**2/2, delta*(e_abs - delta/2))
    return np.mean(loss)