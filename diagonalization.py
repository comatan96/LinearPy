import numpy as np
import gaussianElimination as ge

def is_diagonalizable(matrix: np.array) -> dict:
    """check if given matrix is diagonalizable for each of the eigenvalues

    Args:
        matrix (np.array): matrix to check diagonalization on

    Returns:
        dict: dictionary of eigenvalues as keys and diagonalization status as value
    """    
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    algebric_multiplicity = {eigenvalue: multi for eigenvalue, multi in zip(*np.unique(eigenvalues, return_counts=True))}
    print(f'Eigen values are: {list(algebric_multiplicity.keys())}')
    charateristic_polynomials = {eigenvalue: eigenvalue*np.eye(len(matrix)) - matrix for eigenvalue in algebric_multiplicity.keys()}
    return {eigenvalue: np.linalg.matrix_rank(matrix) == 0 for eigenvalue, matrix in charateristic_polynomials.items()}