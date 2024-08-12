from tkinter import Tk, Entry, Button, StringVar
import math

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x4200+0+66')
        master.config(bg='gray')
        master.resizable(False, False)
        master.iconbitmap("download.ico")

        self.equation = StringVar()
        self.entry_value = ''

        Entry(width=17, bg='lightgray', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # Button grid
        buttons = [
            ('C', self.clear),
            ('(', lambda: self.show('(')),
            (')', lambda: self.show(')')),
            ('%', lambda: self.show('%')),
            ('1', lambda: self.show(1)),
            ('2', lambda: self.show(2)),
            ('3', lambda: self.show(3)),
            ('4', lambda: self.show(4)),
            ('5', lambda: self.show(5)),
            ('6', lambda: self.show(6)),
            ('7', lambda: self.show(7)),
            ('8', lambda: self.show(8)),
            ('9', lambda: self.show(9)),
            ('0', lambda: self.show(0)),
            ('.', lambda: self.show('.')),
            ('+', lambda: self.show('+')),
            ('-', lambda: self.show('-')),
            ('/', lambda: self.show('/')),
            ('*', lambda: self.show('*')),
            ('X^2', lambda: self.show('**2')),
            ('pow', lambda: self.show('**')),
            ('√', lambda: self.show("math.sqrt")),
            ('Sin()', lambda: self.show('math.sin(')),
            ('Cos()', lambda: self.show('math.cos(')),
            ('Tan()', lambda: self.show('math.tan(')),
            ('log()', lambda: self.show('math.log(')),
            ('π', lambda: self.show("math.pi")),            
            ('=', self.solve)
            ]

        x, y = 0, 50
        for button_text, command in buttons:
            Button(width=11, height=4, text=button_text, relief='flat', bg='white', command=command).place(x=x, y=y)
            x += 90
            if x > 270:
                x = 0
                y += 75

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(str(result))
        except SyntaxError:
            self.equation.set("Error")

root = Tk()
calculator = Calculator(root)
root.mainloop()