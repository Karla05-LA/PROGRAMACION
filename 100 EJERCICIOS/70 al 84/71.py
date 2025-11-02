
import sympy as sp

x = sp.Symbol('x')

# a) x^2 - 5x + 7 = 0
eq1 = sp.Eq(x**2 - 5*x + 7, 0)
sol1 = sp.solve(eq1, x)
print("\na) Solución de x^2 - 5x + 7 = 0 →", sol1)

# b) 7x^2 + 9x - 8x^2 - 2x - 3 = 0
eq2 = sp.Eq(7*x**2 + 9*x - (8*x**2 - 2*x - 3), 0)
sol2 = sp.solve(eq2, x)
print("b) Solución de 7x^2 + 9x = 8x^2 - 2x - 3 →", sol2)
