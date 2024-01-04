import tkinter as tk
from tkinter import ttk
import mysql.connector

# Define price
hall_booking_price = {
    "1 Day": 600,
    "3 Day": 1800,
    "5 Day": 3000,
    "1 Week": 4200
}

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=""
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Function to handle the calculation and database saving
def collect_data():
    full_name = full_name_entry.get()
    email = email_entry.get()
    phone_number = int(phone_number_entry.get())
    selected_booking_day = booking_day_combobox.get()
    selected_hall_booking_price = hall_booking_price_combobox.get()

    # Calculate the total price
    total_price = hall_booking_price[selected_hall_booking_price.split(" = ")[0]] * int(selected_booking_day)

    # Inserting data into a table
    sql = "INSERT INTO user_info (full_name, email, phone_number, hall_booking_price, booking_day, total_price) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (full_name, email, phone_number, selected_hall_booking_price, selected_booking_day, total_price)
    mycursor.execute(sql, val)
    mydb.commit()

    # Display the total price in the output label
    output_label.config(text=f'Total Price: {total_price}')

# Create the main Tkinter window
root = tk.Tk()
root.title("Hall Booking System")
root.geometry('400x400')

# User info
full_name_label = tk.Label(root, text="Full Name:")
full_name_label.pack()
full_name_entry = tk.Entry(root)
full_name_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

phone_number_label = tk.Label(root, text="Phone Number:")
phone_number_label.pack()
phone_number_entry = tk.Entry(root)
phone_number_entry.pack()

# Booking info
booking_info_frame = tk.Frame(root)
booking_info_frame.pack(pady=10)

booking_day_label = tk.Label(booking_info_frame, text="Booking Day")
booking_day_combobox = ttk.Combobox(booking_info_frame, values=["1", "2", "3", "4", "5", "6", "7"])
booking_day_label.grid(row=2, column=1)
booking_day_combobox.grid(row=3, column=1)

hall_booking_price_label = tk.Label(booking_info_frame, text="Booking Price per Day")
hall_booking_price_combobox = ttk.Combobox(booking_info_frame, values=["1 Day = 600", "3 Day = 1800", "5 Day = 3000", "1 Week = 4200"])
hall_booking_price_label.grid(row=4, column=1)
hall_booking_price_combobox.grid(row=5, column=1)

# Prices List using textbox
prices_text = tk.Text(root, height=15, width=45)
prices_text.pack(pady=20)

# Save Button
save_button = tk.Button(root, text="Calculate", command=collect_data)
save_button.pack(pady=10)

# Output Label & result
label = tk.Label(root, text='Price Package', font=("Times New Roman", 12))
label.pack(ipadx=10, ipady=10)
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()