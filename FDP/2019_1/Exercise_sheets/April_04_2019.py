# Ex. 1

x1 = 0.
x2 = 0.
x3 = 0.
x4 = 0.

y3a = 100*( (x2-x1**2)**2 + (x3-x2**2)**2 + (x4-x3**2)**2)
y3b = (1-x1)**2 + (1-x2)**2 + (1-x3)**2
y3 = y3a + y3b

# Ex. 2
from math import sin, exp, fabs, sqrt, pi

xx = 0.
yy = 0.

y2a = fabs(sin(xx)*sin(yy)*exp(fabs(100-sqrt(xx**2+yy**2)/pi)))
y2 = -0.0001*(y2a+1)**0.1

# Ex. 3
from math import cos, e
x = 0.
y = 0.

y1a = 20*exp(-0.2*sqrt(0.5*(x**2+y**2)))
y1b = exp(0.5*(cos(2*pi*x) + cos(2*pi*y)))
y1 = -y1a - y1b + e + 20

# Ex. 4
from math import log

x1 = 1.
x2 = 2.
x3 = 3.
x4 = 4.

y0a = (log(log(x1))/log(x1))**x1
y0b = (log(log(x2))/log(x2))**x2
y0c = (log(log(x3))/log(x3))**x3
y0d = (log(log(x4))/log(x4))**x4
y0 = y0a + y0b + y0c + y0d

# Ex. 5
from math import atan

x = 0.

ynum = x**5 + x**2*log(x)
yden = x**3 + x**6*log(2*atan(x)/pi) - (2./pi)*x**5
y = ynum/ydem

# Ex. 6

x = 25.
mu = 4.
sigma = 1.

pc = 1./sqrt(2*pi*sigma**2)
pb = 1./x
pa = exp(- 1./(2*sigma**2) * (log(x) - mu)**2)

p = pc*pb*pa
