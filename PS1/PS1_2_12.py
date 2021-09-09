import cvxpy as cp
import numpy as np

# Set decision variables
A = cp.Variable(10)
B = cp.Variable(10)
C = cp.Variable(10)

# non-negative constraint
non_neg = [A >= 0,
           B >= 0,
           C >= 0
           ]

struct_matrix = np.matrix([[0, 1/12, 1/18],
                           [1/7, 1/5, 0],
                           [1/3, 0, 1/6],
                           [0, 1/12, 1/8],
                           [0, 1/4, 1/10],
                           [1/18, 1/22, 0],
                           [1/13, 0, 1/19],
                           [1/6, 1/17, 0],
                           [0, 1/13, 1/8],
                           [1/9, 0, 1/15]])

prod = struct_matrix @ np.matrix([A, B, C]).T

structs = [cp.sum(prod, axis=x) == 1 for x in range(10)]

limit = [cp.sum(A) <= 40, cp.sum(B) <= 40, cp.sum(C) <= 40]

constraints = limit + structs + non_neg

objective = cp.Minimize(cp.sum(A) + cp.sum(B) + cp.sum(C))

prob = cp.Problem(objective, constraints)

result = prob.solve()

print('Optimal value is ' + str(result))
print('Total hours for A: ' + str(A.value))
print('Total hours for B: ' + str(B.value))
print('Total hours for C: ' + str(C.value))
