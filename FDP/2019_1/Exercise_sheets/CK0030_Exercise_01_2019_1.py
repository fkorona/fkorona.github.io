from math import fabs, sin, cos, exp, pi, sqrt

# EX 1.1
x_i = +4./5

f1_i = 2**x_i + x_i
g1_i = x_i*fabs(x_i) + 1
h1_i = 5**x_i/(1+5**x_i) + x_i**3

# EX 1.2
x_i = 1.
y_i = 1.

f2_i = 0.26*(x_i**2 + y_i**2) - 0.48*x_i*y_i
g2_i = (x_i**2 + y_i - 11)**2 + (x_i + y_i**2 -7)**2

# EX 1.3
x_i = pi
y_i = pi

f3a_i = sin(y_i) * exp((1-cos(x_i))**2)
f3b_i = cos(x_i) * exp((1-sin(y_i))**2)
f3c_i = (x_i - y_i)**2

f3_i = f3a_i + f3b_i + f3c_i

x_i = 0.
y_i = 0.

gg = y_i + 47.

g3a_i = -gg*sin(sqrt(fabs(x_i/2. + gg)))
g3b_i = -x_i*sin(sqrt(fabs(x_i-gg)))

g3_i = g3a_i + g3b_i
