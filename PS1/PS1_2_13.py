import cvxpy as cp
import numpy as np
import pandas as pd

def value_read(var):
    print(f"{var}: {var.value:.2f}")

# Set decision variables
x_1_A = cp.Variable(name="units in period 1 at plant A", nonneg=True)
x_1_B = cp.Variable(name="units in period 1 at plant B", nonneg=True)
x_2_A = cp.Variable(name="units in period 2 at plant A", nonneg=True)
x_2_B = cp.Variable(name="units in period 2 at plant B", nonneg=True)

y_1_A_I = cp.Variable(name="delivered at I in period 1 from plant A", nonneg=True)
y_1_B_I = cp.Variable(name="delivered at I in period 1 from plant B", nonneg=True)
y_2_A_I = cp.Variable(name="delivered at I in period 2 from plant A", nonneg=True)
y_2_B_I = cp.Variable(name="delivered at I in period 2 from plant B", nonneg=True)

y_1_A_II = cp.Variable(name="delivered at II in period 1 from plant A", nonneg=True)
y_1_B_II = cp.Variable(name="delivered at II in period 1 from plant B", nonneg=True)
y_2_A_II = cp.Variable(name="delivered at II in period 2 from plant A", nonneg=True)
y_2_B_II = cp.Variable(name="delivered at II in period 2 from plant B", nonneg=True)

y_1_A_III = cp.Variable(name="delivered at III in period 1 from plant A", nonneg=True)
y_1_B_III = cp.Variable(name="delivered at III in period 1 from plant B", nonneg=True)
y_2_A_III = cp.Variable(name="delivered at III in period 2 from plant A", nonneg=True)
y_2_B_III = cp.Variable(name="delivered at III in period 2 from plant B", nonneg=True)

s_A = cp.Variable(name="stored units at A", nonneg=True)
s_B = cp.Variable(name="stored units at B", nonneg=True)

objective = cp.Maximize(15 * (y_1_A_I + y_1_B_I) +
                        18 * (y_2_A_I + y_2_B_I) +
                        20 * (y_1_A_II + y_1_B_II) +
                        17 * (y_2_A_II + y_2_B_II) +
                        14 * (y_1_A_III + y_1_B_III) +
                        21 * (y_2_A_III + y_2_B_III)
                        - ((s_A + s_B) +
                           4 * (y_1_A_I + y_2_A_I) +
                           7 * (y_1_B_I + y_2_B_I) +
                           6 * (y_1_A_II + y_2_A_II) +
                           4 * (y_1_B_II + y_2_B_II) +
                           8 * (y_1_A_III + y_2_A_III) +
                           3 * (y_1_B_III + y_2_B_III) +
                           8 * x_1_A + 7 * x_1_B +
                           10 * x_2_A + 8 * x_2_B
                           )
                        )

constraints = [x_1_A <= 175, x_1_B <= 200,
               x_2_A <= 150, x_2_B <= 170,
               (y_1_A_I + y_1_B_I) <= 100,
               (y_2_A_I + y_2_B_I) <= 150,
               (y_1_A_II + y_1_B_II) <= 200,
               (y_2_A_II + y_2_B_II) <= 300,
               (y_1_A_III + y_1_B_III) <= 150,
               (y_2_A_III + y_2_B_III) <= 150,
               s_A <= 50,
               s_B <= 50,
               x_1_A == s_A + y_1_A_III + y_1_A_II + y_1_A_I,
               x_1_B == s_B + y_1_B_III + y_1_B_II + y_1_B_I,
               s_A + x_2_A == y_2_A_III + y_2_A_II + y_2_A_I,
               s_B + x_2_B == y_2_B_III + y_2_B_II + y_2_B_I
               ]



prob = cp.Problem(objective, constraints)

result = prob.solve()

print(f"Total Profit: ${result:.2f}")

value_read(x_1_A)
value_read(x_1_B)
value_read(x_2_A)
value_read(x_2_B)
value_read(y_1_A_I)
value_read(y_1_B_I)
value_read(y_2_A_I)
value_read(y_2_B_I)
value_read(y_1_A_II)
value_read(y_1_B_II)
value_read(y_2_A_II)
value_read(y_2_B_II)
value_read(y_1_A_III)
value_read(y_1_B_III)
value_read(y_2_A_III)
value_read(y_2_B_III)
value_read(s_A)
value_read(s_B)