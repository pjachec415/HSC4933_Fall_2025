#%%
# Assign temperature variable "temp_in" and get user input
temp_in = float(input("Please enter the temperature you want to convert: "))
#%%
# Define Function "Celsius to Fahrenheit" to convert from Celsius to Fahrenheit
def celsius_to_fahrenheit(in_c):
    out_f = ((in_c * 9 / 5) + 32)
    out_f = float(out_f)
    return out_f
#%%
# Define Function "Fahrenheit to Celsius" to convert from Fahrenheit to Celsius
def fahrenheit_to_celsius(in_f):
    out_c = ((in_f - 32) * 5 / 9)
    out_c = float(out_c)
    return out_c
#%%
# Get user input for direction
Dir = input ("Enter C to convert from Celsius to Fahrenheit or F to convert from Celsius to Fahrenheit: ")
# Clean variable to make it all lowercase
Dir_clean = Dir.lower()
#%%
# Decide which direction to go based on input
if Dir_clean == "c":
    out_temp = celsius_to_fahrenheit(temp_in)
elif Dir_clean == "f":
    out_temp = fahrenheit_to_celsius(temp_in)
else:
    out_temp = "Error"
    print ("Please Enter 'C/c' or 'F/f'.")
#%%
if Dir_clean == "c":
    conv_dir = "Celsius to Fahrenheit"
    temp_scale = "Fahrenheit"
elif Dir_clean == "f":
    conv_dir = "Fahrenheit to Celsius"
    temp_scale = "Celsius"
else:
    conv_dir = "Error"
    temp_scale = "Error"
#%%
print (f"Converting the temperature {temp_in} from {conv_dir} gives a temperature of {out_temp} degrees {temp_scale}.")
