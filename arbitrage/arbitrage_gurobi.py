import gurobipy as gp
from gurobipy import GRB
import numpy as np
import pandas as pd

# Create a new LP model
m = gp.Model("lp")
m.Params.LogToConsole = 0 # do not print process

# Read data
rates = pd.read_csv('rates.csv')
n = len(list(rates.columns))-1
names = list(rates.columns)[1:(n+1)]
mat = np.array(rates.iloc[0:n,1:(n+1)])

# Create variables 
X = m.addVars(n, n, vtype='C',lb=0)

# Set objective
m.setObjective(0)

# Add constraints
for i in range(n):  
    flow_out = sum(X[i,j] for j in range(n))
    flow_in = sum(0.99*mat[j,i]*X[j,i] for j in range(n))
    
    if i==0:
        m.addConstr(flow_out-flow_in==-1)
    else:
        m.addConstr(flow_out-flow_in==0)
    
# Optimize model
m.optimize()

# Print optimal production level
if m.status == GRB.OPTIMAL:
    print("Congratulations! This arbitrage model makes $$$")
    for i in range(n):
        for j in range(n):
            if X[i,j].x>0:
                print(names[i]+' -> '+names[j]+': '+str(round(X[i,j].x,2)))
else:
    print("Sorry, this arbitrage model does not make $$ :(")        






