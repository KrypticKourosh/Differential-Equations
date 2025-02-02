import sympy as sp

x = sp.Symbol("x")
y = sp.Function("y")(x)

def taylor_answer(y_prime, a, y_a, h, n):
    """
    Steps:
    1. Compute symbolic derivatives and store them.
    2. Substitute known values iteratively into derivatives.
    3. Use Taylor series formula to approximate the result.
    """
    result = 0
    sub_dict = {x: a, y: y_a}

    # **Manually compute y'(a)**
    y_prime_value = y_prime.subs(sub_dict)
    sub_dict[y.diff(x, 1)] = y_prime_value  # Store first derivative

    # **Loop to compute higher derivatives and store their values**
    y_current_prime = y_prime
    for i in range(2, n):  
        y_next_prime = sp.diff(y_current_prime, x)  # Differentiate
        y_next_prime_value = y_next_prime.subs(sub_dict)  # Substitute known values
        sub_dict[y.diff(x, i)] = y_next_prime_value  # Store in dictionary
        y_current_prime = y_next_prime  # Update for next iteration

    sub_dict.pop(x) #only y's are used in the taylor series
    derivative_values = list(sub_dict.values())

    # **Compute Taylor series result**
    for i in range(n):
        result += ((h ** i) / sp.factorial(i)) * derivative_values[i]

    return result

