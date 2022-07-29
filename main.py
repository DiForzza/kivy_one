from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.config import Config
from kivy.properties import ColorProperty
from kivy.uix.gridlayout import GridLayout

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 640)
Config.set('graphics', 'height', 840)


class GUI(BoxLayout):
    pass


class TestApp(App):
    def build(self):
        return GUI()


if __name__ == "__main__":
    app = TestApp()
    app.run()
