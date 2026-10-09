import torch
import time

sizes = [50, 100, 200, 400, 800, 1200]
repetitions = [1, 2, 4, 8, 16]

with open("matrix_3d.dat", "w") as file:

    file.write("# MatrixSize Repetitions ExecutionTime\n")

    for n in sizes:

        A = torch.randn(n, n)
        B = torch.randn(n, n)

        for r in repetitions:

            C = A @ B

            start = time.perf_counter()

            for i in range(r):
                C = A @ B

            end = time.perf_counter()

            total_time = end - start

            file.write(f"{n} {r} {total_time:.8f}\n")

        file.write("\n")

print("Part D completed.")