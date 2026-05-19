# This program will calculate the seed need for a given area of land
# Calculated for Well's variety of rice

# Variety Well's Information
seeds_per_sq_ft = 30
seed_per_pound = 18016

# Area calculation
area = float(input("Enter the area of land (acres): "))
feet_per_acre = 43560
square_feet = area * feet_per_acre

# Percent Increase
method = .20
soil_type = .20
bed_prep = .10
date = .10
percent_increase = method + soil_type + bed_prep + date

# Calculate the seed need
base_seeds = square_feet * seeds_per_sq_ft
total_seeds = base_seeds * (1 + percent_increase)
pounds_needed = round(total_seeds / seed_per_pound)

# Display the results
print("The number of seeds needed is:", total_seeds)
print("The number of pounds needed is:", pounds_needed)
