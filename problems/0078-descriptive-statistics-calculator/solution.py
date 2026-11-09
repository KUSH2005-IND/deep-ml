import numpy as np
import math as m
def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    mean_data=np.mean(data)

    median_data=np.median(data)
    
    values, counts = np.unique(data, return_counts=True)
    mode_data = values[np.argmax(counts)]
    
    diff_sum=0
    n=len(data)
    for i in data:
        sq_diff= (i-mean_data)**2
        diff_sum+=sq_diff
    var_data=diff_sum/n

    std_dev= m.sqrt(var_data)

    p25=np.percentile(data,25)
    p50=np.percentile(data,50)
    p75=np.percentile(data,75)

    iqr= p75-p25

    return {
        "mean": mean_data,
        "median": median_data,
        "mode": mode_data,
        "variance": var_data,
        "standard_deviation": std_dev,
        "25th_percentile": p25,
        "50th_percentile": p50,
        "75th_percentile": p75,
        "interquartile_range": iqr
    }