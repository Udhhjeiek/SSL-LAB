import torch
import time

sizes = [50, 100, 200, 400, 800, 1200]

repetitions = 5

with open("matrix_results.dat", "w") as file:

    file.write("# MatrixSize AverageTime MinimumTime\n")

    for n in sizes:

        A = torch.randn(n, n)
        B = torch.randn(n, n)

        C = A @ B

        times = []

        for i in range(repetitions):

            start = time.perf_counter()

            C = A @ B

            end = time.perf_counter()

            elapsed = end - start

            times.append(elapsed)

        average_time = sum(times) / len(times)

        minimum_time = min(times)

        print("Matrix size:", n)
        print("Average time:", average_time)
        print("Minimum time:", minimum_time)
        print()

        file.write(
            f"{n} {average_time:.8f} {minimum_time:.8f}\n"
        )


print("Part A completed.")
print("Results saved in matrix_results.dat")