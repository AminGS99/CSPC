"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


t, C=np.loadtxt("kinetics.csv", delimiter=",", skiprows=1, unpack=True)
C0=C[0]


def total_error(k):
    k_val=k[0]
    C_model=C0*np.exp(-k_val*t)
    return np.sum((C-C_model)**2)


result= minimize(total_error, x0=0.5, method="SLSQP", bounds=[(0,5)])
print("Success:", result.success)
k_fit=result.x[0]
print(f"Fitted rate constant k: {k_fit:.6f}")

t_smooth=np.linspace(t.min(), t.max(), 200)
C_fit=C0*np.exp(-k_fit*t_smooth)

plt.figure(figsize=(7,5))
plt.scatter(t, C, label="Measured data", alpha=0.8)
plt.plot(t_smooth, C_fit, "r-", linewidth=2, label=f"Fit: C0*exp(-{k_fit:.4f} t)")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.title("First-Order Reaction Kinectics Fit")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("kinetics.png", dpi=150)
plt.close()
