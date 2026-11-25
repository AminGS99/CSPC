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