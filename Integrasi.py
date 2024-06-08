import numpy as np
import matplotlib.pyplot as plt
import time

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Metode Simpson 1/3
def simpson_1_3(f, a, b, N):
    if N % 2 == 1:
        N += 1  # N harus genap untuk metode Simpson 1/3
    h = (b - a) / N
    x = np.linspace(a, b, N+1)
    fx = f(x)
    
    integral = fx[0] + fx[-1]
    for i in range(1, N, 2):
        integral += 4 * fx[i]
    for i in range(2, N-1, 2):
        integral += 2 * fx[i]
    
    integral *= h / 3
    return integral

# Nilai referensi pi
pi_ref = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Menyimpan hasil
results = []

for N in N_values:
    start_time = time.time()
    pi_approx = simpson_1_3(f, 0, 1, N)
    end_time = time.time()
    
    rms_error = np.sqrt((pi_approx - pi_ref)**2)
    exec_time = end_time - start_time
    
    results.append((N, pi_approx, rms_error, exec_time))

# Extract results
N_values = [result[0] for result in results]
pi_approximations = [result[1] for result in results]
rms_errors = [result[2] for result in results]
execution_times = [result[3] for result in results]

# Plotting the approximation of pi vs N
plt.figure(figsize=(12, 6))

# Subplot 1: Approximation of Pi vs N
plt.subplot(1, 3, 1)
plt.plot(N_values, pi_approximations, 'bo-', label='Approximation of Pi')
plt.axhline(y=pi_ref, color='r', linestyle='--', label='Reference Pi')
plt.xscale('log')
plt.xlabel('N (log scale)')
plt.ylabel('Approximation of Pi')
plt.title('Approximation of Pi vs N')
plt.legend()

# Subplot 2: RMS Error vs N
plt.subplot(1, 3, 2)
plt.plot(N_values, rms_errors, 'go-', label='RMS Error')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N (log scale)')
plt.ylabel('RMS Error (log scale)')
plt.title('RMS Error vs N')
plt.legend()

# Subplot 3: Execution Time vs N
plt.subplot(1, 3, 3)
plt.plot(N_values, execution_times, 'ro-', label='Execution Time')
plt.xscale('log')
plt.xlabel('N (log scale)')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs N')
plt.legend()

plt.tight_layout()
plt.show()
