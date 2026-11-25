"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0


def grad_descent(df, x0, lr=0.1, tol=1e-8, max_iter=10000):
    x=float(x0)
    for _ in range(max_iter):
        step=lr*df(x)
        x-=step
        if abs(step)<tol:
            break
    return x

x0_2a= 0.0
gd_2a=grad_descent(df, x0_2a, lr=0.1)
nw_2a=newton(df, x0=x0_2a, fprime=d2f)
slsqp_2a=minimize(f, x0=[x0_2a], method="SLSQP").x[0]

print(f"Gradient descent: {gd_2a:.6f}")
print(f"Newton: {nw_2a:.6f}")
print(f"SLSQP:  {slsqp_2a:.6f}")

# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.
#   For Newton (which solves dg(x)=0), also check the sign of d2g at the answer:
#   d2g > 0 means a minimum, d2g < 0 means a maximum.
#   In your README note: do the methods agree? did Newton find a minimum or
#   another stationary point? how did the starting point change the result?

for x0 in [0.0, 2.0]:
    gd_2b=grad_descent(dg, x0, lr=0.05)
    nw_2b=newton(dg, x0=x0, fprime=d2g)
    slsqp_2b=minimize(g, x0=[x0], method="SLSQP").x[0]
    sign_nw=d2g(nw_2b)
    kind_nw="minimum" if sign_nw>0 else ("maximum" if sign_nw<0 else "saddle/flat")

    print(f"\n   2B: g(x) from x0={x0}   ")
    print(f"Gradient descent: x={gd_2b:.6f} (g''={d2g(gd_2b):.4f})")
    print(f"Newton:  x={nw_2b:.6f} (g''={sign_nw:.4f} -> {kind_nw})")
    print(f"SLSQP: x={slsqp_2b:.6f} (g''={d2g(slsqp_2b):.4f})")