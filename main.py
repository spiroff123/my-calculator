from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Calculator(App):

    def build(self):
        main_layout = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        self.display = Label(
            text="0",
            font_size=42,
            halign="right",
            valign="middle",
            size_hint_y=0.3
        )

        main_layout.add_widget(self.display)

        buttons_layout = GridLayout(
            cols=4,
            spacing=6
        )

        buttons = [
            "7", "8", "9", "÷",
            "4", "5", "6", "×",
            "1", "2", "3", "−",
            "C", "0", ".", "+"
        ]

        for text in buttons:
            button = Button(
                text=text,
                font_size=26
            )
            button.bind(on_press=self.button_pressed)
            buttons_layout.add_widget(button)

        equal_button = Button(
            text="=",
            font_size=30,
            size_hint_y=0.18
        )
        equal_button.bind(on_press=self.calculate)

        main_layout.add_widget(buttons_layout)
        main_layout.add_widget(equal_button)

        return main_layout

    def button_pressed(self, button):
        value = button.text

        if value == "C":
            self.display.text = "0"
            return

        operators = ["+", "−", "×", "÷"]

        if value in operators:
            value = {
                "×": "*",
                "÷": "/",
                "−": "-"
            }[value]

        if self.display.text == "0":
            self.display.text = value
        else:
            self.display.text += value

    def calculate(self, button):
        try:
            expression = self.display.text
            result = eval(expression)
            self.display.text = str(result)
        except:
            self.display.text = "Error"


Calculator().run()