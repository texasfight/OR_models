import cvxpy as cp

x = cp.Variable(10, integer=True)

female = sum(x[:5])
male = sum(x[5:])
students = x[1] + x[0] + x[2] + x[9]
admin = x[4] + x[5]
faculty = x[3] + x[6] + x[7] + x[8]

constraints = [female >= 1, male >= 1, students >= 1, admin >= 1, faculty >= 1]

objective = cp.Minimize(sum(x))

prob = cp.Problem(objective, constraints)

result = prob.solve()

print(result)
print(x.value)