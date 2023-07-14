import tkinter as tk
from tkinter import ttk

class Gui():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x400")
        self.window.title("Initial Settings")
        self.window.resizable(False,False)
        self.window.attributes('-topmost', 1)
        
        self.generators_names = ["Linear congruential","Middle square","Lehmer","Lagged Fibonacci"]
        self.describsions = [["seed","modulo-m","multiplier-a","increment-c"],["seed","","number of digits - a",""],["seed","modulo-m","multiplier-a",""],["seed","modulo-m","j","k"]]
        self.selecte_description = self.describsions[0]
        self.returning_value = []
    
    def labels(self):
        self.generator_label = ttk.Label(self.window, text="Generator")
        self.seed_label = ttk.Label(self.window, text=f"{self.selecte_description[0]}")
        self.modulo_label = ttk.Label(self.window, text=f"{self.selecte_description[1]}")
        self.a_label = ttk.Label(self.window, text=f"{self.selecte_description[2]}")
        self.c_label = ttk.Label(self.window, text=f"{self.selecte_description[3]}") 
        
        self.generator_label.grid(column=0, row=0, padx=10,pady=10)
        self.seed_label.grid(column=0, row=1, padx=10,pady=10)
        self.modulo_label.grid(column=0, row=2, padx=10,pady=10)
        self.a_label.grid(column=0, row=3, padx=10, pady=10)
        self.c_label.grid(column=0, row=4,padx=10,pady=10)
    
    def entrences(self):
        self.seed_entry = tk.Entry(self.window)
        self.modulo_entry = tk.Entry(self.window)
        self.a_entry = tk.Entry(self.window)
        self.c_entry = tk.Entry(self.window)
        
        self.seed_entry.grid(column=1, row = 1, padx=10, pady=10)
        self.modulo_entry.grid(column=1, row = 2, padx=10, pady=10)
        self.a_entry.grid(column=1, row = 3, padx=10, pady=10)
        self.c_entry.grid(column=1, row = 4, padx=10, pady=10)
        
    def combo_box(self):
        self.generator_box = tk.StringVar()
        self.generators_cb = ttk.Combobox(self.window, textvariable=self.generator_box)

        self.generators_cb['values'] = self.generators_names
        self.generators_cb['state'] = 'readonly'

        self.generators_cb.grid(column=1, row=0, padx=10,pady=10)  
    
    def button(self):
        self.generate_button = ttk.Button(self.window, text="Generate", command=self.action_button)
        self.generate_button.grid(column=0, row=5,padx=10,pady=10,columnspan=3) # sticky="WENS"

    def action_button(self):
        #TODO
        #exceptions if wrong values
        print(f"{self.generator_box.get()} {self.seed_entry.get()} {self.a_entry.get()} {self.c_entry.get()}")
        
        try:
            self.generators_names.index(self.generator_box.get())
            self.returning_value = [self.generators_names.index(self.generator_box.get())+1,self.seed_entry.get(),self.modulo_entry.get(),self.a_entry.get(),self.c_entry.get()]
            self.window.destroy()
        except:
            print("Xd")

    def action_combobox(self,event):
        self.selecte_description = self.describsions[self.generators_names.index(self.generator_box.get())] 
        self.seed_label.config(text=f"{self.selecte_description[0]}")
        self.modulo_label.config(text=f"{self.selecte_description[1]}")
        self.a_label.config(text=f"{self.selecte_description[2]}")
        self.c_label.config(text=f"{self.selecte_description[3]}") 
        

    def run(self):
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(2, weight=3)

        self.labels()
        self.entrences()
        self.combo_box()
        self.button()
        
        self.generators_cb.current()
        self.generators_cb.bind("<<ComboboxSelected>>",self.action_combobox)
        
        self.window.mainloop()
        return self.returning_value

#TODO label with generators patterns

