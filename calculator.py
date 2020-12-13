car = input("Name of the car: ")
value = float(input("Price of the car: "))
deposit = value * 0.1
end_value = value - (value * 0.7)
difference = value - deposit - end_value
monthly = difference / 60

fuel = float(input("Cost of fuel per 100km: "))
total_fuel = fuel * 1000

total_costs = difference + deposit + total_fuel

print(f"----{car.upper()}----")
print(f"First deposit: {deposit:.2f}€")
print(f"Remaining cost after 5 years: {end_value:.2f}€")
print(f"Monthly payment without percentage: {monthly:.2f}€")
print(f"Full cost of fuel in 5 years (100k km): {total_fuel:.2f}€")
print(f"Total cost in five years: {total_costs:.2f}€")