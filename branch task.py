branches = [
    {"name": "Lagos",  "customers": 45_000, "transactions": 120_000},
    {"name": "Abuja",  "customers": 12_000, "transactions": 34_000},
    {"name": "Kano",   "customers": 8_500,  "transactions": 22_000},
]

for branch in branches:
    print(branch["name"])
    print(branch["customers"])
    print(branch["transactions"])

for branch in branches:
    print(f"{branch['name']} — {branch['customers']:,} customers — {branch['transactions']:,} transactions")