"""
Name: Chirag Verma
Date: 06/05/2023
Brief Project Description: TRAVEL TRACKER 2.0 WITH THE HELP OF CLASSES AND KIVY
GitHub URL:
"""
from kivy.app import App
from kivy.lang import Builder
from kivy import Config
from kivy.properties import StringProperty
from placecollection import PlaceCollection

# constants
KV_FILE = "app.kv"
FILE_NAME = "places.csv"


class TravelTrackerApp(App):
    """..."""
    bottom_status_text = "Welcome to Travel Tracker 2.0"

    def build(self):
        self.title = "TravelTracker"
        self.root = Builder.load_file(KV_FILE)
        return self.root

    def clear_fields(self):
        self.root.ids.name_input.text = ""
        self.root.ids.country_input.text = ""
        self.root.ids.priority_input.text = ""


if __name__ == '__main__':
    TravelTrackerApp().run()
