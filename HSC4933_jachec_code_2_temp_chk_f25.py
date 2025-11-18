########################################################
# A code to accept a temperature reading, convert to   #
# Celsius if necessary, and then return a summary      #
########################################################
# H. Jachec ##### HSC4933 ##### Sec. 002 ##### 9/15/25 #
########################################################
# V 1.0.0 ##############################################
########################################################

#Zero variables
temp_c = 0

while True:
    #Define Conversion Function and Temperature Range Function
    def f_to_c(temp_f):
        conv_f = (temp_f - 32) * 5 / 9
        return conv_f

    #Get User Inputs for temperature scale
    c_or_f = input("Do you have the temperature in C or F? (c/f)")

    def temp_input():
        while True:  # loop until we break
            temp = input("Enter the temperature as a whole number or a  decimal number: ")
            try:
                #
                temp_flt = float(temp)
                return temp_flt
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    #If Statement for Calculating Temperature in Celsius and rejecting non-numeric values
    if c_or_f == "f":
        temp_c = f_to_c(temp_input())
        print(f"The temperature in C is: {temp_c:.2f}")
    elif c_or_f == "c":
        temp_c = temp_input()
        print(f"The temperature in C is: {temp_c:.2f}")

    # if/else function for sorting temperature into categories
    if temp_c < 36.1:
        print("This temperature is hypothermic.")
    elif 36.1 <= temp_c <= 37.5:
        print("This temperature is normal.")
    elif temp_c >= 37.5:
        print("This temperature is feverish.")
    else:
        print("There has been a fatal error, please check your input and run the program again.")

    # Present user with keep going/quit
    choice = input("Do you want to quit? (y/n): ").strip().lower()
    if choice == "y":
        print("Goodbye!")
        break # End program
