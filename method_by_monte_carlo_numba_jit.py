# Finding Polynomial Definite Integral
import random
from math import pow
from timer import timer  # pip install timer
from numba import njit


@njit
def polynomial_function(x, coefficients):
    current_result = 0
    for i in range(len(coefficients)):
        n_without_sum_i_1 = len(coefficients) - i - 1
        current_result += coefficients[i] * pow(x, n_without_sum_i_1)
    return current_result


@njit
def primitive(x, coefficients):
    m_1 = []
    for i in range(len(coefficients)):
        m_1.append(coefficients[i] / (len(coefficients) - i))
    m_1.append(0)
    return polynomial_function(x, m_1)


@njit
def method_by_monte_carlo(left_bound, right_bound, number_of_the_dots, coefficients):
    current_result = 0
    delta_x = (right_bound - left_bound) / number_of_the_dots
    for i in range(number_of_the_dots):
        ksi = random.random()
        x = ksi * delta_x + left_bound + i * delta_x
        current_result += polynomial_function(x, coefficients)
    return current_result * delta_x


@njit
def formula_by_newton_leibniz(left_bound, right_bound, coefficients):
    return primitive(right_bound, coefficients) - primitive(left_bound, coefficients)


def enter_data():
    coefficients = tuple(map(
        int, input('Enter the coefficients of the polynomial in descending order of the degree of monomials: ').split()
    ))

    left_bound = float(input('Enter the left bound: '))
    right_bound = float(input('Enter the right bound: '))
    number_of_the_dots = int(input(
        'Enter the number of the dots '
        '(the more dots you enter, the more precision you achieve and the more time will be spent): '
    ))
    return coefficients, left_bound, right_bound, number_of_the_dots


def perform_calculations(coefficients, left_bound, right_bound, number_of_the_dots):
    with timer(unit='ms') as mc_timer:
        calculated_with_method_by_monte_carlo = \
            method_by_monte_carlo(left_bound, right_bound, number_of_the_dots, coefficients)
        print('Integral calculated by the Monte Carlo\'s method: ',
              calculated_with_method_by_monte_carlo)
        print('Time elapsed:', mc_timer.elapse, 'ms')
        print()

    with timer(unit='ms') as nl_timer:
        calculated_with_formula_by_newton_leibniz = formula_by_newton_leibniz(left_bound, right_bound, coefficients)
        print('The integral calculated using the Newton-Leibniz formula: ',
              calculated_with_formula_by_newton_leibniz)
        print('Time elapsed:', nl_timer.elapse, 'ms')
        print()

    print('Monte Carlo accuracy: ',
          min(
            calculated_with_method_by_monte_carlo / calculated_with_formula_by_newton_leibniz,
            calculated_with_formula_by_newton_leibniz / calculated_with_method_by_monte_carlo
          )
          )


def main():
    data = enter_data()
    print()
    perform_calculations(*data)


if __name__ == "__main__":
    main()
