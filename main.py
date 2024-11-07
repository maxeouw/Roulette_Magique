import random
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk  # For handling images
import os

# Configuration
image_folder = "img"  # Folder where images are stored
options = ["cara", "cara_rouge", "vin_rouge", "genepi", "speciale"]  # Options for roulette
scrolling_speed = 500  # Speed of scrolling in milliseconds (lower is faster)
countdown_duration = 5  # Countdown duration in seconds
image_width = 1920  # Full-screen width
image_height = 1080  # Full-screen height

# Global variable to track countdown steps
countdown_remaining = countdown_duration * 1000 // scrolling_speed  # Convert to "steps" based on scrolling speed

# Create the main function to start the roulette scrolling
def lancer_roulette():
    global countdown_remaining
    countdown_remaining = countdown_duration * 1000 // scrolling_speed  # Reset countdown steps
    scroll_images()  # Start the scrolling animation

def scroll_images():
    global countdown_remaining
    if countdown_remaining > 0:
        # Select a random image to display during scrolling
        selection = random.choice(options)
        image_path = os.path.join(image_folder, f"{selection}.png")

        try:
            # Load and resize the image to full screen
            image = Image.open(image_path)
            image = image.resize((image_width, image_height))  # Resize image to full-screen size
            photo_image = ImageTk.PhotoImage(image)

            # Display the resized image
            canvas.create_image(0, 0, image=photo_image, anchor="nw")
            canvas.image = photo_image  # Keep reference to avoid garbage collection

        except Exception as e:
            print(f"Error loading image {image_path}: {e}")

        # Update the countdown label
        countdown_label.config(text=f"Countdown: {countdown_remaining * scrolling_speed // 1000} sec")
        
        # Decrement countdown and schedule next scroll
        countdown_remaining -= 1
        root.after(scrolling_speed, scroll_images)
    else:
        # Time's up, select the final image
        select_final_image()

def select_final_image():
    # Pick the final image and update the interface
    selection = random.choice(options)
    image_path = os.path.join(image_folder, f"{selection}.png")
    
    try:
        # Load and resize the final image to full screen
        image = Image.open(image_path)
        image = image.resize((image_width, image_height))  # Resize image to full-screen size
        photo_image = ImageTk.PhotoImage(image)

        # Display the resized final image
        canvas.create_image(0, 0, image=photo_image, anchor="nw")
        canvas.image = photo_image  # Keep reference to avoid garbage collection

        result_label.config(text=f"La roulette a sélectionné : {selection}")
        countdown_label.config(text="Countdown: 0 sec")
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")

# Setup the GUI
root = tk.Tk()
root.title("Roulette de sélection")

# Make the window full screen
root.attributes("-fullscreen", True)

# Create a Canvas to hold the image and overlay text
canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

# Static overlay: Label for countdown display
countdown_label = Label(root, text="Countdown: 0 sec", font=('Helvetica', 36), bg='black', fg='white')
countdown_label.pack(side=tk.TOP, pady=20)

# Static overlay: Label for displaying the selected result
result_label = Label(root, text="Cliquez pour lancer la roulette", font=('Helvetica', 36), bg='black', fg='white')
result_label.pack(side=tk.BOTTOM, pady=20)

# Static overlay: Button to launch the roulette
button = tk.Button(root, text="Lancer la roulette", font=('Helvetica', 24), command=lancer_roulette)
button.pack(side=tk.BOTTOM, pady=50)

# Start the GUI loop
root.mainloop()
