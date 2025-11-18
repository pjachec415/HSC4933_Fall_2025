import math

# ---------------------------------------------------------
# Function: Calculate Sample Size for Systematic Sampling
# ---------------------------------------------------------
def calculate_sample_size(population_size, confidence_level, margin_of_error):
    # Convert confidence level (like 95) to Z-score
    if confidence_level == 90:
        Z = 1.645
    elif confidence_level == 95:
        Z = 1.96
    elif confidence_level == 99:
        Z = 2.576
    else:
        print("Unsupported confidence level. Using 95% by default.")
        Z = 1.96

    P = 0.5  # conservative estimate
    E = margin_of_error

    # Sample size formula
    sample_size = (Z**2 * P * (1 - P)) / (E**2)

    # If sample size exceeds population, cap it
    if sample_size > population_size:
        return population_size

    return round(sample_size)


# ---------------------------------------------------------
# Systematic Sampling Function
# ---------------------------------------------------------
def systematic_sampling(population, sample_size):
    interval = len(population) / sample_size
    interval = round(interval)

    sample = []
    index = 0

    for _ in range(sample_size):
        if index < len(population):
            sample.append(population[index])
            index += interval

    return sample


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------
population_size = int(input("Enter the population size: "))
confidence_level = int(input("Enter the confidence level (e.g., 95 or 99): "))
margin_of_error = float(input("Enter the desired margin of error (e.g., 0.05): "))

required_sample_size = calculate_sample_size(population_size, confidence_level, margin_of_error)

print(f"\nThe required sample size for systematic sampling is approximately {required_sample_size}.\n")

# Create a simple population list: [1, 2, 3, ..., N]
population = list(range(1, population_size + 1))

# Ask user for desired sample size
while True:
    requested = int(input("Enter the sample size you want to draw: "))

    if requested > required_sample_size:
        print("\nSorry, the requested sample size is not feasible with the given parameters.")
        print(f"The maximum sample size possible is {required_sample_size}. Please enter a lower value.\n")
    else:
        break

# Perform sampling
sample = systematic_sampling(population, requested)

print("\nThe systematic sampling selected the following elements:")
print(sample)
