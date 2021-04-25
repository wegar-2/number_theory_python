from tools import euclid_algorithm as ea


def least_common_multiple(m, n):
    """
    Calculate the least common divisor of non-zero natural numbers m and n
    :param m: positive integer
    :param n: positive integer
    :return: least common multiple of m and n, non-zero natural number (Python type: integer)
    """
    # ---------- 1. input validation ----------
    if not isinstance(m, int) or not isinstance(n, int):
        raise Exception("Either m or n is not of integer type! ")
    if m <= 0 or n <= 0:
        raise Exception("Either m or n is non-positive!")
    # ---------- 2. calculate gcd and return ----------
    d = ea.euclid_algorithm(m, n)
    return int(m*n/d)


def find_modular_inverse(x, n):
    """
    Calculate inverse of the non-zero integer x modulo n
    :param x: positive integer in between 1 and (n-1) whose modular inverse is to be calculated
    :param n: integer, larger than 1, modulus for which the inverse is to be calculated
    :return: inverse of x modulo n (Python int) if exists, otherwise returns None
    """
    # ---------- 1. input validation ----------
    if not isinstance(x, int) or not isinstance(n, int):
        raise Exception("Either m or n is not of integer type! ")
    if n <= 1:
        raise Exception("The indicated modulus is smaller than 1! ")
    if x <= 0 or x >= n:
        raise Exception("The indicated x is outside of the allowed range")
    # ---------- 2. run the Euclid's extended algorithm and return ----------
    x0, y0, d = ea.extended_euclid_algorithm(n, x)
    if d != 1:
        return None
    else:
        return y0
