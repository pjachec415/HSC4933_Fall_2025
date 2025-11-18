###################################
# A program to analyze px data    #
# from two different hospitals.   #
###################################
# H. Jachec # 11/9/2025 # HSC4933 #
###################################

class Patient:
    def __init__(self, name, age, gender, blood_pressure, temperature):
        """Initialize a new patient record."""
        self.name = name
        self.age = age
        self.gender = gender
        self.blood_pressure = blood_pressure  # (systolic, diastolic)
        self.temperature = temperature        # in Celsius

    def display_patient_info(self):
        """Display the patient's information in a formatted way."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Blood Pressure: {self.blood_pressure}")
        print(f"Temperature: {self.temperature:.1f}°C")
        print()  # Blank line for readability

    def is_hypertensive(self):
        """Return True if the patient is hypertensive."""
        systolic, diastolic = self.blood_pressure
        return systolic >= 140 or diastolic >= 90

    def is_feverish(self):
        """Return True if the patient has a fever."""
        return self.temperature >= 37.5


# --- Main Program ---
def main():
    # Create two patient instances
    patient1 = Patient("John Doe", 45, "Male", (140, 85), 36.8)
    patient2 = Patient("Jane Smith", 32, "Female", (130, 88), 37.6)

    # Display patient information
    print("Patient 1 Information:\n")
    patient1.display_patient_info()

    print("Patient 2 Information:\n")
    patient2.display_patient_info()

    # Analyze health data
    print(f"Patient 1 is Hypertensive: {patient1.is_hypertensive()}")
    print(f"Patient 1 is Feverish: {patient1.is_feverish()}\n")

    print(f"Patient 2 is Hypertensive: {patient2.is_hypertensive()}")
    print(f"Patient 2 is Feverish: {patient2.is_feverish()}")


# Run the program
if __name__ == "__main__":
    main()
