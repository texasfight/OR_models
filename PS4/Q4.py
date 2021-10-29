import cvxpy as cp
import numpy as np

containers = np.array([2700, 2800, 1100, 1800, 3400])

demand = np.array([2900, 4000, 4900])
costs = np.array([10, 8, 6])

super = cp.Variable((5,), boolean=True)
regular = cp.Variable((5,), boolean=True)
unleaded = cp.Variable((5,), boolean=True)

gasses = np.array([super, regular, unleaded])


shortage = cp.Variable((3,))

constraints = list()

constraints += [sum(super), sum(regular), sum(unleaded)]
shortage_constraints = [shortage <= 500, shortage >= 0]

for i in range(3):
    shortage_constraints.append(shortage[i] >= demand[i] - sum(cp.multiply(gasses[i], containers)))

for i in range(5):
    constraints.append(super[i] + unleaded[i] + regular[i] <= 1)

constraints += shortage_constraints

objective = cp.Minimize(sum(cp.multiply(shortage, costs)))


problem = cp.Problem(objective, constraints)

result = problem.solve()
print(result)
print(super.value)
print(regular.value)
print(unleaded.value)
print(shortage.value)