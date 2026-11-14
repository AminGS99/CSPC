import time
from decay import simulate, simulate_loop

def speed_comparison():
    N0 = 200000
    lam=0.4

    t0=time.perf_counter()
    simulate_loop(N0, lam)
    time_loop=time.perf_counter()-t0 

    t0=time.perf_counter()
    simulate(N0, lam)
    time_numpy = time.perf_counter() - t0

    speedup = time_loop / time_numpy

    print(f"Pure Python simulate_loop: {time_loop: .4f} seconds")
    print(f"Vectorised NumPy simulate: {time_numpy: .4f} seconds")
    print(f"Numpy version is {speedup:.2f}x faster")

if __name__=="__main__":
    speed_comparison()
