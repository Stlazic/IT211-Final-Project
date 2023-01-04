debt = 29.62
placehold = 0
year = 2022
interest = .095
saves = {}

while year <= 2036:
    placehold = debt * interest
    debt = debt + placehold
    debt_float = "{:.2f}".format(debt)
    saves[year] = debt_float
    year += 1


for key, value in saves.items():
    print(key, ': $', value, ' Trillion')
