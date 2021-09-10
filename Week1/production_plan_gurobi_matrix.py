import gurobipy as gp
from gurobipy import GRB
import numpy as np

# Create a new LP model
m = gp.Model("lp")

# Create variables with bounds
x = m.addMVar(shape=3, vtype='C',
              lb=0, ub=np.array([100,40,60]), 
              name="Production")

# Set objective
c = np.array([45,60,50])
m.setObjective(c@x, GRB.MAXIMIZE)

# Add constraint(s)
A = np.matrix([[20,10,10],
               [12,28,16],
               [15,6,16],
               [10,15,0]])
b = np.array([2400,2400,2400,2400])
m.addConstr(A@x <= b, "Machines")

# Optimize model
m.optimize()

# Print optimal production level
for v in m.getVars():
    print('Decision Variable %s: %g' % (v.varName, v.x))
# Print the actual usage for each machine
for c in m.getConstrs():
    print('%s: Actual usage %g' % (c.ConstrName, c.RHS-c.Slack))
    
    
    
    
    
    
    
    
    
    

 