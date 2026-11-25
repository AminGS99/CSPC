"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.

V, pH= np.loadtxt("titration.csv", delimiter=",", skiprows=1, unpack=True)

# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.

slope=np.gradient(pH, V)
idx_eq=np.argmax(slope)
v_eq=V[idx_eq]
print(f"Equivalence point volume: {v_eq:.2f} mL")

# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.
fig, (ax1, ax2)= plt.subplots(1,2, figsize=(11, 4.5))

ax1.plot(V, pH, "o-", markersize=3, label="Titration curve")
ax1.axvline(v_eq, color="r", linestyle="--", label=f"Equivalence (~{v_eq:.1f} mL)")
ax1.set_xlabel("Base volume V(mL)")
ax1.set_ylabel("pH")
ax1.set_title("Titration Curve: pH vs Volume")
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2.plot(V, slope, color="darkorange", label="d(pH)/dV")
ax2.axvline(v_eq, color="r", linestyle="--", label=f"Peak at {v_eq:.1f} mL")
ax2.set_xlabel("Base volume V (mL)")
ax2.set_ylabel("d(pH)/dV")
ax2.set_title("Slope of Titration Curve")
ax2.legend()
ax2.grid(True, alpha=0.3)

fig.tight_layout()
plt.savefig("titration.png", dpi=150)
plt.close(fig)