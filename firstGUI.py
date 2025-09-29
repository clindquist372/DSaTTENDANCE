import tkinter as tk

# --- 1. Define the function for the button's action ---
def submit_action():
    # 1. Get the text from the input box (Entry widget)
    # .get() retrieves the current value
    user_input = input_entry.get()

    # 2. Process the input (for this example, we just format a message)
    output_message = f"You entered: {user_input}"

    # 3. Display the output
    # The .config(text=...) method changes the text property of the Label widget
    output_label.config(text=output_message)
    
    # OPTIONAL: Clear the input box after submission
    # input_entry.delete(0, tk.END) 


# --- 2. Setup the main window ---
# Create the main window object
root = tk.Tk()
root.title("My First Tkinter GUI")
root.geometry("400x200") # Set the initial size of the window

# --- 3. Create Widgets ---

# Text Box (Entry widget for single line input)
# The text that the user will type
input_entry = tk.Entry(root, width=50)
# The .pack() method is a simple layout manager to place the widget in the window
input_entry.pack(pady=10) 

# Button
# The 'command' argument links the button click to our function
submit_button = tk.Button(root, 
                          text="Submit Text", 
                          command=submit_action)
submit_button.pack(pady=10)

# Output Area (Label widget to display output text)
# We start with an empty string
output_label = tk.Label(root, text="")
output_label.pack(pady=10)


# --- 4. Run the main loop ---
# This keeps the window open and listens for events (like button clicks)
root.mainloop()