from tools import base_representations as br


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


def modular_exponentiation(b, e, m):
    # 1. find binary representation of the exponent e
    bin_rep_list = br.find_binary_number_representation_indep(e)
    # 2. calculate the required powers of 2
    list_powers_of_two = list(range(0, len(bin_rep_list)))
    list_modular_powers = [0] * len(list_powers_of_two)
    for i in range(0, len(list_powers_of_two)):
        if i == 0:
            list_modular_powers[i] = b % m
        else:
            list_modular_powers[i] = ((list_modular_powers[i-1]) * (list_modular_powers[i-1])) % m
    # 3. use the powers of 2 to calculate the modular exponent
    c = 1
    for i in range(0, len(bin_rep_list)):
        if bin_rep_list[i] == 1:
            c = (list_modular_powers[i] * c) % m
    return c


