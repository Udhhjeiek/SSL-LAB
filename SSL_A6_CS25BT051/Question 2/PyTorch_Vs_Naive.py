import torch
import time

def naive_matrix_multiply(A, B):
    n = len(A)

    C = [[0.0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

sizes = [50, 100, 200]
repetitions = 3

with open("method_comparison.dat", "w") as file:

    file.write("# MatrixSize PyTorchTime NaivePythonTime\n")

    for n in sizes:

        print("--------------------------------")
        print("Matrix size:", n)
        print("--------------------------------")

        A = torch.randn(n, n)
        B = torch.randn(n, n)

        A_python = A.tolist()
        B_python = B.tolist()

        C = A @ B

        pytorch_times = []

        for i in range(repetitions):
            start = time.perf_counter()
            C = A @ B
            end = time.perf_counter()

            pytorch_times.append(end - start)

        pytorch_average = sum(pytorch_times) / len(pytorch_times)

        C_python = naive_matrix_multiply(A_python, B_python)

        naive_times = []

        for i in range(repetitions):
            start = time.perf_counter()
            C_python = naive_matrix_multiply(A_python, B_python)
            end = time.perf_counter()

            naive_times.append(end - start)

        naive_average = sum(naive_times) / len(naive_times)

        print("PyTorch average time:", pytorch_average, "seconds")
        print("Naive Python average time:", naive_average, "seconds")

        file.write(
            f"{n} {pytorch_average:.8f} {naive_average:.8f}\n"
        )

print()
print("Part B completed.")
print("Results saved in method_comparison.dat")