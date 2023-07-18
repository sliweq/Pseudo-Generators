import tkinter as tk 
from tkinter import ttk

class SettingsGui(tk.Toplevel):
    def __init__(self, parent, settings):
        super().__init__(parent)
        
        self.geometry('300x300')
        self.title('Simulation Settings')
        settings.set_points_amount(210)
        
        self.resizable(False,False)
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=3)
        
        self.labels()
        self.speed_spinbox()
    
    def labels(self): 
        self.label_points_color = ttk.Label(self, text="Points colors")
        self.label_axes_colors = ttk.Label(self,text="Axes colors")
        self.label_speed = ttk.Label(self,text="Speed")
        self.axes_length = ttk.Label(self,text="Axes lenght")
        self.label_points_color = ttk.Label(self,text="Points amount")   
        
        self.label_points_color.grid(column=0, row=2, padx=10,pady=10)
        self.label_axes_colors.grid(column=0, row=1, padx=10,pady=10)
        
        self.label_speed.grid(column=0, row=0, padx=10,pady=10)
        
        self.axes_length.grid(column=0, row=3, padx=10,pady=10)
        self.label_points_color.grid(column=0, row=4, padx=10,pady=10)
        
    def speed_spinbox(self):
        self.current_value = tk.StringVar()
        self.current_value.set("10")
        self.spinbox = ttk.Spinbox(self,from_=1,to=15,increment=1,textvariable=self.current_value,wrap=True)
        
        self.spinbox.grid(column=1, row=0, padx=10,pady=10)
        