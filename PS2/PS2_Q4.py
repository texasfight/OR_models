import pulp
import pandas as pd

s1 = pulp.LpVariable("Shaft 1", 0)
s2 = pulp.LpVariable("Shaft 2", 0)
s3 = pulp.LpVariable("Shaft 3", 0, 20)

prob = pulp.LpProblem("Maximize Shaft Profits", pulp.LpMaximize)

# Objective function
prob += 50 * s1 + 20 * s2 + 25 * s3, "objective"

# Constraints
prob += 9 * s1 + 3 * s2 + 5 * s3 <= 500, "milling"
prob += 5 * s1 + 4 * s2 <= 350, "lathe"
prob += 3 * s1 + 2 * s3 <= 150, "grinder"

prob.solve()


print("Model Status: {}".format(pulp.LpStatus[prob.status]))
for v in prob.variables():
    print(v.name, "=", v.varValue, "\tReduced Cost =", v.dj)
print(f"Objective = ${pulp.value(prob.objective):.2f}")
o = [{'name': name, 'shadow price':c.pi, 'slack': c.slack}
     for name, c in prob.constraints.items()]
print(pd.DataFrame(o))
