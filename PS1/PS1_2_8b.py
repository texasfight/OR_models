import cvxpy as cp

# Create decision variable

x1 = cp.Variable(1, integer=True)
x2 = cp.Variable(1, integer=True)
x3 = cp.Variable(1, integer=True)
x4 = cp.Variable(1, integer=True)
x5 = cp.Variable(1, integer=True)
x6 = cp.Variable(1, integer=True)

x = [x1, x2, x3, x4, x5, x6]

# Add the non-negative constraint for each variable
non_neg = [var >= 0 for var in x]

# Set the structural constraints
structs = [x1 + x5 >= 4,
           x2 + x6 >= 8,
           x3 + x1 >= 10,
           x4 + x2 >= 7,
           x5 + x3 >= 12,
           x6 + x4 >= 4
           ]

constraints = non_neg + structs

# Set the objective function
objective = cp.Minimize(sum(x))

# Create the problem
prob = cp.Problem(objective, constraints)

result = prob.solve()

print('Optimal value is ' + str(result))
[print(str(var.value)) for var in x]

