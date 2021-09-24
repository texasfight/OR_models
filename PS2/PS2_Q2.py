import cvxpy as cp

cargo1 = cp.Variable(3, name="Cargo 1")
cargo2 = cp.Variable(3, name="Cargo 2")
cargo3 = cp.Variable(3, name="Cargo 3")
cargo4 = cp.Variable(3, name="Cargo 4")

totals = cp.Variable(3, name="Total Compartment cargos")

volumes = [500, 700, 600, 400]

space_cap = [7000, 9000, 5000]
weight_cap = [12, 18, 10]

weight_supply = [20, 16, 25, 13]

profits = [320, 400, 360, 290]

cargo_list = [cargo1, cargo2, cargo3, cargo4]

constraints = list()

# Add proportions
constraints.append(totals[0] * 5 - 6 * totals[2] == 0)
constraints.append(totals[0] * 3 - 2 * totals[1] == 0)
constraints.append(totals - cp.sum(cargo_list) == 0)


for j in range(3):
    # total under cap
    constraints.append(totals[j] <= weight_cap[j])
    total_volume = 0
    for i, cargo in enumerate(cargo_list):
        # Non-negative constraint
        constraints.append(cargo[j] >= 0)
        total_volume += cargo[j] * volumes[i]

    constraints.append(total_volume <= space_cap[j])

for i, cargo in enumerate(cargo_list):
    constraints.append(sum(cargo) <= weight_supply[i])

objective = cp.Maximize(sum(cargo1) * profits[0] + sum(cargo2) * profits[1] +
                        sum(cargo3) * profits[2] + sum(cargo4) * profits[3])

prob = cp.Problem(objective, constraints)

result = prob.solve()

print(result)
front = 0
mid = 0
back = 0
for cargo in cargo_list:
    print(cargo.value, sum(cargo.value))
    front += cargo.value[0]
    mid += cargo.value[1]
    back += cargo.value[2]

print(front, mid, back)