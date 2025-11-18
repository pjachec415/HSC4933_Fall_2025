# Generic Epidemiological Metrics Calculator

def calculate_prevalence(total_cases, population):
    return (total_cases / population) * 100000

def calculate_incidence(new_cases, population):
    return (new_cases / population) * 100000

def calculate_mortality(deaths, population):
    return (deaths / population) * 100000

def calculate_ypll(death_ages, life_expectancy):
    return sum([life_expectancy - age for age in death_ages if age < life_expectancy])

# --- Get User Inputs ---
print("Enter data for the disease:")

# Prevalence input
total_cases = int(input("Total existing cases: "))
population = float(input("Total population: "))
prevalence = calculate_prevalence(total_cases, population)

# Incidence input
new_cases = int(input("Number of new cases: "))
incidence = calculate_incidence(new_cases, population)

# Mortality input
deaths = int(input("Number of deaths: "))
mortality = calculate_mortality(deaths, population)

# YPLL input (optional)
has_ypll = input("Do you want to calculate Years of Potential Life Lost (YPLL)? (yes/no): ").strip().lower()
ypll = None

if has_ypll == "yes":
    death_ages_input = input("Enter the ages of deceased individuals (comma-separated): ")
    death_ages = [int(age.strip()) for age in death_ages_input.split(",")]
    life_expectancy = int(input("Average life expectancy: "))
    ypll = calculate_ypll(death_ages, life_expectancy)

# --- Print Summary ---
print("\n--- Epidemiological Metrics Summary ---")
print(f"Prevalence: {prevalence:.2f} per 100,000")
print(f"Incidence: {incidence:.2f} per 100,000")
print(f"Mortality Rate: {mortality:.2f} per 100,000")
if ypll is not None:
    print(f"Years of Potential Life Lost (YPLL): {ypll}")
