import cvxpy as cv

# feeding mix

# Cattle, sheep=, chicken

# corn, limestone, soybean, fishmeal

# Feed demand: kg

demand = {"cattle": 10000,
          "sheep": 6000,
          "chicken": 8000}

supply = {"corn": 6000,
          "limestone": 10000,
          "soybean": 4000,
          "fishmeal": 5000}

costs = {"corn": 20,
          "limestone": 12,
          "soybean": 24,
          "fishmeal": 12}

nutrition = {"vitamin": [6, ],
             "protein": [6,],
             "calcium": [7,],
             "crude fat": [4,8]}

ing_nuts = {"corn": [8,10,6,8],
            "limestone": [6,5,20,6],
            "soybean": [10, 12, 6, 6],
            "fishmeal": [4,18,6,9]}