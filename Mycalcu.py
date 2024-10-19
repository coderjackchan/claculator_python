import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        # Entry widget to display the input and results
        self.display = tk.Entry(master, width=30, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'  # Clear button
        ]

        # Create and place buttons on the grid
        row = 1
        col = 0
        for button_text in buttons:
            button = tk.Button(master, text=button_text, width=5, height=2,
                               command=lambda text=button_text: self.button_click(text))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, text):
        if text == '=':
            try:
                result = str(eval(self.display.get()))  # Evaluate the expression
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except (SyntaxError, ZeroDivisionError, NameError):  #basic error handling
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == 'C':
            self.display.delete(0, tk.END)  # Clear the display
        else:
            self.display.insert(tk.END, text)  # Append the button text to the display



root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
