# LinearPy

## Educational Linear Algebra python library
### WIP:
*   Gaussian Elimination (including finite fields like Z5 etc.)
*   Solutions for Linear equations
*   Spans and basis from solutions (including Kernel basis for Transformations)
*   Diagonalization checker for matrices

## Usage
```git
git clone https://github.com/comatan96/LinearPy
cd LinearPy
python -i linearpy.py
```
every matrix is represented as a numpy array.

## Gaussian Elimination
```python
import numpy as np
import linearpy as lp
matrix = np.array([[1, 0, 4], [0, 2, 3], [0, 0 5]])
# eliminate:
eliminated = lp.eliminate(matrix)
```
