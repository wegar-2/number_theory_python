import euclid_algorithm as ea


def crt_find_number_two_modules(n1, r1, n2, r2):
    """
    Given two moduli n1, n2 that are relatively prime and given the remainders for these moduli, respectively, r1 and r2
    this function finds a natural number in between 0 and (n1*n2 - 1) that is congruent to r1 modulo n1 and r2 modulo n2
    :param n1: first modulus, int type
    :param r1: remainder modulo n1, int type
    :param n2: second modulus, int type
    :param r2: remainder modulo n2, int type
    :return: least positive integer that satisfies the condition
    """
    # ---------- 1. input validation ----------
    # 1.1. check if n1, r1, n2, r2 are integers
    if not isinstance(n1, int) or not isinstance(n2, int) or not isinstance(r1, int) or not isinstance(r2, int):
        raise Exception("One of the function parameters is not of integer type...")
    # 1.2. check if the values passed are in the allowed ranges: n1, n2
    if n1 <= 1 or n2 <= 1:
        raise Exception("One of the function parameters n1, n2 is not at least 2!")
    # 1.3. check if the values passed are in the allowed ranges: r1, r2
    if not (0 <= r1 < n1) or not (0 <= r2 < n2):
        raise Exception("One of the function parameters r1, r2 is out of the allowed ranges - cf. n1, n2 values!")
    # ---------- 2. find the number satisfying the required condition ----------
    # 2.1. run the extended Euclid's algorithm
    if n1 <= n2:
        temp = n1
        n1 = n2
        n2 = temp
    x, y, d = ea.extended_euclid_algorithm(m=n1, n=n2)
    if d != 1:
        raise Exception("The parameters n1 and n2 are not coprime! ")
    # 2.2. calculate the value that satisfies the required condition using x, y directly and return
    n0 = r2*n1*x + r1*n2*y
    return n0 % (n1*n2)

