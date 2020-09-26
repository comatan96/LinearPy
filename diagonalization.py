import numpy as np
import gaussianElimination as ge

def is_diagonalizable(matrix: np.array) -> bool:
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    algebric_multiplicity = {eigenvalue: multi for eigenvalue, multi in zip(*np.unique(eigenvalues, return_counts=True))}
    print(f'Eigen values are: {list(algebric_multiplicity.keys())}')
    charateristic_polynomials = [eigenvalue*np.eye(len(matrix)) - matrix for eigenvalue in algebric_multiplicity.keys()]
    return {eigenvalue: truth_value for eigenvalue}