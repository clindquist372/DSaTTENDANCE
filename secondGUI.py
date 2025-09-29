import tkinter as tk

# --- 1. Define the function to update the greeting ---
def show_greeting(language):
    greetings = {
        "espanol": "Hola",
        "francais": "Bonjour",
        "deutsch": "Hallo",
        "english": "Hello"
    }
    
    # Get the appropriate greeting
    greeting_text = greetings.get(language, "Hello (Language not found)")
    
    # Update the text of the main output label
    output_label.config(text=f"{greeting_text}!")
    
    # Clear the welcome message once a button is pressed
    welcome_label.config(text="") 


# --- 2. Setup the main window ---
root = tk.Tk()
root.title("Hello in Different Languages")
root.geometry("350x300") # Made the window a bit taller to fit the vertical layout

# --- 3. Create Widgets and Apply New Layout ---

# Welcome Label (Stays at the very top)
welcome_label = tk.Label(root, 
                          text="Welcome. Select any language to see the greeting.", 
                          font=("Arial", 10), 
                          fg="black")
welcome_label.pack(pady=10) 

# --- Vertical Button Layout ---

# We no longer need the 'button_frame' or 'side=tk.LEFT' because we want
# the buttons to stack vertically by default. We just pack them one after the other.

# Spanish Button
espanol_button = tk.Button(root, 
                           text="Español", 
                           command=lambda: show_greeting("espanol"),
                           width=10) # Added a fixed width for uniformity
espanol_button.pack(pady=2) 

# French Button
francais_button = tk.Button(root, 
                            text="Français", 
                            command=lambda: show_greeting("francais"),
                            width=10)
francais_button.pack(pady=2)

# German Button
deutsch_button = tk.Button(root, 
                           text="Deutsch", 
                           command=lambda: show_greeting("deutsch"),
                           width=10)
deutsch_button.pack(pady=2)

# English Button
english_button = tk.Button(root, 
                           text="English", 
                           command=lambda: show_greeting("english"),
                           width=10)
english_button.pack(pady=2)

# Label to display the actual greeting (now packed LAST, so it appears at the bottom)
output_label = tk.Label(root, text=" ", font=("Arial", 18, "bold"))
output_label.pack(pady=20)


# --- 4. Run the main loop ---
root.mainloop()