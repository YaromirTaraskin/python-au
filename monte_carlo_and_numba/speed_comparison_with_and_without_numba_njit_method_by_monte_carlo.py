from monte_carlo_and_numba import method_by_monte_carlo_numba_jit, method_by_monte_carlo


def print_divider():
    print()
    print("---")
    print()


def main():
    data = method_by_monte_carlo.enter_data()
    print_divider()
    print("Calculating without numba njit...")
    print()
    method_by_monte_carlo.perform_calculations(*data)
    print_divider()
    print("Calculating with numba njit...")
    print()
    method_by_monte_carlo_numba_jit.perform_calculations(*data)
    print_divider()


if __name__ == "__main__":
    main()