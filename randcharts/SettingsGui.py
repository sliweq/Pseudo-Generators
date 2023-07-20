import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showerror


class SettingsGui(tk.Toplevel):
    def __init__(self, parent, settings):
        super().__init__(parent)
        
        self.settings = settings
        
        self.geometry('500x350')
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
        self.apply_button()
    
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
        
    def colors_radio(self):
        colors = (("White",0),("Green",1),("Yellow",2),("Red",3),("Blue",4),("Purple",5))
        self.selected_color = tk.StringVar()
        
        r = 3
        c = 1
        
        for color in colors:
            if(c == 4):
                c = 1
                r += 1
                
            rb = ttk.Radiobutton(self,text=color[0], value=color[1], variable=self.selected_color, command= lambda:print(self.selected_color.get()))
            rb.grid(column=c, row=r, padx=10,pady=10)
            c +=1
            
        self.selected_color.set(colors[1][1]) 
        
        
        self.selected_color_2 = tk.StringVar()
        
        r = 5
        c = 1
        
        for color in colors:
            if(c == 4):
                c = 1
                r += 1
                
            rb = ttk.Radiobutton(self,text=color[0], value=color[1], variable=self.selected_color_2,command= lambda:print(self.selected_color_2.get()))
            rb.grid(column=c, row=r, padx=10,pady=10)
            c +=1
        
        self.selected_color_2.set(colors[0][1])
       
    def apply_button(self):
        apply = tk.Button(self, text= "Apply", command=self.quit)
        apply.grid(column=0, row=7, pady = 10, padx = 10)
        
    def quit(self):
        if(self.check_setting()):
            self.apply_settings()
            self.destroy()
        else:
            #TODO moze to wyswietylanie info 
            showerror(title="Error", message="Error in values")
        
    def check_setting(self):
        try:
            int(self.current_value.get())
            int(self.current_value_2.get())
            int(self.current_value_3.get())
        except:
            return False
        
        if(int(self.current_value_3.get()) >5000 or int(self.current_value_3.get()) < 500 ):
            return False
        
        if(int(self.current_value_2.get())>1000 or int(self.current_value_2.get()) < 50 ):
            return False
        
        if( int(self.current_value.get()) >15 or  int(self.current_value.get()) < 1 ):
            return False
        return True 
       
    def apply_settings(self):
        self.settings.set_points_color(int(self.selected_color.get()))
        self.settings.set_axes_color(int(self.selected_color_2.get()))
        
        self.settings.set_speed(int(self.current_value.get()))
        self.settings.set_points_amount(int(self.current_value_2.get()))
        self.settings.set_axes_length(int(self.current_value_3.get()))