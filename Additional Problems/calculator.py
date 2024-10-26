import tkinter as tk
import math

# Create the main application window
window = tk.Tk()
window.title("Advanced Calculator")
window.geometry("400x600")
window.config(bg="#2C2F33")  # Set background color

# Global variable to hold the current expression
expression = ""

# Function to update the input field when buttons are clicked
def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# Function to clear the input field
def button_clear():
    global expression
    expression = ""
    input_text.set("")

# Function to calculate the result
def button_equal():
    global expression
    try:
        result = str(eval(expression))  # Evaluate the expression
        input_text.set(result)
        expression = result  # Update the expression with the result
    except ZeroDivisionError:
        input_text.set("Error: Division by Zero")
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

# Scientific functions
def button_sqrt():
    global expression
    try:
        result = str(math.sqrt(eval(expression)))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def button_log():
    global expression
    try:
        result = str(math.log10(eval(expression)))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def button_ln():
    global expression
    try:
        result = str(math.log(eval(expression)))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def button_sin():
    global expression
    try:
        result = str(math.sin(math.radians(eval(expression))))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def button_cos():
    global expression
    try:
        result = str(math.cos(math.radians(eval(expression))))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def button_tan():
    global expression
    try:
        result = str(math.tan(math.radians(eval(expression))))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def button_exp():
    global expression
    try:
        result = str(math.exp(eval(expression)))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def button_factorial():
    global expression
    try:
        result = str(math.factorial(int(eval(expression))))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Create an input field to display the expression and result
input_text = tk.StringVar()
input_frame = tk.Frame(window, width=400, height=50, bd=0, bg="#2C2F33")
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 20, 'bold'), textvariable=input_text, width=22, bg="#4E5D6C", fg="white", bd=0, justify="right")
input_field.grid(row=0, column=0)
input_field.pack(ipady=15)  # Increase the height of the input field

# Create a frame for the buttons
button_frame = tk.Frame(window, bg="#2C2F33")
button_frame.pack()

# Button style settings
button_color = "#4E5D6C"
text_color = "white"
button_font = ('arial', 14)

# First row: Clear, Parentheses, Pi, Euler's number
clear = tk.Button(button_frame, text="C", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=button_clear)
clear.grid(row=0, column=0, padx=10, pady=10)
open_paren = tk.Button(button_frame, text="(", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click("("))
open_paren.grid(row=0, column=1, padx=10, pady=10)
close_paren = tk.Button(button_frame, text=")", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click(")"))
close_paren.grid(row=0, column=2, padx=10, pady=10)
pi_button = tk.Button(button_frame, text="π", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click(math.pi))
pi_button.grid(row=0, column=3, padx=10, pady=10)
e_button = tk.Button(button_frame, text="e", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click(math.e))
e_button.grid(row=0, column=4, padx=10, pady=10)

# Second row: Numbers 7, 8, 9, Divide, Square root
seven = tk.Button(button_frame, text="7", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click(7))
seven.grid(row=1, column=0, padx=10, pady=10)
eight = tk.Button(button_frame, text="8", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click(8))
eight.grid(row=1, column=1, padx=10, pady=10)
nine = tk.Button(button_frame, text="9", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click(9))
nine.grid(row=1, column=2, padx=10, pady=10)
divide = tk.Button(button_frame, text="/", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click("/"))
divide.grid(row=1, column=3, padx=10, pady=10)
sqrt = tk.Button(button_frame, text="√", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=button_sqrt)
sqrt.grid(row=1, column=4, padx=10, pady=10)

# Third row: Numbers 4, 5, 6, Multiply, Exponent
four = tk.Button(button_frame, text="4", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click(4))
four.grid(row=2, column=0, padx=10, pady=10)
five = tk.Button(button_frame, text="5", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click(5))
five.grid(row=2, column=1, padx=10, pady=10)
six = tk.Button(button_frame, text="6", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click(6))
six.grid(row=2, column=2, padx=10, pady=10)
multiply = tk.Button(button_frame, text="*", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click("*"))
multiply.grid(row=2, column=3, padx=10, pady=10)
exp = tk.Button(button_frame, text="exp", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=button_exp)
exp.grid(row=2, column=4, padx=10, pady=10)

# Fourth row: Numbers 1, 2, 3, Subtract, Logarithm
one = tk.Button(button_frame, text="1", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click(1))
one.grid(row=3, column=0, padx=10, pady=10)
two = tk.Button(button_frame, text="2", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click(2))
two.grid(row=3, column=1, padx=10, pady=10)
three = tk.Button(button_frame, text="3", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click(3))
three.grid(row=3, column=2, padx=10, pady=10)
subtract = tk.Button(button_frame, text="-", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click("-"))
subtract.grid(row=3, column=3, padx=10, pady=10)
log = tk.Button(button_frame, text="log", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=button_log)
log.grid(row=3, column=4, padx=10, pady=10)

# Fifth row: Decimal, Number 0, Factorial, Add, Natural Logarithm (ln)
decimal = tk.Button(button_frame, text=".", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click("."))
decimal.grid(row=4, column=0, padx=10, pady=10)
zero = tk.Button(button_frame, text="0", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click(0))
zero.grid(row=4, column=1, padx=10, pady=10)
factorial = tk.Button(button_frame, text="n!", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=button_factorial)
factorial.grid(row=4, column=2, padx=10, pady=10)
add = tk.Button(button_frame, text="+", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=lambda: button_click("+"))
add.grid(row=4, column=3, padx=10, pady=10)
ln = tk.Button(button_frame, text="ln", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=button_ln)
ln.grid(row=4, column=4, padx=10, pady=10)

# Sixth row: Sin, Cos, Tan, Equal button
sin = tk.Button(button_frame, text="sin", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=button_sin)
sin.grid(row=5, column=0, padx=10, pady=10)
cos = tk.Button(button_frame, text="cos", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=button_cos)
cos.grid(row=5, column=1, padx=10, pady=10)
tan = tk.Button(button_frame, text="tan", width=5, height=2, bg=button_color, fg=text_color, font=button_font, command=button_tan)
tan.grid(row=5, column=2, padx=10, pady=10)
equals = tk.Button(button_frame, text="=", width=12, height=2, bg="orange", fg="white", font=button_font, command=button_equal)
equals.grid(row=5, column=3, columnspan=2, padx=10, pady=10)

# Run the main loop for the application
window.mainloop()