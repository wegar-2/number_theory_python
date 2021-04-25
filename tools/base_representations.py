

def find_number_representation_in_base_b(n, b):
    """
    Finds representation of natural number n in system with base b
    :param n: natural number whose representation is to be found
    :param b: base of the system; allowed values: 2, 3, ..., 9
    :return: list os ints, each int is the coefficient corresponding to consecutive powers of b; the power of b increases
    from left to right of the list
    """
    # ---------- 1. input validation ----------
    if not isinstance(n, int) or not isinstance(b, int):
        raise Exception("One of the parameters n, b is not an integer! ")
    if b <= 1 or b >= 10:
        raise Exception("Parameter b is outside of the allowed scope 2, 3, ..., 9 !!!")
    if n < 0:
        raise Exception("Parameter n is negative integer! ")
    # ---------- 2. calculating base-b representation ----------
    base_b_representation_list = []
    q = n
    while q > 0:
        q0 = q // b
        r = q % b
        q = q0
        base_b_representation_list.append(r)
    if len(base_b_representation_list) == 0:
        return [0]
    else:
        return base_b_representation_list


def find_binary_number_representation_dep(n):
    """
    Finds representation of natural number n in system with base 2 using the function find_number_representation_in_base_b
    :param n: number whose binary representation is to be found
    :return: list os ints, each int is the coefficient corresponding to consecutive powers of 2; the power of 2 increases
    from left to right of the list
    """
    # ---------- 1. input validation ----------
    if not isinstance(n, int):
        raise Exception("Parameter n is not of int type!")
    if n < 0:
        raise Exception("Parameter n is negative integer! ")
    # ---------- 2. get the binary representation ----------
    binary_representation = find_number_representation_in_base_b(n, 2)
    return binary_representation


def find_binary_number_representation_indep(n):
    """
    This is a stand-alone function for finding binary representation of non-negative integer n
    :param n: int type variable, non-negative
    :return: list os ints, each int is the coefficient corresponding to consecutive powers of 2; the power of 2 increases
    from left to right of the list
    """
    # ---------- 1. input validation ----------
    if not isinstance(n, int):
        raise Exception("Parameter n is not of int type!")
    if n < 0:
        raise Exception("Parameter ")
    # ---------- 2. getting binary representation ----------
    binary_list = []
    q = n
    while q > 0:
        q0 = q // 2
        r = q % 2
        q = q0
        binary_list.append(r)
    if len(binary_list) == 0:
        return [0]
    else:
        return binary_list


def list_to_string(list_representation):
    # reverse the order of list elements and concatenate into string
    list_representation.reverse()
    list_representation = [str(el) for el in list_representation]
    return ''.join(list_representation)


