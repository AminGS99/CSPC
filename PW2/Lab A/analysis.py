"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid


t, y=np.loadtxt("freefall.csv", delimiter=",", skiprows=1, unpack=True)

v=np.gradient(y, t)
a=np.gradient(v, t)
print("Mean acceleration:", np.mean(a)) #value is about -8.58. It is noisy
print("Std acceleration:", a.std())
# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)

v_rec=cumulative_trapezoid(a, t, initial=0)+v[0]
y_rec=cumulative_trapezoid(v_rec, t, initial=0)+y[0]
diff = y_rec - y
max_diff = np.max(np.abs(diff))

print(f"Max |y_rec - y|: {max_diff:.4f}")
print("v_rec shape:", v_rec.shape, "y_rec shape:", y_rec.shape)
print("Start/end y vs y_rec:", y[0], y_rec[0], "->", y[-1], y_rec[-1])

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png

fig, axes=plt.subplots(3, 1, sharex=True, figsize=(8, 9))

axes[0].plot(t, y, label="y (measured)")
axes[0].plot(t, y_rec, "--", label="y_rec (integrated)")
axes[0].set_ylabel("Position y")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(t, v, label="v (gradient)")
axes[1].plot(t, v_rec, "--", label="v_rec (integrated)")
axes[1].set_ylabel("Velocity v")
axes[1].legend()
axes[1].grid(True, alpha=0.3)

axes[2].plot(t, a, label="a (gradient)")
axes[2].axhline(-9.81, color="r", linestyle="--", label="True -9.81")
axes[2].set_ylabel("Acceleration a")
axes[2].set_xlabel("Time t")
axes[2].legend()
axes[2].grid(True, alpha=0.3)

fig.tight_layout()
plt.savefig("motion.png", dpi=150)
plt.close(fig)