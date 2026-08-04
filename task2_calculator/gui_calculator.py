import customtkinter as ctk

# -------------------- Appearance --------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Modern Calculator")
app.geometry("360x550")
app.resizable(False, False)

expression = ""


# -------------------- Functions --------------------
def button_click(value):
    global expression
    expression += str(value)
    display.delete(0, "end")
    display.insert("end", expression)


def clear():
    global expression
    expression = ""
    display.delete(0, "end")


def backspace():
    global expression
    expression = expression[:-1]
    display.delete(0, "end")
    display.insert("end", expression)


def calculate():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, "end")
        display.insert("end", result)
        expression = result
    except:
        display.delete(0, "end")
        display.insert("end", "Error")
        expression = ""


# -------------------- Display --------------------
display = ctk.CTkEntry(
    app,
    width=320,
    height=70,
    font=("Arial", 28),
    justify="right",
    corner_radius=15
)
display.pack(pady=20)


# -------------------- Button Layout --------------------
buttons = [
    ["AC", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

frame = ctk.CTkFrame(app, fg_color="transparent")
frame.pack()

for r, row in enumerate(buttons):
    for c, text in enumerate(row):

        if text == "=":
            cmd = calculate
        elif text == "AC":
            cmd = clear
        elif text == "⌫":
            cmd = backspace
        else:
            cmd = lambda t=text: button_click(t)

        if r == 4 and text == "0":
            btn = ctk.CTkButton(
                frame,
                text=text,
                width=160,
                height=60,
                corner_radius=15,
                font=("Arial", 22),
                command=cmd
            )
            btn.grid(row=r, column=0, columnspan=2, padx=5, pady=5)

        else:
            col = c if r < 4 else c + 1
            btn = ctk.CTkButton(
                frame,
                text=text,
                width=75,
                height=60,
                corner_radius=15,
                font=("Arial", 22),
                command=cmd
            )
            btn.grid(row=r, column=col, padx=5, pady=5)

app.mainloop()