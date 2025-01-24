patients = []

def register_patient():
    """Register a new patient."""
    print("\n--- Register a New Patient ---")
    name = input("Enter patient name: ").strip()
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender (Male/Female/Other): ").strip()
    contact = input("Enter patient contact number: ").strip()
    address = input("Enter patient address: ").strip()
    hospital = input("Enter hospital name: ").strip()
    vaccine_name = input("Enter vaccine name: ").strip()
    doses_completed = int(input("Enter how many doses have been completed (0/1/2): "))
    vaccine_time = input("Enter the vaccine time (e.g., 10:00 AM, 2:30 PM): ").strip()
    
    
    patient = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Contact": contact,
        "Address": address,
        "Hospital": hospital,
        "Vaccine": vaccine_name,
        "Doses Completed": doses_completed,
        "Vaccine Time": vaccine_time
    }
    patients.append(patient)
    print("\nPatient registered successfully!\n")

def show_all_patients():
    """Display all registered patients."""
    if not patients:
        print("\nNo patients have been registered yet.\n")
        return
    
    print("\n--- All Registered Patients ---")
    for i, patient in enumerate(patients, start=1):
        print(f"Patient {i}:")
        for key, value in patient.items():
            print(f"  {key}: {value}")
        print("-" * 30)

def search_patient():
    """Search for a patient by name."""
    if not patients:
        print("\nNo patients have been registered yet.\n")
        return
    
    search_name = input("\nEnter the name of the patient to search: ").strip().lower()
    found = False
    print("\n--- Search Results ---")
    for patient in patients:
        if patient["Name"].lower() == search_name:
            found = True
            for key, value in patient.items():
                print(f"{key}: {value}")
            print("-" * 30)
    
    if not found:
        print(f"No patient found with the name '{search_name}'.\n")

def main_menu():
    """Main menu for the vaccine registration system."""
    while True:
        print("\n--- Vaccine Registration System ---")
        print("1. Register a New Patient")
        print("2. Show All Registered Patients")
        print("3. Search for a Patient")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            register_patient()
        elif choice == "2":
            show_all_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            print("Exiting the program. Stay safe!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main_menu()
