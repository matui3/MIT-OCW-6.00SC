# 6.00 Problem Set 2
#
# Successive Approximation
#

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    # for number in poly:
    #    for digit in range(len(poly)):
    #        (x ** digit)
    total = 0
    for number in range(len(poly)):
        total = total + (x ** number) * poly[number]
    return total


def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    tuple1 = ()
    value = 0
    for i in range(1, len(poly)):
        value = i * poly[i]
        tuple1 = tuple1 + (value,)
    return tuple1
    # TO DO ...


def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    ans = evaluate_poly(poly, x_0)
    deriv = compute_deriv(poly)
    xn = x_0 - evaluate_poly(poly, x_0)/evaluate_poly(deriv, x_0)
    n = 1
    while evaluate_poly(poly, xn) != 0:
        n += 1.0
        if evaluate_poly(poly, xn) > epsilon:
            xn = xn - evaluate_poly(poly, xn)/evaluate_poly(deriv, xn)
        elif evaluate_poly(poly, xn) < -epsilon:
            xn = xn - evaluate_poly(poly, xn)/evaluate_poly(deriv, xn)
        else:
            break
    return (xn, n)
