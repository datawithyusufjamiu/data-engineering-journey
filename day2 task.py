# Day 2 Task — Nigerian Bank Branch Data

branches = ["Lagos", "Abuja", "Kano", "PH", "Ibadan"]
customers = [45_000, 12_000, 8_500, 19_000, 6_200]

print(branches)
print(customers)




total = 0
for tot in customers:
    total = total + tot

print(f"Total customers: {total:,}")

print("---")

for index, branch in enumerate(branches):
    print(f"{index + 1}. {branch} - {customers[index]:,} customers")


print("---")

print(f"average customers per branch:{sum(customers) // len(branches):,}")

