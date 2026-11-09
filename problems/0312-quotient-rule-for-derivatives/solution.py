import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    
    g=np.poly1d(g_coeffs) #poly1d() converts list into polynomial object
    h=np.poly1d(h_coeffs)

    g_der=np.polyder(g) #polyder() differentiates a polynomial
    h_der=np.polyder(h)

    derivative= ((g_der(x)*h(x))-(h_der(x)*g(x)))/(h(x)**2)

    return derivative
    