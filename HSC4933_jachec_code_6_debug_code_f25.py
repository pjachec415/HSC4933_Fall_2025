# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False

    # FIX: 'number % i = 0' was an assignment, which is invalid syntax.
    # It must be '==' for comparison.
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


# Main program
print("Prime Number Finder")

# Get user input
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Swap start and end if start is greater
# (Your logic was correct here.)
if start > end:
    temp = start
    start = end
    end = temp

# Find and print prime numbers
print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")
