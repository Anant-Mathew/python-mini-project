
import numpy as np

# ---- helper : print matrix nicely ----
def print_matrix(mat, name="Matrix"):
    print(f"\n  {name} :")
    print("  " + "-" * (len(mat[0]) * 8))
    for row in mat:
        row_str = "  | "
        for val in row:
            row_str += f"{val:>6.2f} "
        row_str += "|"
        print(row_str)
    print("  " + "-" * (len(mat[0]) * 8))


# ---- helper : take matrix input from user ----
def input_matrix(name="A"):
    print(f"\n  Enter details for Matrix {name}")
    rows = int(input(f"  Number of rows    : "))
    cols = int(input(f"  Number of columns : "))
    print(f"  Enter {rows * cols} elements row by row (space separated) :")
    data = []
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"  Row {i+1} : ").split()))
                if len(row) != cols:
                    print(f"  !! Please enter exactly {cols} values")
                    continue
                data.append(row)
                break
            except ValueError:
                print("  !! Only numbers please!")
    return np.array(data)


# ---- menu ----
def show_menu():
    print("\n" + "=" * 45)
    print("       MATRIX OPERATIONS TOOL")
    print("=" * 45)
    print("  1. Matrix Addition       (A + B)")
    print("  2. Matrix Subtraction    (A - B)")
    print("  3. Matrix Multiplication (A x B)")
    print("  4. Transpose             (A^T)")
    print("  5. Determinant           |A|")
    print("  6. Inverse               (A^-1)")
    print("  7. Exit")
    print("=" * 45)
    choice = input("  Choose an option (1-7) : ")
    return choice


# ---- operations ----

def addition():
    print("\n--- MATRIX ADDITION ---")
    A = input_matrix("A")
    B = input_matrix("B")
    if A.shape != B.shape:
        print("\n  !! Error: Matrices must have same size for addition!")
        return
    result = A + B
    print_matrix(A, "Matrix A")
    print_matrix(B, "Matrix B")
    print_matrix(result, "Result A + B")


def subtraction():
    print("\n--- MATRIX SUBTRACTION ---")
    A = input_matrix("A")
    B = input_matrix("B")
    if A.shape != B.shape:
        print("\n  !! Error: Matrices must have same size for subtraction!")
        return
    result = A - B
    print_matrix(A, "Matrix A")
    print_matrix(B, "Matrix B")
    print_matrix(result, "Result A - B")


def multiplication():
    print("\n--- MATRIX MULTIPLICATION ---")
    A = input_matrix("A")
    B = input_matrix("B")
    if A.shape[1] != B.shape[0]:
        print(f"\n  !! Error: Columns of A ({A.shape[1]}) must equal rows of B ({B.shape[0]})!")
        return
    result = np.dot(A, B)
    print_matrix(A, "Matrix A")
    print_matrix(B, "Matrix B")
    print_matrix(result, "Result A x B")


def transpose():
    print("\n--- MATRIX TRANSPOSE ---")
    A = input_matrix("A")
    result = A.T
    print_matrix(A, "Matrix A")
    print_matrix(result, "Transpose A^T")


def determinant():
    print("\n--- DETERMINANT ---")
    A = input_matrix("A")
    if A.shape[0] != A.shape[1]:
        print("\n  !! Error: Matrix must be square (n x n) for determinant!")
        return
    det = np.linalg.det(A)
    print_matrix(A, "Matrix A")
    print(f"\n  Determinant |A| = {det:.4f}")


def inverse():
    print("\n--- MATRIX INVERSE ---")
    A = input_matrix("A")
    if A.shape[0] != A.shape[1]:
        print("\n  !! Error: Matrix must be square (n x n) for inverse!")
        return
    det = np.linalg.det(A)
    if abs(det) < 1e-10:
        print("\n  !! Error: Matrix is singular (det = 0), inverse does not exist!")
        return
    result = np.linalg.inv(A)
    print_matrix(A, "Matrix A")
    print_matrix(result, "Inverse A^-1")


# ---- main program ----

print("\n  Welcome to Matrix Operations Tool!")
print("  Made with Python + NumPy")

while True:
    choice = show_menu()

    if   choice == "1": addition()
    elif choice == "2": subtraction()
    elif choice == "3": multiplication()
    elif choice == "4": transpose()
    elif choice == "5": determinant()
    elif choice == "6": inverse()
    elif choice == "7":
        print("\n  Bye bye! Thanks for using Matrix Tool :)")
        break
    else:
        print("\n  !! Invalid choice. Please enter 1 to 7.")

    input("\n  Press Enter to go back to menu...")
