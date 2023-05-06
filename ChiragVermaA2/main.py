"""
Name: Chirag Verma
Date: 06/05/2023
Brief Project Description: TRAVEL TRACKER 2.0 WITH THE HELP OF CLASSES AND KIVY
GitHub URL:
"""
from kivy.app import App
from kivy.lang import Builder
from kivy import Config
from kivy.uix.button import Button
from kivy.properties import StringProperty
from placecollection import PlaceCollection

# constants
KV_FILE = "app.kv"
FILENAME = "places.csv"


class TravelTrackerApp(App):
    """..."""
    bottom_status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.place_collection = PlaceCollection()
        self.place_collection.load_places(FILENAME)
        # print(self.place_collection)

    def build(self):
        self.title = "TravelTracker"
        self.root = Builder.load_file(KV_FILE)
        self.bottom_status_text = "Welcome to Travel Tracker 2.0"
        self.create_buttons()
        return self.root

    def create_buttons(self):
        for place in self.place_collection:
            # print(place)
            # Create a button for each place in list
            temp_button = Button(text=str(place))
            temp_button.bind(on_press=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self):
        pass

    def clear_fields(self):
        self.root.ids.name_input.text = ""
        self.root.ids.country_input.text = ""
        self.root.ids.priority_input.text = ""


if __name__ == '__main__':
    TravelTrackerApp().run()
