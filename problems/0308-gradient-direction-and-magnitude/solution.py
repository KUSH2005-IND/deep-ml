import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    """
    Calculate the magnitude and direction of a gradient vector.

    Args:
        gradient: A list representing the gradient vector

    Returns:
        Dictionary containing:
        - magnitude: The L2 norm of the gradient
        - direction: Unit vector in direction of steepest ascent
        - descent_direction: Unit vector in direction of steepest descent
    """
    gradient = np.array(gradient, dtype=float)

    mag = np.sqrt(np.sum(gradient ** 2))

    if mag == 0:
        direction = np.zeros_like(gradient)
    else:
        direction = gradient / mag

    descent = -direction

    return {
        "magnitude": float(mag),
        "direction": direction.tolist(),
        "descent_direction": descent.tolist()
    }