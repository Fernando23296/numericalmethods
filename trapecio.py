from math import sin,pi,e

def trapecio(a, b, f, n):

  h = (b - a)/n
  S = 0.5 * (f(a) + f(b))
  for i in range(1, n):
    S += f(a + i * h)
    integral = h * S
  
  return integral
