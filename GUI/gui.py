'''
Group Name: Sydney Group 17
Group Members: 4
Mohammed Ashrafujjaman Hera - 391197
Pujan Dey  - 395076
Shaown Imtiaz - 396121
Al-Amin Dhaly - 395230
'''
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from GUI.baseGuiWindows import BaseWindow

import sys
import os

# Get the parent directory (Huging_face_integration_with_python/)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
    
from AI_models.AI_models import AIModels
from utils.all_information import information
from utils.image import ImageViewer

# multiple inheritance
class guiApp(BaseWindow,AIModels):
    """Inheritance: GUI (BaseWindow)"""
    def __init__(self):
        BaseWindow.__init__(self)
        AIModels.__init__(self)
        self.run_model_flag_gen_AI = True
        
        

    # GUI LAYOUT 
    def build_gui(self):
        # This whole GUI build by Grid layout. 
        # Create the main menubar
        menubar = tk.Menu(self.root())

        # Create the "File" menu dropdown
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self._exit_app)
        menubar.add_cascade(label="File", menu=file_menu)

        # Create the "Help" menu dropdown
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="OOP Explanation", command=self._show_OOP_explanations)
        menubar.add_cascade(label="Help", menu=help_menu)

        # Attach menubar to the root window
        self.root().config(menu=menubar)
        
        # Top Frame
        # It holds two more frame, one for selecting AI model and another for showing names of AI models
        top = tk.Frame(self.root(), padx=10, pady=10)
        top.grid(row=0, column=0, sticky="ew")
        
        # Top Left SubFrame
        # This frame is for dropdown menu to select an AI model to run
        topSubFrame1 = tk.Frame(top, padx=10, pady=10)
        topSubFrame1.grid(row=0, column=0, sticky="nw")

        # Label for dropdown model
        tk.Label(topSubFrame1, text="Select Model:").grid(row=0, column=0, pady=5, sticky="w")

        # Tkinter's own variable holder library for dynamic input
        self.input_type = tk.StringVar(value="")
        # Combobox or dropdown menu box for selecting model
        
        self.input_type_cb = ttk.Combobox(topSubFrame1, textvariable=self.input_type, 
                                          values=["Generative AI Model", "Image Classifier AI Model"],
                                          state="readonly", width=50)
        self.input_type_cb.grid(row=1, column=0, padx=6, sticky="w")
        
        # Binding combobox options with a function. using lambda function will allow to pass parameters
        # Although we don't need to pass any parameter here but it is best practice and use only this time
        self.input_type_cb.bind("<<ComboboxSelected>>", lambda e: self._toggle_input())

        # Top Right SubFrame
        # this frame will show names of the AI models.
        topSubFrame2 = tk.LabelFrame(top, text="Model Names:", padx=10, pady=10)
        topSubFrame2.grid(row=0, column=1, sticky="e")
        topSubFrame2.grid_columnconfigure(0, weight=1)
        
        # This sub-frame is for Generative AI model
        modelSubFrame1 = tk.Frame(topSubFrame2, padx=10, pady=5)
        modelSubFrame1.grid(row=0, column=0, sticky="ew")
        tk.Label(modelSubFrame1, text="Model Generative AI:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.model_a = tk.StringVar(value="Generative AI") # Actual model name will go here after implementing one
        tk.Label(modelSubFrame1, text=self.model_a.get()).grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # this sub-frame is for Image Classifier AI model
        modelSubFrame2 = tk.Frame(topSubFrame2, padx=10, pady=5)
        modelSubFrame2.grid(row=1, column=0, sticky="ew")
        tk.Label(modelSubFrame2, text="Model Image Classifier:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.model_b = tk.StringVar(value="Image Classifier") # Actual model name will go here after implementing one
        tk.Label(modelSubFrame2, text=self.model_b.get()).grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Frame for input section ( Mid section for grid implementation)
        # In this part User input Will be taken.
        # One input will be for generative AI
        # another will be for image selecting from users device
        # These two input will be displayed according to selected model from the upper droudown menu
        self.mid = tk.LabelFrame(self.root(), text="Input", padx=10, pady=10)
        self.mid.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.mid.grid_rowconfigure(0, weight=1)
        self.mid.grid_columnconfigure(0, weight=1)

        # Text Box
        # Text input for Generative AI 
        self.placeholder = "Type some text here. Any question, Any info..."
         
        # Create Text widget
        self.text_box = tk.Text(self.mid, height=3, fg='gray')
        self.text_box.insert("1.0", self.placeholder)
        self.text_box.grid(row=0, column=0, sticky="nsew")
        
        # Bind focus in/out events
        self.text_box.bind("<FocusIn>", self._clear_placeholder)
        self.text_box.bind("<FocusOut>", self._add_placeholder)

        # Image path
        # It will take image path for image classification
        self.img_path = tk.StringVar()
        self._img_row = tk.Frame(self.mid)
        self._img_row.grid(row=0, column=0, sticky="ew")
        # the line below will hide image input iniitially. only visible when relative model is selected
        self._img_row.grid_remove() 

        tk.Entry(self._img_row, textvariable=self.img_path, width=80).pack(side="left", fill="x", expand=True)
        tk.Button(self._img_row, text="Browse Image...", command=self._choose_image).pack(side="left", padx=6)

        # Model running button
        # This button will run relative model
        runAIBtn = tk.Frame(self.root(), padx=10, pady=6)
        runAIBtn.grid(row=2, column=0, sticky="ew")

        tk.Button(runAIBtn, text="Run Selected Models", command=self._run_models ).grid(row=0, column=0, padx=5) # 
       
        # Output Panes
        # It will show output of the model
        # there are 2 frame. One for AI model output. Another is for AI model information.
        output_panes = tk.PanedWindow(self.root(), orient="horizontal")
        output_panes.grid(row=3, column=0, sticky="nsew", padx=10, pady=(0, 10))

        # 2 frame for AI output and AI information
        output_AI = tk.LabelFrame(output_panes, text="Model Outputs", padx=8, pady=8)
        output_info = tk.LabelFrame(output_panes, text="Model Information", padx=8, pady=8)
        output_panes.add(output_AI)
        output_panes.add(output_info)

        self.output_text = tk.Text(output_AI, height=18)
        self.output_text.pack(fill="both", expand=True)

        self.info_text = tk.Text(output_info, height=18)
        self.info_text.pack(fill="both", expand=True)
        
        # the function below will show information about model according to dropdown selected options
        self._show_model_info()
        
        # spliting windows 50% for AI output and AI information
        self.root().after(100, lambda: output_panes.sash_place(0, self.root().winfo_width() // 2, 0))        

        
        # Bottom layer
        # there is 2 button one for clear AI output info, another is for OOPConcept explanation
        bottom_layer = tk.Frame(self.root(), padx=10, pady=6)
        bottom_layer.grid(row=4, column=0, sticky="ew")
        
        # Allow column expansion so buttons can align to left/right ends
        bottom_layer.grid_columnconfigure(0, weight=0)
        bottom_layer.grid_columnconfigure(1, weight=1)
        
        # This button clear the output panel 
        tk.Button(bottom_layer, text="Clear Output", command=self._clear_output).grid(row=0, column=1, padx=5)
        tk.Button(bottom_layer, text="More about AI Model", command=self._show_model_explanations).grid(row=0, column=2, padx=5) 
        

        # Configure resizing the grid for overall GUI
        self.root().grid_rowconfigure(3, weight=1)
        self.root().grid_columnconfigure(0, weight=1)


    # this toggle input for Generative AI input text and image AI model's file input
    def _toggle_input(self):
        # If image classification model is selected then text input hide
        if self.input_type.get() == "Image Classifier AI Model":
            self.text_box.grid_remove()
            self._img_row.grid()
        else:
            # is generative AI model selected file input hide
            self._img_row.grid_remove()
            self.text_box.grid()
        # refresh model info base on selected model    
        self._show_model_info() 

    def _choose_image(self):
        # choosing an image from the pc for image classificaion
        path = filedialog.askopenfilename(title="Choose an image",
                                          filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if path:
            self.img_path.set(path)

    # clearing output panel for next output based on call
    def _clear_output(self):
        self.output_text.delete("1.0", "end")
        
    
    
    # If mouse click on the text input It will clear the placeholder text
    def _clear_placeholder(self, event):
        current_text = self.text_box.get("1.0", tk.END).strip()
        if current_text == self.placeholder:
            self.text_box.delete("1.0", tk.END)
            self.text_box.config(fg='black')

    # this is simple placeholder in the text imput field
    # if mouse click on the anywhere other then the text input field then the placeholder text will show
    def _add_placeholder(self, event):
        current_text = self.text_box.get("1.0", tk.END).strip()
        if not current_text:
            self.text_box.insert("1.0", self.placeholder)
            self.text_box.config(fg='gray')


    # this is to show model info briefly in the gui right beside the outout panel
    def _show_model_info(self):
        selected_model = self.input_type.get()
        self.info_text.delete("1.0", "end")
        # it shows info based on selected model from the toggle menu
        if selected_model == "Generative AI Model":
            info = information.show_brief_gen_ai_info()
        elif selected_model == "Image Classifier AI Model":
            info = information.show_brief_img_classifier_info()
        else:
            info = "No model selected."

        self.info_text.insert("1.0", info)
     
    # this function explain all the object orriented programming done in this project
    # it is in menu (help->oop explanation)
    # it is getting the info from another python file in utils folder(utils->all_information.py)
    def _show_OOP_explanations(self): 
        explanation = information.show_OOP_explanations()
        messagebox.showinfo("OOP Explanation", explanation)
    
    
    # this fucntion run this AI model based on the selected model
    def _run_models(self):
        # it is simple warning to say that AI model might not produce actual/correct information
        if self.run_model_flag_gen_AI == True:
            messagebox.showwarning("AI warning!","AI does not always produce information correctly.")
            self.run_model_flag_gen_AI = False
        # generative model (in case of fail run it show an error message)
        in_type = self.input_type.get().lower()
        if in_type == "Generative AI Model".lower():
            text = self.text_box.get("1.0", "end").strip()
            if text == "Type some text here. Any question, Any info...":
                messagebox.showerror("Error!","Please enter some text.")
                return
            if not text:
                messagebox.showerror("Error!","Please enter some text.")
                return
            res = self.run_generative_AI(text)
            self.output_text.insert("end", f"Generative AI Model's output:\n{res}\n\n")
        # Image AI model ( in case of fail run it show an error message)
        elif in_type == "Image Classifier AI Model".lower():
            self._clear_output()
            img_path = self.img_path.get().strip()
            if not img_path:
                messagebox.showerror("Error!","Please select an image file.")
                return
            res = self.run_image_classifier(img_path)
            self.output_text.insert("end", f"Image Model's Output:\n{res[0]['label']} : {float(res[0]['score'])*100}%\n{res[1]['label']} : {float(res[1]['score'])*100}%\n{res[2]['label']} : {float(res[2]['score'])*100}%\n")
            ImageViewer.show(img_path)
        else:
            messagebox.showerror("Error!","Please select a model.")
        
    
    # this function shows details info about model and there limitations as well
    def _show_model_explanations(self):
        selected_model = self.input_type.get()
        
        self.info_text.delete("1.0", "end")
        
        # info about generative AI model
        if selected_model == "Generative AI Model":
            gen_AI_info = information.show_Gen_AI_model_explanations()
            messagebox.showinfo("Model Information: ", gen_AI_info)
        # info about image classifier AI model
        elif selected_model == "Image Classifier AI Model":
            img_model_info = information.show_image_classifier_info()
            messagebox.showinfo("Model Information: ", img_model_info)
        else:
            messagebox.showinfo("Info","No model selected!")
            

    # software exit funciton(Menu:file->exit)
    def _exit_app(self):
        self.root.quit()
   
"""
References:
for combobox:
https://www.pythontutorial.net/tkinter/tkinter-combobox/
for LabelFrame:
https://www.pythontutorial.net/tkinter/tkinter-labelframe/
for menubar:
https://www.pythontutorial.net/tkinter/tkinter-menu/
for Text widget (multi-line text area for displaying info):
https://www.pythontutorial.net/tkinter/tkinter-text/
https://tkdocs.com/tutorial/text.html
for Buttons (to trigger commands):
https://www.pythontutorial.net/tkinter/tkinter-button/
for Handling events & commands in Tkinter:
https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
for explanation (OOP):
https://www.geeksforgeeks.org/interview-prep/object-oriented-programming-oop-tutorial/

"""