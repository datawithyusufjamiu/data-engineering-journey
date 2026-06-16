def describe_customer(name, balance):
    return f"{name} has a balance of {balance:,} naira"

customers = [
{"name": "Yusuf", "balance":250_000},
{"name": "Amina", "balance":180_000},
{"name": "Chidi", "balance":420_000},
]

for customer in customers:
    message = describe_customer(customer["name"], customer["balance"])
    print(message)

def describe_customer(name, balance, branch="Lagos"):
    return f"{name} — {balance:,} naira — Branch: {branch}"