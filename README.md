# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under `PW<n>/Lab <X>/`.

## Setup
Create the environment for a given lab:
```bash
    conda env create -f PW<n>/Lab <X>/environment.yml
    conda activate cspc
```
Run the tests for a lab inside its folder:
``` bash
cd "PW<n>/Lab <X>"
pytest -v
```

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- A vectorized radioactive decay simulation using NumPy and a pure-Python loop version, accompanied by automated pytest unit tests.

**Speed comparison (loop vs NumPy):**
- loop : 1.7788 s
- numpy : 0.0002 s
- speed-up : 10932.83 x faster

**Tests:** all passing? (yes / no)
- yes

**Conclusion:**
Vectorisation using NumPy eliminates slow Python interpreter loops, replacing them with optimized C-level operations. This improves performance, making scientific simulations thousands of times faster while keeping high precision.


## PW1 - Lab B: Data, Plotting and Automation

**Observation:**
- The observed dataset shows counts decreasing from initial value N0 over time following the analytical curve N=N0 * e^(-lambda*t).

**Snakemake pipeline**
- Snakemake takes `decay_observed.csv` as input, runs `plot.py` and generates `figure.png` if output is missing or outdated.


## PW2 - Lab A: Motion from Tracking Data

### Results & Observations
- **Mean acceleration:** `-8.58 m/s²` (expected `~-9.81 m/s²`)

- **Acceleration standard deviation:** `28.72 m/s²`

- **Differentiation & Noise:** Differentiating noisy position measurements twice magnifies small noise into large swings in acceleration while position itself has no derivatives taken and remains smooth.

- **Integration & Recovery:** Integrating the noisy acceleration twice back to position gives a largest difference of `0.7846` m, matching the original trajectory within about a meter because integration cancels out random noise.


## PW2 - Lab B: Optimization in Chemistry

### Warm-up: Comparing Optimization Methods
- **An easy convex function $f(x)=(x - 3)^2+1$ (`x0 = 0`):** Gradient descent, Newton's method, and SLSQP all agreed and converged to the unique global minimum at `x = 3.000000`.
- **A harder landscape $g(x) = x^4 - 3x^2 + x + 5$:**
  - **Agreement & Newton's stationary point:** The methods did not all agree. From `x0 = 0.0`, gradient descent and SLSQP reached the global minimum `x ≈ -1.3008`, while Newton's method converged to `x ≈ 0.1699` (a **local maximum**, because Newton only searches for $g'(x) = 0$).
  - **Effect of the starting point:** Changing the start to `x0 = 2.0` caused both gradient descent and Newton to settle into the nearby local minimum at `x ≈ 1.1309` ($g'' ≈ 9.35 > 0$), while SLSQP stepped across to the global minimum at `x ≈ -1.3006`.

### Chemistry 1: Fitting a Reaction Rate
- **Kinetics Reaction:** Fitting $C(t) = C_0 e^{-kt}$ with SLSQP gave a rate constant of `k~0.2618` (close to `0.25`), with fitted curve tracking the noisy concentration measuremnets in `kinetics.png`.

### Chemistry 2: Chemical Equilibrium
- **Chemical equilibrium** For H2 + I2 ⇌ HI ($K = 15.6$, starting from 1 mol each of H2 and I2), root-finding with newton and squared-imbalance minimization with SLSQP agreed on $x \approx 0.6638$, yielding `0.3362 mol` H2, `0.3362 mol` I2, and `1.3277 mol` HI (plotted in `equilibrium.png`). 
### Chemistry 3:
- **Titration equivalence point :** Differentiating pH with respect to base volume via `np.gradient` and finding `np.argmax` located the steepest pH jump (equivalence point) at approximately `<titration_vol> mL` , plotted alongside `d(pH)/dV` in `titration.png`