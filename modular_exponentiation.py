
def modular_exponentiation_special_case(b, k, m):
    """
    Calculates modular exponent b^e mod m for the special case where e = 2^k, i.e. for the case where e is a power of two
    :param b: positive integer
    :param k:
    :param m: modulus to use in the calculation
    :return:
    """
    if k == 0:
        return b % m
    elif k > 0:
        c = b % m
        print("c before loop: ", c)
        for i in range(1, k+1):
            print("c before ", i ,"-th iteration: ", c)
            c = (c * c) % m
            print("c after ", i, "-th iteration: ", c)
        return c

# modular_exponentiation_special_case(b=3, k=8, m=7)