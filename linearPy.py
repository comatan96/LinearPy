import numpy as np
from  gaussianElimination import *
# import diagonalization as di
from span import Span

matrix = np.array([[1, -1, 3], [2, 6, -2], [4, 4, 4]])
m = np.array([[1,0,0,1], [0,1,4,0]])
x, sol = eliminate(matrix, field='Z5')
s = Span(sol)
# di.is_diagonalizable(x)
eliminate(np.array([[0,1,0],[0,-2,0],[1,1,1]]))