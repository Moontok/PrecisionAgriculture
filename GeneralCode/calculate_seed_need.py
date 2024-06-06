# This program will calculate the seed need for a given area of land

area = float(input("Enter the area of land (in square feet): "))
seeds_per_sq_ft = float(input("Enter the number of seeds per square foot: "))
percent_increase = float(input("Enter the percentage increase in seeds: "))
seed_per_pound = float(input("Enter the number of seeds per pound: "))

# Calculate the seed need
base_seeds = area * seeds_per_sq_ft
total_seeds = base_seeds * (1 + percent_increase / 100)
pounds_needed = total_seeds / seed_per_pound

# Display the results
print("The number of seeds needed is", total_seeds)
print("The number of pounds needed is", pounds_needed)

# #############################################################
# # Pounds per acre
# area = float(input("Enter the area of land (in acres): "))
# seeds_per_acre = float(input("Enter the number of seeds per acre: "))
# percent_increase = float(input("Enter the percentage increase in seeds: "))
# seed_per_pound = float(input("Enter the number of seeds per pound: "))

# # Calculate the seed need
# base_seeds = area * seeds_per_acre
# total_seeds = base_seeds * (1 + percent_increase / 100)
# pounds_needed = total_seeds / seed_per_pound

# # Display the results
# print("The number of seeds needed is", total_seeds)
# print("The number of pounds needed is", pounds_needed)
