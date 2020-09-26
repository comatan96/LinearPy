import numpy as np
import re


def eliminate(matrix: np.array, field: str='R', show_steps=False) -> np.ndarray:
    matrix = matrix.astype('float64')
    for column in range(len(matrix.T)):
        if np.array_equal(np.zeros(matrix[column:].shape), matrix[column:]):
                break
        pivot_row = get_pivot(matrix.T[column,column:])
        if pivot_row >= 0:
            # normalize the row to the first element to be 1
            matrix[pivot_row] *= 1/matrix[pivot_row, column]
            if show_steps:
                print(f'Chosed row {pivot_row+1} to eliminate and normalized it:\n{matrix}')
            # switch the row with the best position for it
            matrix[[pivot_row, column]] = matrix[[column, pivot_row]]
            if show_steps:
                print(f'Elimination by row number: {pivot_row+1}')
                if pivot_row != column:
                    print(f'Switch row {pivot_row} with row {column}:\n{matrix}')
            # fix the number
            pivot_row = column
            for row in range(len(matrix)):
                if row != pivot_row:
                    matrix[row] -= matrix[row, column] * matrix[pivot_row]
            if show_steps:
                print(f'Eliminate the column:\n{matrix}')
    field = field.upper()
    if field not in ['R', 'C']:
        field_mod = int(re.match(r'.?(\d+)', field).group(1))
        matrix %= field_mod
    else:
        field_mod = None
    solution = extract_solution_from_matrix(matrix, field_mod)
    return (matrix, solution)

def extract_solution_from_matrix(matrix: np.array, field_mod: int=None) -> tuple:
    if np.array_equal(matrix, np.eye(len(matrix))):
        return np.zeros(len(matrix))
    solution = np.ndarray(shape=matrix.shape[1], dtype=object)
    for row in range(len(matrix)):
        if np.array_equal(np.zeros(matrix[row].shape), matrix[row]):
            solution[row] = f'x{row+1}'
        sols = matrix[row,row+1:]
        if not np.linalg.matrix_rank(sols):
            solution[row] = f'x{row+1}'
        for sol in range(len(sols)):
            if sols[sol] != 0:
                sign = ''
                current_x = row+sol+2
                if field_mod:
                    if solution[row]:
                        sign = '+'
                    else:
                        solution[row] = ''
                    solution[row] += f'{sign}{-sols[sol]%field_mod}'
                else:
                    sign = '-' if sols[sol] > 0 else '+'
                    if solution[row]:
                        solution[row] += f'{sign}{abs(sols[sol])}'
                    else:
                        solution[row] = f'{-sols[sol]}'
                solution[row]+= f'x{current_x} '
    for free_variable in range(*matrix.shape):
        solution[free_variable] = f'x{free_variable + 1}'
    return solution

def get_pivot(column: np.array) -> int:
    if np.array_equal(np.zeros(column.shape), column):
        return -1
    pivot = 0
    for idx in range(len(column)):
        if column[idx] == 1 and column[idx-1] == 0:
            return idx
        if column[idx] != 0:
            pivot = idx
    return pivot
