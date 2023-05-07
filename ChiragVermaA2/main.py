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
from kivy.properties import ListProperty
from placecollection import PlaceCollection
from place import Place

# constants
KV_FILE = "app.kv"
FILENAME = "places.csv"
SORT_KEY_TO_SORT_VALUE = {'Visited': 'is_visited', 'Name': 'name', 'Country': 'country', 'Priority': 'priority'}


class TravelTrackerApp(App):
    """..."""
    current_sort_key = StringProperty()
    sort_keys = ListProperty()
    top_status_text = StringProperty()
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
        self.top_status_text = f"{self.place_collection.number_of_unvisited_places()}"
        self.sort_keys = SORT_KEY_TO_SORT_VALUE.keys()
        print(self.sort_keys)
        self.current_sort_key = self.sort_keys[0]
        return self.root

    def change_sort_key(self, sort_key):
        print(self.place_collection)
        self.place_collection.sort(SORT_KEY_TO_SORT_VALUE[sort_key])
        print(self.place_collection)
        self.root.ids.entries_box.clear_widgets()
        self.create_buttons()

    def create_buttons(self):
        self.root.ids.entries_box.clear_widgets()
        for place in self.place_collection:
            # print(place)
            # Create a button for each place in list
            temp_button = Button(text=str(place))
            temp_button.bind(on_release=self.press_entry)
            temp_button.place = place
            if place.is_visited:
                temp_button.background_color = 1, 1, 1, 1  # set background color to white
            else:
                temp_button.background_color = 0, 1, 0, 1  # set background color to green for visited places
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        place = instance.place
        instance.text = str(place)
        if place.is_visited:
            place.mark_unvisited()
            instance.background_color = 0, 1, 0, 1  # set background color to green
            if place.is_important():
                self.bottom_status_text = f"You need to visit {place.name}.Get Going!"
            else:
                self.bottom_status_text = f"You need to visit {place.name}."
        else:
            place.mark_visited()
            instance.background_color = 1, 1, 1, 1  # set background color to white
            if place.is_important():
                self.bottom_status_text = f"You visited {place.name}. Great Travelling!"
            else:
                self.bottom_status_text = f"You visited {place.name}."
        instance.text = str(place)
        self.change_sort_key(self.current_sort_key)

    def create_place(self):
        name = self.root.ids.name_input.text.strip().title()
        country = self.root.ids.country_input.text.strip().title()
        priority = self.root.ids.priority_input.text.strip()
        if name == "" or country == "" or priority == "":
            self.bottom_status_text = "All fields must be completed"
            return
        try:
            priority = int(priority)
        except ValueError:
            self.bottom_status_text = "Please enter a valid number"
            return
        if priority < 1:
            self.bottom_status_text = "Priority must be > 0"
            return
        Place(name, country, priority, False)
        self.place_collection.add_place(Place(name, country, priority, False))
        self.create_buttons()
        self.clear_fields()
        self.bottom_status_text = f"{name} in {country}, priority {priority} added."

    def clear_fields(self):
        self.root.ids.name_input.text = ""
        self.root.ids.country_input.text = ""
        self.root.ids.priority_input.text = ""
        self.bottom_status_text = ""

    def on_stop(self):
        self.place_collection.save_places(FILENAME)
        print(f"{len(self.place_collection)} places saved to {FILENAME}")


if __name__ == '__main__':
    TravelTrackerApp().run()
