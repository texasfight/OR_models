# import package
import cvxpy as cp
import numpy as np
import pandas as pd
import math

# read data
rates = pd.read_csv('rates.csv')
n = len(list(rates.columns))-1
names = list(rates.columns)[1:(n+1)]
mat = np.array(rates.iloc[0:n,1:(n+1)])

# decision variables
X = cp.Variable((n,n))

# objective
objective = cp.Minimize(sum(sum(X)))

# constraint
constraints = [X >= 0]

for i in range(n):  
    flow_out = sum(X[i,:])
    flow_in = sum(0.99*mat[j,i]*X[j,i] for j in range(n))
    if i==0:
        constraints += [flow_out-flow_in==-1]
    else:
        constraints += [flow_out-flow_in==0]
    
# solve the problem
prob = cp.Problem(objective, constraints)
result = prob.solve()

# print results
if result != math.inf:
    print("Congratulations! This arbitrage model makes $$$")
    for i in range(n):
        for j in range(n):
            if X[i,j].value > 0.01: # numerical issues
                print(names[i]+' -> '+names[j]+': '+str(round(X[i,j].value,2)))
else:
    print("Sorry, this arbitrage model does not make $$ :(")        
        

