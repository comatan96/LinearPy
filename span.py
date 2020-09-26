import enum
import numpy as np
import re

from numpy.linalg.linalg import matrix_rank
import gaussianElimination as ge


class Span:
    def __init__(self, solution_vector: np.ndarray):
        self.free_vars = sorted(set(re.findall(r'x\d', ' '.join(solution_vector))))
        self.span = [[] for var in self.free_vars]
        for idx, var in enumerate(self.free_vars):
            for coordinate in solution_vector:
                if var in coordinate:
                    if var == coordinate:
                        coefficient = 1
                    else:
                        coefficient = float(re.match(rf'.?\d.[^{var}]', coordinate).group(0))
                else:
                    coefficient = 0
                self.span[idx].append(coefficient)
        self.__matrix = np.array(self.span)

    @property
    def matrix(self) -> np.array:
        return self.__matrix

    def is_basis(self) -> bool:
        return np.linalg.matrix_rank(self.matrix) == len(self.matrix)

    def __repr__(self) -> str:
        return f'span{set(tuple([tuple(vector) for vector in self.span]))}'

    def __str__(self) -> str:
        return self.__repr__