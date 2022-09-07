#!/usr/bin/python3
import tkinter as tk


class CalculatorUiApp:
    def __init__(self, master=None):
        self.equation = []
        self.numberselect = 0
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.configure(background="#9e97ff", height=450, width=307)
        self.toplevel1.attributes("-alpha", 0.9)
        self.toplevel1.geometry("307x450")
        self.toplevel1.title("My First Calculator")
        self.frame = tk.Frame(self.toplevel1)
        self.frame.configure(background="#9e97ff", height=450, width=305)
        self.output = tk.Entry(self.frame)
        self.output.configure(
            background="#e9f8e1",
            borderwidth=2,
            font="{Maiandra GD} 24 {bold}",
            justify="center",
            relief="raised",
        )
        self.output.place(anchor="nw", height=69, width=256, x=24, y=21)
        self.digit_1 = tk.Button(self.frame)
        self.digit_1.configure(
            background="#ebf7e3",
            borderwidth=2,
            cursor="arrow",
            font="{Maiandra GD} 24 {bold}",
            justify="right",
            relief="raised",
            text="1",
            command=lambda: self.output.insert(len(self.output.get()), 1)
        )
        self.digit_1.place(anchor="nw", height=54, width=54, x=24, y=235)
        self.digit_2 = tk.Button(self.frame)
        self.digit_2.configure(
            background="#ebf7e3",
            borderwidth=2,
            cursor="arrow",
            font="{Maiandra GD} 24 {bold}",
            justify="center",
            relief="raised",
            text="2",
            command=lambda: self.output.insert(len(self.output.get()), 2)
        )
        self.digit_2.place(anchor="nw", height=54, width=54, x=91, y=235)
        self.digit_3 = tk.Button(self.frame)
        self.digit_3.configure(
            background="#ebf7e3",
            borderwidth=2,
            cursor="arrow",
            font="{Maiandra GD} 24 {bold}",
            justify="center",
            relief="raised",
            text="3",
            command=lambda: self.output.insert(len(self.output.get()), 3)
        )
        self.digit_3.place(anchor="nw", height=54, width=54, x=159, y=235)
        self.digit_4 = tk.Button(self.frame)
        self.digit_4.configure(
            background="#ebf7e3",
            borderwidth=2,
            cursor="arrow",
            font="{Maiandra GD} 24 {bold}",
            justify="left",
            relief="raised",
            text="4",
            command=lambda: self.output.insert(len(self.output.get()), 4)
        )
        self.digit_4.place(anchor="nw", height=54, width=54, x=24, y=169)
        self.digit_5 = tk.Button(self.frame)
        self.digit_5.configure(
            background="#ebf7e3",
            borderwidth=2,
            cursor="arrow",
            font="{Maiandra GD} 24 {bold}",
            justify="center",
            relief="raised",
            text="5",
            command=lambda: self.output.insert(len(self.output.get()), 5)
        )
        self.digit_5.place(anchor="nw", height=54, width=54, x=91, y=169)
        self.digit_6 = tk.Button(self.frame)
        self.digit_6.configure(
            background="#ebf7e3",
            borderwidth=2,
            cursor="arrow",
            font="{Maiandra GD} 24 {bold}",
            justify="center",
            relief="raised",
            text="6",
            command=lambda: self.output.insert(len(self.output.get()), 6)
        )
        self.digit_6.place(anchor="nw", height=54, width=54, x=159, y=169)
        self.digit_7 = tk.Button(self.frame)
        self.digit_7.configure(
            background="#ebf7e3",
            borderwidth=2,
            cursor="arrow",
            font="{Maiandra GD} 24 {bold}",
            justify="left",
            relief="raised",
            text="7",
            command=lambda: self.output.insert(len(self.output.get()), 7)
        )
        self.digit_7.place(anchor="nw", height=54, width=54, x=24, y=103)
        self.digit_8 = tk.Button(self.frame)
        self.digit_8.configure(
            background="#ebf7e3",
            borderwidth=2,
            cursor="arrow",
            font="{Maiandra GD} 24 {bold}",
            justify="left",
            relief="raised",
            text="8",
            command=lambda: self.output.insert(len(self.output.get()), 8)
        )
        self.digit_8.place(anchor="nw", height=54, width=54, x=91, y=103)
        self.digit_9 = tk.Button(self.frame)
        self.digit_9.configure(
            background="#ebf7e3",
            borderwidth=2,
            cursor="arrow",
            font="{Maiandra GD} 24 {bold}",
            justify="left",
            relief="raised",
            text="9",
            command=lambda: self.output.insert(len(self.output.get()), 9)
        )
        self.digit_9.place(anchor="nw", height=54, width=54, x=158, y=103)
        self.digit_0 = tk.Button(self.frame)
        self.digit_0.configure(
            background="#ebf7e3",
            borderwidth=2,
            cursor="arrow",
            font="{Maiandra GD} 24 {bold}",
            justify="center",
            relief="raised",
            text="0",
            command=lambda: self.output.insert(len(self.output.get()), 0)
        )
        self.digit_0.place(anchor="nw", height=54, width=54, x=24, y=301)
        self.digit_mult = tk.Button(self.frame)
        self.digit_mult.configure(
            background="#ebf7e3",
            borderwidth=2,
            cursor="arrow",
            font="{Maiandra GD} 24 {bold}",
            justify="center",
            relief="raised",
            text="X",
            command=self.multiply
        )
        self.digit_mult.place(anchor="nw", height=54, width=54, x=225, y=169)
        self.digit_divide = tk.Button(self.frame)
        self.digit_divide.configure(
            background="#ebf7e3",
            borderwidth=2,
            cursor="based_arrow_down",
            font="{Maiandra GD} 24 {bold}",
            justify="center",
            relief="raised",
            text="÷",
            command=self.divide
        )
        self.digit_divide.place(anchor="nw", height=54, width=54, x=225, y=103)
        self.digit_minus = tk.Button(self.frame)
        self.digit_minus.configure(
            background="#ebf7e3",
            borderwidth=2,
            cursor="arrow",
            font="{Maiandra GD} 24 {bold}",
            justify="center",
            relief="raised",
            text="-",
            command=self.minus
        )
        self.digit_minus.place(anchor="nw", height=54, width=54, x=225, y=235)
        self.button_period = tk.Button(self.frame)
        self.button_period.configure(
            background="#ebf7e3",
            borderwidth=2,
            cursor="arrow",
            font="{Maiandra GD} 24 {bold}",
            justify="center",
            relief="raised",
            text=".",
            command=lambda: self.output.insert(self.output.get(),'.'),
        )
        self.button_period.place(anchor="nw", height=54, width=54, x=90, y=301)
        self.button_equals = tk.Button(self.frame)
        self.button_equals.configure(
            background="#ebf7e3",
            borderwidth=2,
            cursor="arrow",
            font="{Maiandra GD} 24 {bold}",
            justify="center",
            relief="raised",
            text="=",
            command=self.evaluate
        )
        self.button_equals.place(anchor="nw", height=54, width=54, x=159, y=301)
        self.button_plus = tk.Button(self.frame)
        self.button_plus.configure(
            background="#ebf7e3",
            borderwidth=2,
            cursor="arrow",
            font="{Maiandra GD} 24 {bold}",
            justify="center",
            relief="raised",
            text="+",
            command=self.plus
        )
        self.button_plus.place(anchor="nw", height=54, width=54, x=225, y=301)
        self.digit_reset = tk.Button(self.frame)
        self.digit_reset.configure(
            background="#ebf7e3",
            cursor="arrow",
            font="{Maiandra GD} 24 {bold}",
            justify="center",
            relief="raised",
            text="Reset",
            command=lambda: self.output.delete(0, 'end')
        )
        self.digit_reset.place(anchor="nw", height=54, width=254, x=24, y=370)
        self.frame.pack(side="top")

        # Main widget
        self.mainwindow = self.toplevel1

    def divide(self):
        if self.output.get():
            self.equation.append(self.output.get())
            self.equation.append('divide')
            self.output.delete(0, 'end')
            print(self.equation)

    def multiply(self):
        if self.output.get():
            self.equation.append(self.output.get())
            self.equation.append('multiply')
            self.output.delete(0, 'end')
            print(self.equation)

    def minus(self):
        if self.output.get():
            self.equation.append(self.output.get())
            self.equation.append('minus')
            self.output.delete(0, 'end')
            print(self.equation)

    def plus(self):
        if self.output.get():
            self.equation.append(self.output.get())
            self.equation.append('plus')
            self.output.delete(0, 'end')
            print(self.equation)

    def evaluate(self):
        if self.output.get():
            self.equation.append(self.output.get())
            self.output.delete(0, 'end')

        self.plus_count = self.equation.count('plus')
        self.minus_count = self.equation.count('minus')
        self.divide_count = self.equation.count('divide')
        self.multiply_count = self.equation.count('multiply')

        for i in range(self.divide_count):
            symbol = self.equation.index('divide')
            addition = float(self.equation[symbol-1])/float(self.equation[symbol+1])
            self.equation[symbol] = addition
            del self.equation[symbol-1]
            del self.equation[symbol]

        for i in range(self.multiply_count):
            symbol = self.equation.index('multiply')
            addition = float(self.equation[symbol-1])*float(self.equation[symbol+1])
            self.equation[symbol] = addition
            del self.equation[symbol-1]
            del self.equation[symbol]

        for i in range(self.plus_count):
            symbol = self.equation.index('plus')
            addition = float(self.equation[symbol-1])+float(self.equation[symbol+1])
            self.equation[symbol] = addition
            del self.equation[symbol-1]
            del self.equation[symbol]


        for i in range(self.minus_count):
            symbol = self.equation.index('minus')
            subtraction = float(self.equation[symbol-1])-float(self.equation[symbol+1])
            self.equation[symbol] = subtraction
            del self.equation[symbol-1]
            del self.equation[symbol]

        if int(self.equation[0]) == self.equation[0]:
            self.equation = int(self.equation[0])

        self.output.insert(0, self.equation)
        self.equation = []

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = CalculatorUiApp()
    app.run()
