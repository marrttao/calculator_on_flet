import flet as ft
import math

def main(page):
    # Set alignment for the entire page
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    calculate_window = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)

    def update_text(value):
        if calculate_window.value == "0" or calculate_window.value == "Error":
            calculate_window.value = value
        else:
            calculate_window.value += value
        calculate_window.update()

    def calculate():
        try:
            # Replace the square root symbol with the actual math.sqrt function call
            expression = calculate_window.value.replace("√", "math.sqrt(") + ")"
            calculate_window.value = str(eval(expression))
        except:
            calculate_window.value = "Error"
        calculate_window.update()

    def clear():
        calculate_window.value = "0"
        calculate_window.update()

    # Create title and buttons
    title = ft.Text("Calculator")
    button1 = ft.ElevatedButton("1", on_click=lambda e: update_text("1"))
    button2 = ft.ElevatedButton("2", on_click=lambda e: update_text("2"))
    button3 = ft.ElevatedButton("3", on_click=lambda e: update_text("3"))
    button_plus = ft.ElevatedButton("+", on_click=lambda e: update_text("+"))
    button4 = ft.ElevatedButton("4", on_click=lambda e: update_text("4"))
    button5 = ft.ElevatedButton("5", on_click=lambda e: update_text("5"))
    button6 = ft.ElevatedButton("6", on_click=lambda e: update_text("6"))
    button_minus = ft.ElevatedButton("-", on_click=lambda e: update_text("-"))
    button7 = ft.ElevatedButton("7", on_click=lambda e: update_text("7"))
    button8 = ft.ElevatedButton("8", on_click=lambda e: update_text("8"))
    button9 = ft.ElevatedButton("9", on_click=lambda e: update_text("9"))
    button_multiply = ft.ElevatedButton("*", on_click=lambda e: update_text("*"))
    button0 = ft.ElevatedButton("0", on_click=lambda e: update_text("0"))
    button_dot = ft.ElevatedButton(".", on_click=lambda e: update_text("."))
    button_square = ft.ElevatedButton("√", on_click=lambda e: update_text("√"))
    button_divide = ft.ElevatedButton("÷", on_click=lambda e: update_text("/"))
    button_equals = ft.ElevatedButton("=", width=100, on_click=lambda e: calculate())
    button_clear = ft.ElevatedButton("C", width=100, on_click=lambda e: clear())

    # Add objects to Column for vertical alignment
    page.add(
        ft.Column(
            [
                ft.Row([title], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([calculate_window], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([button1, button2, button3, button_plus], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([button4, button5, button6, button_minus], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([button7, button8, button9, button_multiply], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([button0, button_dot, button_square, button_divide], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([button_equals, button_clear], alignment=ft.MainAxisAlignment.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

# Run the application
ft.app(target=main)