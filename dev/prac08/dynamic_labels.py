from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    message = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = {"Mukshit", "Chirag", "Jasmine"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)
        return self.root


DynamicLabelsApp().run()
