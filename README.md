# CSPC-Lab A: Radioactive Decay Simulation

### 1. Test Status
-All unit tests passed successfully

### 2. Performance Benchmark (`speed.py`)
- **Parameters:** $N0 = 200000$ atoms, $\lambda=0.4$
- **Pure-Python loop (`simulate_loop`):** 1.7788 seconds
- **Vectorised NumPy (`simulate`):** 0.0002 seconds
- **Speed-up factor:** NumPy version is **~10,932.83x faster**.

### 3.Conclusion
Vectorisation using NumPy eliminates slow Python loops, replacing them with optimized C-level operations. This improves performance, making scientific simulations thousands of times faster while keeping high precision.
