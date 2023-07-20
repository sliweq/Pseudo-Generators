import tkinter as tk 
from tkinter import ttk

class SettingsGui(tk.Toplevel):
    def __init__(self, parent, settings):
        super().__init__(parent)
        
        self.geometry('500x300')
        self.title('Simulation Settings')
        settings.set_points_amount(210)
        
        self.resizable(False,False)
        
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)
        self.columnconfigure(3,weight=1)
        
        self.labels()
        self.speed_spinbox()
        self.colors_radio()
    
    def labels(self): 
        self.label_speed = ttk.Label(self,text="Speed")
        self.label_points_amount = ttk.Label(self,text="Points amount")   
        self.axes_length = ttk.Label(self,text="Axes lenght")
        
        self.label_points_color = ttk.Label(self, text="Points colors")
        self.label_axes_colors = ttk.Label(self,text="Axes colors")
        
        self.label_speed.grid(column=0, row=0, padx=10,pady=10)
        self.label_points_amount.grid(column=0, row=1, padx=10,pady=10)
        self.axes_length.grid(column=0, row=2, padx=10,pady=10)
        
        self.label_points_color.grid(column=0, row=3, padx=10,pady=10)
        self.label_axes_colors.grid(column=0, row=5, padx=10,pady=10)
        
        
    def speed_spinbox(self):
        
        self.current_value = tk.StringVar()
        self.current_value.set("10")
        self.spinbox = ttk.Spinbox(self,from_=1,to=15,increment=1,textvariable=self.current_value,wrap=True)
        self.spinbox.grid(column=1, row=0, padx=10,pady=10)

        self.current_value_2 = tk.StringVar()
        self.current_value_2.set("200")
        self.spinbox_2 = ttk.Spinbox(self,from_=50,to=1000,increment=50,textvariable=self.current_value_2,wrap=True)
        self.spinbox_2.grid(column=1, row=1, padx=10,pady=10)

        self.current_value_3 = tk.StringVar()
        self.current_value_3.set("2000")
        self.spinbox_3 = ttk.Spinbox(self,from_=500,to=5000,increment=500,textvariable=self.current_value_3,wrap=True)
        self.spinbox_3.grid(column=1, row=2, padx=10,pady=10)
        
        #0-white 1-green 2-yellow 3-red 4-blue 5-purple
    def colors_radio(self):
        colors = (("White",0),("Green",1),("Yellow",2),("Red",3),("Blue",4),("Purple",5))
        selected_color = tk.StringVar()
        
        r = 3
        c = 1
        
        for color in colors:
            if(c == 4):
                c = 1
                r += 1
                
            rb = ttk.Radiobutton(self,text=color[0], value=color[1], variable=selected_color, command= lambda:print(selected_color.get()))
            rb.grid(column=c, row=r, padx=10,pady=10)
            c +=1
            
        
        selected_color.set(colors[1][1]) 
        
        
    def quit(self):
        #TODO sprawdzenie warptości w speed spinbox
        pass