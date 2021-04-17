
def euclid_algorithm(m, n):
    """
    Implementation of Euclid algorithm using while loop.
    Greatest common divisor d of numbers m and n is returned (d = gcd(m, n))
    For a function that returns the integer coefficients x, y satisfying the relationship: m*x + n*y = d
    have a look at the function extended_euclid_algorithm below.
    Importantly, 'strong typing'-like parameters verification is added.
    :param m: non-negative integer
    :param n: non-negative integer
    :return: greatest common divisor of integers m and n
    """
    # ---------- 1. input validation ----------
    if not isinstance(m, int) or not isinstance(n, int):
        raise Exception("Either m or n is not of integer type! ")
    if m < 0 or n < 0:
        raise Exception("Either m or n is negative!")
    # ---------- 2. finding gcd ----------
    # 2.1. order the integers m, n
    a = max(m, n)
    b = min(m, n)
    # 2.2. run the while loop
    while a > 0 and b > 0:
        temp = b
        b = a % b
        a = temp
    d = max(a, b)
    return d


def extended_euclid_algorithm(m, n):
    """
    Implementation of the extended Euclid's algorithm. While euclid_algorithm can do without recursive calls, here it
    is not possible due to the need to update repeatedly the values of the parameters x, y of the linear combination
    that equals d
    :param m: non-negative integer
    :param n: non-negative integer, not larger than m
    :return: 3-tuple (x, y, d) with d = gcd(m, n) and m*x + n*y = d
    """
    # ---------- 1. input validation ----------
    if not isinstance(m, int) or not isinstance(n, int):
        raise Exception("Either m or n is not of integer type! ")
    if m < 0 or n < 0:
        raise Exception("Either m or n is negative!")
    if m < n:
        raise Exception("Parameter m has to be larger than n! ")

    # ---------- 2. executing extended Euclid's algorithm ----------
    # 2.1. bottom-most case: the smaller of the pair of integers is zero
    if n == 0:
        d = m
        x = 1
        y = 0
    # 2.2. non-bottom case: the
    else:
        # recursive self-call: note that n is passed as the first parameter and the remainder from division is passed as
        # the second one
        x, y, d = extended_euclid_algorithm(n, m % n)
        # update the parameters
        temp = x
        x = y
        y = temp - (m // n) * x
    return x, y, d

