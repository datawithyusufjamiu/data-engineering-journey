#day 1 - variables & data types
# My first data engineering script

#strings text data
city_name ="Lagos"
country = "Nigeria"
region = "South West"

#Integers - whole numbers
population = 15_000_000
year_founded = 1472

#Floats - decimal numbers
area_km2 = 1171.28

#Booleans - True or False only
is_coastal = True
is_capital = False

#Print everything using f-strings
print(f"City: {city_name}")
print(f"Country: {country}")
print(f"Population: {population:,}")
print(f"Area: {area_km2}")
print(f"Coastal city: {is_coastal}")
print(f"Capital city: {is_capital}")
print(f"---")
print(f"{city_name} is a city in {country} with {population:,} people")

city2_name = "Kano"
city2_population = 4_100_000
city2_area = 810.0
city2_is_coastal = False
city2_is_capital = True

print(f"{city2_name} is a city in {country} with {city2_population:,} people")

city3_name = "Port Harcourt"
city3_population = 2_500_000
city3_area = 1000.0
city3_is_coastal = True
city3_is_capital = False

print(f"{city3_name} is a city in {country} with {city3_population:,} people")

city4_name = "Abuja"
city4_population = 3_600_000
city4_area = 2000.0
city4_is_coastal = False
city4_is_capital = True

print(f"{city4_name} is a city in {country} with {city4_population:,} people")
