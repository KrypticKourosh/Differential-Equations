from taylor_series import taylor_answer
from sympy import Symbol, Function, sympify

x = Symbol("x")
y = Function("y")(x)

def get_data():
    print("-----------------------------")
    print("Taylor series: ")
    y_prime = input("1.Enter y'(x): ")
    a, y_a = map(float, input("2.Enter initial conditions (a, y(a)): ").split())
    h = float(input("3.Enter step size (h): "))
    n = int(input("4.Enter number of Taylor series terms (n): "))
    print("-----------------------------")

    y_prime = sympify(y_prime, locals={"x" : x, "y" : y})
    return [y_prime, a, y_a, h, n]

def main():
    y_prime, a, y_a, h, n = get_data()
    result = taylor_answer(y_prime, a, y_a, h, n)
    print(f"{result:.5f}")


if __name__ == "__main__":
    main()
