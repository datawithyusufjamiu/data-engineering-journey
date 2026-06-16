def describe_customer(name, balance, branch="Lagos"):
    return f"{name} — {balance:,} naira — Branch: {branch}"

print(describe_customer("Amina",180_000))
print(describe_customer("Yusuf",250_000, "Abuja"))
print(describe_customer("Chidi",420_000, "Kano"))