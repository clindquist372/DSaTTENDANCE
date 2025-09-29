import tkinter as tk
from tkinter import ttk 

# --- 1. Setup the main window ---
root = tk.Tk()
root.title("tk") 
root.geometry("500x550") 
root.resizable(False, False) 

# --- 2. Create the main components ---

# Title Label (at the very top)
title_label = tk.Label(
    root, 
    text="Please provide feedback on your experience",
    font=("Arial", 16, "bold"), 
    pady=15 
)
title_label.pack()

# --- 3. Create a Frame for the Form to use the grid layout ---
form_frame = ttk.Frame(root, padding="10 10 10 10")
form_frame.pack(fill='both', expand=True) 

# Configure the grid columns
form_frame.columnconfigure(1, weight=1)

# --- WIDGETS ---

# 1. Name Input
name_label = ttk.Label(form_frame, text="Name:", font=("Arial", 10))
name_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5) 

name_entry = ttk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5) 

# 2. Email Input
email_label = ttk.Label(form_frame, text="Email:", font=("Arial", 10))
email_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

email_entry = ttk.Entry(form_frame, width=30)
email_entry.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)

# 3. Feedback (Multi-line)
feedback_label = ttk.Label(form_frame, text="Feedback:", font=("Arial", 10))
feedback_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=10, columnspan=2)

feedback_text = tk.Text(form_frame, height=10, width=45, wrap=tk.WORD) 
feedback_text.grid(row=3, column=0, sticky=tk.NSEW, padx=5, pady=5, columnspan=2) 

# ⭐️ 4. The Submit Button (placed OUTSIDE the form_frame) ⭐️

# Define a placeholder function for the button's action
def submit_data():
    """Retrieves and prints the data from the form."""
    name = name_entry.get()
    email = email_entry.get()
    # For the Text widget, we must specify the start and end of the text
    feedback = feedback_text.get("1.0", tk.END).strip() 
    
    print("\n--- Form Submission ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Feedback: \n{feedback}")
    print("-----------------------\n")
    
    # Optional: Clear the fields after submission (for a real application)
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    feedback_text.delete("1.0", tk.END)


# Create the button and link it to the submit_data function
submit_button = ttk.Button(
    root, 
    text="Submit Feedback", 
    command=submit_data, # Calls the function when clicked
    width=20
)
# We use pack() outside the grid frame to place it simply at the bottom
submit_button.pack(pady=20)


# --- 5. Run the main loop ---
root.mainloop()
