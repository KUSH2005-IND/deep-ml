import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    if norm_type == "l1":
        return float(np.sum(np.abs(arr)))

    elif norm_type == "l2":
        l2 = 0
        for i in arr:
            for j in np.ravel(i):
                l2 += j**2
        return float(np.sqrt(l2))

    elif norm_type == "linf":
        return float(np.max(np.abs(arr)))

    elif norm_type == "frobenius":
        if arr.ndim != 2:
            raise ValueError("Input must be a 2D matrix")

        frob = 0
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                frob += arr[i][j]**2

        return float(np.sqrt(frob))

    else:
        raise ValueError("Invalid norm type")