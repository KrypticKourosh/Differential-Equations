from taylor_series import taylor_answer
from sympy import Symbol, Function


x = Symbol("x")
y = Function("y")(x)

def main():
    # Inputs:
    y_prime = x - y ** 2
    a, y_a = 1, 1  # Initial conditions
    h = 0.2  # Step size
    n = 4  # Number of Taylor series terms

    result = taylor_answer(y_prime, a, y_a, h, n)
    print(f"{result:.5f}")


if __name__ == "__main__":
    main()
