# Taylor Series Differential Equation Solver

A Python implementation of the Taylor series method for solving ordinary differential equations (ODEs) numerically. This project demonstrates advanced mathematical programming concepts including symbolic computation, automatic differentiation, and iterative numerical methods.

## Mathematical Background

The Taylor series method approximates the solution to a differential equation by expanding the unknown function around a known point using its derivatives. For a function y(x) with initial condition y(a) = y₀, the Taylor series expansion is:

```
y(a + h) ≈ y(a) + h·y'(a) + (h²/2!)·y''(a) + (h³/3!)·y'''(a) + ... + (hⁿ/n!)·y⁽ⁿ⁾(a)
```

This method is particularly useful for:
- Initial value problems where analytical solutions are difficult
- Cases requiring high precision control
- Educational purposes to understand numerical methods

## Key Features

- **Automatic Symbolic Differentiation**: Computes higher-order derivatives automatically using SymPy
- **Iterative Substitution Algorithm**: Handles complex dependency chains between derivatives
- **Flexible Input**: Accepts arbitrary differential equations in symbolic form
- **Configurable Precision**: User-defined number of Taylor series terms
- **General Purpose Solver**: Works with any first-order ODE that can be expressed symbolically

## Technical Implementation

### Core Algorithm

1. **Symbolic Differentiation**: Uses SymPy to compute successive derivatives of the given differential equation
2. **Iterative Substitution**: Evaluates each derivative at the initial point, storing results for use in subsequent derivative calculations
3. **Taylor Series Construction**: Applies the Taylor series formula with computed derivative values

### Key Technical Challenges Solved

- **Dependency Management**: Each higher derivative depends on previously computed values
- **Symbolic-to-Numeric Conversion**: Seamless transition from symbolic expressions to numerical values
- **Dynamic Computation**: Calculates arbitrary number of terms without hardcoding specific cases

## Usage

### Basic Example
```python
python main.py
```

### Input Format
- **Differential Equation**: Enter y'(x) in terms of x and y (e.g., "x - y**2")
- **Initial Conditions**: Provide point and function value (e.g., "1 1" for y(1) = 1)
- **Step Size**: Distance from initial point (e.g., 0.2 for computing y(1.2))
- **Number of Terms**: Precision control (more terms = higher accuracy)

### Sample Problem
```
Solve: y' = x - y²
Initial condition: y(1) = 1
Compute: y(1.2) using 4 terms

Expected output: 1.01733
```

## Code Structure

- **`taylor_series.py`**: Core mathematical engine
  - `taylor_answer()`: Main solver function implementing the Taylor series algorithm
- **`main.py`**: User interface and input handling
  - `get_data()`: Input parsing and validation
  - `main()`: Program execution flow

## Mathematical Accuracy

The accuracy of the solution depends on:
- **Number of terms**: More terms generally improve accuracy
- **Step size**: Smaller steps increase precision but require more computational steps
- **Function behavior**: Smooth functions converge better than those with discontinuities

## Dependencies

- **SymPy**: For symbolic mathematics and automatic differentiation
- **Python 3.x**: Standard library functions

## Installation

```bash
pip install sympy
```

## Example Use Cases

This solver can handle various types of first-order ODEs:
- Linear equations: `y' = 2*x + 3*y`
- Nonlinear equations: `y' = x*y**2 + sin(x)`
- Separable equations: `y' = y*(1-y)`
- Bernoulli equations: `y' + y = x*y**2`

## Limitations

- Currently supports first-order ODEs only
- Requires the differential equation to be expressible in explicit form y' = f(x,y)
- Convergence depends on the mathematical properties of the specific equation
- Large step sizes may lead to divergence for certain equations

## Development Notes

This project was developed over several weeks, involving:
- Research into numerical methods for differential equations
- Implementation of symbolic computation techniques
- Design of the iterative substitution algorithm
- Testing with various mathematical examples

The implementation demonstrates the intersection of pure mathematics and computational programming, showcasing how symbolic mathematics libraries can be leveraged to create sophisticated numerical solvers.
