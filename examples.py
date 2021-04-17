import euclid_algorithm as ea
import least_common_multiple as lcm
import base_representations as br

# ----------------------------------------------------------------------------------------------------------------------
# -------------------------                     euclid_algorithm.py                 ------------------------------------
# 1. euclid_algorithm()
print(ea.euclid_algorithm(0, 0))
print(ea.euclid_algorithm(10, 0))
print(ea.euclid_algorithm(0, 10))
print(ea.euclid_algorithm(15, 25))
# 2. ea.extended_euclid_algorithm()
print(ea.extended_euclid_algorithm(0, 0))
print(ea.extended_euclid_algorithm(10, 0))
print(ea.extended_euclid_algorithm(25, 10))
x, y, d = ea.extended_euclid_algorithm(25, 10)
print(x*25 + y*10)
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------                   least_common_multiple.py               ---------------------------------
# 1. least_common_multiple()
print(lcm.least_common_multiple(1, 2))
print(lcm.least_common_multiple(3, 5))
print(lcm.least_common_multiple(30, 15))
print(lcm.least_common_multiple(6, 14))
# 2. find_modular_inverse()
print(lcm.find_modular_inverse(10, 13))
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------              base_representations.py             -----------------------------------
# 1. find_binary_number_representation_indep()
print(br.find_binary_number_representation_indep(5))
print(br.find_binary_number_representation_indep(0))
# 2. find_number_representation_in_base_b()
print(br.find_number_representation_in_base_b(100, 9))
# 3. find_binary_number_representation_dep()
print(br.find_binary_number_representation_dep(5))
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------              base_representations.py             -----------------------------------

# ----------------------------------------------------------------------------------------------------------------------
