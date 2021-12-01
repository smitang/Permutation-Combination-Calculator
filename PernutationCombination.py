# Author: Stephen Tang
# Date: 12/1/2021
# Description: This program allows the user to calculate permutations and combinations based on 3 given formulas: (1)
# permutation of selected elements, (2) combinations of counting subsets of a set, and (3) combinations of counting
# subsets of a set with repetition

while True:
    def factorial_n(integer_n):                                 # calculating n!
        if integer_n == 0 or integer_n == 1:
            return 1
        else:
            return integer_n * factorial_n(integer_n - 1)

    def factorial_r(integer_r):                                 # calculating r!
        if integer_r == 0 or integer_r == 1:
            return 1
        else:
            return integer_r * factorial_r(integer_r - 1)

    def factorial_n_minus_r(integer_n, integer_r):              # calculating (n - r)!
        diff_integer = integer_n - integer_r
        return factorial_n(diff_integer)

    def comb_with_rep(integer_n, integer_r):                    # calculating (r + n - 1)C(r)
        numerator = integer_r + integer_n - 1
        denominator = integer_r
        total = factorial_n(numerator) / (factorial_r(denominator) * factorial_n_minus_r(numerator, denominator))
        return total

    choice_formula = int(input(
        '''
        Which formula would you like to use? Please enter the correct corresponding integer:
        1) Permutation of Selected Elements
        2) Combinations of Counting Subsets of a Set
        3) Combinations of Counting Subsets of a Set with Repetition
        '''))
    if choice_formula == 1:
        print("Ok, you have chosen: Permutation of Selected Elements")
        num_elements = int(input("Please enter a positive integer for number of elements (n): "))
        num_subsets = int(input("Please enter a positive integer for number of subsets (r): "))
        result = factorial_n(num_elements)/factorial_n_minus_r(num_elements, num_subsets)
        print("Your total number of permutations are", result)
    elif choice_formula == 2:
        print("Ok, you have chosen: Combinations of Counting Subsets of a Set")
        num_elements = int(input("Please enter a positive integer for number of elements (n): "))
        num_subsets = int(input("Please enter a positive integer for number of subsets (r): "))
        result = factorial_n(num_elements)/(factorial_r(num_subsets) * factorial_n_minus_r(num_elements, num_subsets))
        print("Your total number of combinations are", result)
    elif choice_formula == 3:
        print("Ok, you have chosen: Combinations of Counting Subsets of a Set with Repetition.")
        num_elements = int(input("Please enter a positive integer for number of elements (n): "))
        num_subsets = int(input("Please enter a positive integer for number of subsets (r): "))
        print("Your total number of combinations are", comb_with_rep(num_elements, num_subsets))
    else:
        print("Sorry, number is invalid. Please try again.")
    continue_calc = input("Would you like to perform another calculation? If Yes enter 'Y'. If No enter 'N': ")
    if continue_calc == "N":
        print("Thank you for using Permutation Combination Calculator!")
        break
