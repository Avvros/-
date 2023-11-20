from typing import IO


def print_matrix(matrix, file: IO):
    for row in matrix:
        for num in row:
            # print(np.format_float_positional(np.float32(num), 3, fractional=True, unique=False))
            #file.write(f"{abs(num):.6g}", end=' ')
            print(f"{abs(num):.6g}", end=' ', file=file)
        print(file=file)