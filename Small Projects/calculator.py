import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x500")
        self.resizable(0, 0)
        
        self.expression = ""
        
        self.create_widgets()
    
    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('CE', 5, 1)
        ]
        
        for (text, row, col) in buttons:
            self.create_button(text, row, col)
    
    def create_button(self, text, row, col):
        button = tk.Button(self, text=text, padx=20, pady=20, font=("Arial", 18), bd=8, fg="black", 
                           bg="light grey", command=lambda t=text: self.on_button_click(t))
        button.grid(row=row, column=col, sticky="nsew")
        
        # Make all columns and rows have the same weight for even spacing
        self.grid_columnconfigure(col, weight=1)
        self.grid_rowconfigure(row, weight=1)
    
    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == 'CE':
            self.expression = self.expression[:-1]
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Expression: {e}")
                self.expression = ""
        else:
            self.expression += str(char)
        
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
