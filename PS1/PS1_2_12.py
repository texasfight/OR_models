import cvxpy as cp
import numpy as np
import pandas as pd

# Set decision variables
A = cp.Variable(10, name="A")
B = cp.Variable(10, name="B")
C = cp.Variable(10, name="C")

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

limit = [cp.sum(A) <= 40, cp.sum(B) <= 40, cp.sum(C) <= 40]

constraints = limit + non_neg

for i in range(10):
    constraints.append(A[i] * struct_matrix[i,0] + B[i] * struct_matrix[i,1] + C[i] * struct_matrix[i,2] == 1)

objective = cp.Minimize(cp.sum(A) + cp.sum(B) + cp.sum(C))

prob = cp.Problem(objective, constraints)

result = prob.solve()


pd.set_option('display.max_columns', None)
df = pd.DataFrame([np.round(A.value), np.round(B.value), np.round(C.value)], index=["A","B","C"], columns=[f"Task {x+1}" for x in range(10)])
df["Total"] = df.sum(axis=1)
print(df)
df.to_csv("./output/2_12.csv")
print(np.round(result))