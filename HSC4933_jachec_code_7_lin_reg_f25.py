# Simple Linear Regression using Control Flow
# Harrison Jachec
# 10/26/25

# -------------------------------
# Given Data
# -------------------------------
data_points = [
    (2000, 72.5), (2001, 73.1), (2002, 73.8), (2003, 74.2), (2004, 74.7),
    (2005, 75.3), (2006, 75.9), (2007, 76.5), (2008, 76.9), (2009, 77.4),
    (2010, 78.0), (2011, 78.5), (2012, 79.0), (2013, 79.5), (2014, 80.0),
    (2015, 80.5), (2016, 81.0), (2017, 81.5), (2018, 82.0), (2019, 82.5)
]

# -------------------------------
# Function 1 - Calculate Mean
# -------------------------------
def calculate_mean(data):
    total = 0
    count = 0
    for value in data:
        total += value
        count += 1
    mean = total / count
    return mean

# -------------------------------
# Function 2 - Calculate Regression Coefficients
# -------------------------------
def calculate_regression_coefficients(data_points):
    # Separate x and y values
    x_values = [x for x, y in data_points]
    y_values = [y for x, y in data_points]

    # Calculate means
    x_mean = calculate_mean(x_values)
    y_mean = calculate_mean(y_values)

    # Calculate numerator and denominator for slope (m)
    numerator = 0
    denominator = 0
    for i in range(len(data_points)):
        x = x_values[i]
        y = y_values[i]
        numerator += (x - x_mean) * (y - y_mean)
        denominator += (x - x_mean) ** 2
    slope = numerator / denominator
    intercept = y_mean - (slope * x_mean)
    return slope, intercept

# -------------------------------
# Function 3 - Make Predictions
# -------------------------------
def make_predictions(x_value, slope, intercept):
    predicted_y = slope * x_value + intercept
    return predicted_y

# -------------------------------
# Main Program
# -------------------------------
def main():
    # Step 1: Calculate regression coefficients
    slope, intercept = calculate_regression_coefficients(data_points)

    # Step 2: Display results
    print("Regression Coefficients:")
    print(f"Slope (m): {slope}")
    print(f"Intercept (b): {intercept}\n")

    # Step 3: Ask user for a new x value
    try:
        new_x = float(input("Enter a new x value (e.g., a year) for prediction: "))
        # Step 4: Predict y
        predicted_y = make_predictions(new_x, slope, intercept)

        # Step 5: Display predicted value
        print(f"\nPredicted y value (Life Expectancy): {predicted_y:.2f}")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Run the program
if __name__ == "__main__":
    main()