from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Frame


def factorial(n):
    """Calculate factorial of n."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def binomial_expansion(a, x, n):
    terms = []
    for i in range(n + 1):
        coeff = factorial(n) // (factorial(i) * factorial(n - i))
        term = f"{coeff * (a ** (n - i))}"
        if i > 0:
            term += f"x^{i}" if i > 1 else "x"
        terms.append(term)
    return f"({a} + {x})^{n} = " + " + ".join(terms)


def calculate():
    """Calculate and display the binomial expansion."""
    try:
        a = int(input_a.get())
        x = int(input_x.get())
        n = int(input_n.get())
        output_var.set(binomial_expansion(a, x, n))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for A, X, and n.")


def clear_entries():
    input_a.set("")
    input_x.set("")
    input_n.set("")
    output_var.set("")


def show_help():
    messagebox.showinfo(
        "Help",
        "Enter the values for A (constant term), X (variable term), and n (power)."
        "\nClick 'Calculate' to see the binomial expansion of (A + X)^n."
        "\nClick 'Clear' to reset the inputs."
        "\nClick 'Back' to return to the main screen."
    )


def show_calculator():
    """Switch to the calculator screen."""
    home_frame.place_forget()
    calculator_frame.place(relwidth=1, relheight=1)


def show_home():
    """Switch to the home screen."""
    calculator_frame.place_forget()
    home_frame.place(relwidth=1, relheight=1)


def exit_app():
    root.quit()


# Main Application Window
root = Tk()
root.title("Binomial Expansion Calculator")
root.geometry("800x500")
root.configure(bg="#e6f2ff")

# Home Screen
home_frame = Frame(root, bg="#e6f2ff")
home_frame.place(relwidth=1, relheight=1)

Label(
    home_frame, text="Binomial Expansion", font=("Helvetica", 32, "bold"), bg="#e6f2ff", fg="#003366"
).place(x=250, y=50)
Label(
    home_frame, text="CS ELECTIVE - I", font=("Helvetica", 8), bg="#e6f2ff", fg="#003366"
).place(x=350, y=130)

Button(
    home_frame, text="Start", command=show_calculator, font=("Helvetica", 12), bg="#b3cde0", fg="#003366", bd=0,
    width=20, height=2
).place(x=300, y=200)

Button(
    home_frame, text="Help", command=show_help, font=("Helvetica", 12), bg="#b3cde0", fg="#003366", bd=0, width=20,
    height=2
).place(x=300, y=300)

Button(
    home_frame, text="Exit", command=exit_app, font=("Helvetica", 12), bg="#b3cde0", fg="#003366", bd=0, width=20,
    height=2
).place(x=300, y=400)

# Calculator Screen
calculator_frame = Frame(root, bg="#e6f2ff")

Label(calculator_frame, text="Enter A (constant term):", bg="#e6f2ff", fg="#003366").place(x=200, y=50)
input_a = StringVar()
Entry(calculator_frame, textvariable=input_a, width=10).place(x=450, y=50)
Label(calculator_frame, text="Enter X (variable term):", bg="#e6f2ff", fg="#003366").place(x=200, y=100)
input_x = StringVar()
Entry(calculator_frame, textvariable=input_x, width=10).place(x=450, y=100)
Label(calculator_frame, text="Enter n (power):", bg="#e6f2ff", fg="#003366").place(x=200, y=150)
input_n = StringVar()
Entry(calculator_frame, textvariable=input_n, width=10).place(x=450, y=150)
output_var = StringVar()
Label(calculator_frame, textvariable=output_var, bg="#e6f2ff", fg="#003366").place(x=200, y=220)

Button(
    calculator_frame, text="Calculate", command=calculate, bg="#b3cde0", fg="#003366", bd=0, width=15, height=2
).place(x=200, y=270)
Button(
    calculator_frame, text="Clear", command=clear_entries, bg="#b3cde0", fg="#003366", bd=0, width=15, height=2
).place(x=350, y=270)
Button(
    calculator_frame, text="Back", command=show_home, bg="#b3cde0", fg="#003366", bd=0, width=15, height=2
).place(x=500, y=270)

root.mainloop()