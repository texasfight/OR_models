import gurobipy as gp
from gurobipy import GRB


# Create a new LP model
m = gp.Model("lp")

# Create variables
x1 = m.addVar(vtype='C', lb=0, name="x1")
x2 = m.addVar(vtype='C', lb=0, name="x2")

# Set objective
m.setObjective(6*x1 + 4*x2, GRB.MAXIMIZE)

# Add constraint(s)
m.addConstr(x1 + x2 <= 6, "(1)")
m.addConstr(2*x1 + x2 <= 9, "(2)")
m.addConstr(2*x1 + 3*x2 <= 16, "(3)")

# Optimize model
m.optimize()

print('###################################')
print('############# RESULTS #############')
print('###################################')
for v in m.getVars():
    print('Decision Variable %s: %g' % (v.varName, v.x))
print('Objective Value: %g' % m.objVal)

print('##############################################')
print('############# SENSITIVITY REPORT #############')
print('##############################################')
for v in m.getVars():
    print('Decision Variable %s: Obj Coeff Range: (%g, %g), Reduced Cost: %g' % (v.varName, v.SAObjLow, v.SAObjUp, v.RC))
    
for c in m.getConstrs():
    print('Constraint %s: Slack %g, Shadow Price %g, RHS range (%g, %g)' % (c.ConstrName, c.Slack, c.Pi, c.SARHSLow, c.SARHSUp))

    

