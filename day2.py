#A list holds multiple items in one variable
# Square brackets. Items seperated by commas.

cities = ["Lagos", "Kano", "Port Harcourt", "Abuja", "Ibadan"]

#Access items by position - index starts at 0
print(cities[0])    #Lagos
print(cities[1])    #Kano
print(cities[-1])   #Ibadan - negative index goes from the end

#How many items in the list?
print(len(cities)) #5

#Add a new city
cities.append("Enugu")
print(len(cities)) #6 now

#Remove a city
cities.remove("Kano")


cities = ["Lagos", "Kano", "Port Harcourt", "Abuja", "Ibadan"]

# A for loop processes every item automatically

for city in cities:
    print(f"Processing: {city}")

print("---") 

#Loop with position number using enumerate
for index, city in enumerate(cities):
    print(f"{index+1}. {city}")

#A list of numbers - population data
populations = [15_000_000, 4_100_000, 2_500_000, 3_600_000, 3_500_000]

#Find the total
total=0
for pop in populations:
    total = total + pop

print(f"Total population: {total:,}")

print("---") 

#Find the largest
largest = 0
for pop in populations:
    if pop > largest:
        largest= pop

print(f"Largest city population: {largest:,}")

print("---") 

#python has built in funcyions for these

print(f"sum: {sum(populations):,}")
print(f"max: {max(populations):,}")
print(f"min: {min(populations):,}")