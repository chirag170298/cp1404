""" Program to convert miles to km."""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

CONVERSION_RATE = 1.609


class MilesToKm(App):
    """Kivy app for converting miles to km."""
    message = StringProperty()

    def build(self):
        """Build the kivy app from the kv file."""
        Window.size = (300, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, miles):
        """Covert the mile into km."""
        self.message = str(self.convert_to_float(miles) * CONVERSION_RATE)

    def handle_increment(self, value):
        """ handle the increment and decrement part of kivy app/"""
        miles = self.convert_to_float(self.root.ids.user_input.text) + value
        self.root.ids.user_input.text = str(miles)

    @staticmethod
    def convert_to_float(text):
        """Convert str to float and return 0.0 in case of value error."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesToKm().run()
