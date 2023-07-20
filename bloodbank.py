import sqlite3

# Database connection
conn = sqlite3.connect('bloodbank.db')
cursor = conn.cursor()

# Add a new donor to the database
def add_donor():
    name = input("Enter donor name: ")
    blood_group = input("Enter donor blood group: ")
    cursor.execute("INSERT INTO Donors (name, blood_group) VALUES (?, ?)", (name, blood_group))
    conn.commit()
    print("New donor added successfully.")

# Add a new hospital to the database
def add_hospital():
    name = input("Enter hospital name: ")
    location = input("Enter hospital location: ")
    cursor.execute("INSERT INTO Hospitals (name, location) VALUES (?, ?)", (name, location))
    conn.commit()
    print("New hospital added successfully.")

# Record blood donation
def record_donation():
    try:
        donor_id = int(input("Enter donor ID: "))
        blood_group = input("Enter blood group: ")
        donation_date = input("Enter donation date (YYYY-MM-DD): ")

        # Check if the donor ID exists in the database
        cursor.execute("SELECT * FROM Donors WHERE donor_id = ?", (donor_id,))
        donor = cursor.fetchone()
        if donor is None:
            print("Invalid donor ID. Please enter a valid donor ID.")
            return

        cursor.execute("INSERT INTO BloodDonations (donor_id, blood_group, donation_date) VALUES (?, ?, ?)",
                       (donor_id, blood_group, donation_date))
        conn.commit()
        print("Blood donation recorded successfully.")
    except ValueError:
        print("Invalid input. Please enter numeric donor ID.")

# Record blood request
def record_request():
    try:
        hospital_id = int(input("Enter hospital ID: "))
        blood_group = input("Enter blood group: ")
        request_date = input("Enter request date (YYYY-MM-DD): ")

        # Check if the hospital ID exists in the database
        cursor.execute("SELECT * FROM Hospitals WHERE hospital_id = ?", (hospital_id,))
        hospital = cursor.fetchone()
        if hospital is None:
            print("Invalid hospital ID. Please enter a valid hospital ID.")
            return

        cursor.execute("INSERT INTO BloodRequests (hospital_id, blood_group, request_date) VALUES (?, ?, ?)",
                       (hospital_id, blood_group, request_date))
        conn.commit()
        print("Blood request recorded successfully.")
    except ValueError:
        print("Invalid input. Please enter numeric hospital ID.")

# Check blood availability for a specific blood group
def check_blood_availability():
    blood_group = input("Enter blood group: ")
    cursor.execute("SELECT COUNT(*) FROM BloodDonations WHERE blood_group = ?", (blood_group,))
    result = cursor.fetchone()
    print("Available blood units for", blood_group, ":", result[0])

# Close the database connection
def close_connection():
    cursor.close()
    conn.close()

# Example usage
add_donor()
add_hospital()
record_donation()
record_request()
check_blood_availability()
close_connection()
