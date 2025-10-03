from PIL import Image
from tkinter import messagebox

class ImageViewer:
    #  add an image from a given file path.
    
    def show(image_path):
        """ To display the image file."""
        try:
            # Try to open the image from the given path
            image = Image.open(image_path)
            
            # Display the image using the image viewer
            image.show()
        
        except FileNotFoundError:
            # If the file path is not found or file does not exist,
            # show an error message box
            messagebox.showerror("File not found:", f"{image_path}")
        
        except Exception as e:
            # For any other unexpected error 
            # display the error message
            messagebox.showerror("An error occurred:", f"{e}")
