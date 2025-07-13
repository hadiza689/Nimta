import math

def solve_quadratic(a, b, c):
    """
    Solves a quadratic equation of the form ax² + bx + c = 0
    using the quadratic formula (the Almighty Formula).
    
    Returns:
        A tuple containing the two solutions (real or complex).
    """
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Case 1: Two distinct real roots
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    
    # Case 2: One real root (repeated)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root, root)
    
    # Case 3: Complex roots
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return (root1, root2)

# Get input from user
print("Solving the quadratic equation ax² + bx + c = 0")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Solve the equation
try:
    solutions = solve_quadratic(a, b, c)
    print("\nSolutions:")
    print(f"x₁ = {solutions[0]}")
    print(f"x₂ = {solutions[1]}")
except ZeroDivisionError:
    print("Error: Coefficient 'a' cannot be zero (it is not a quadratic equation).")
