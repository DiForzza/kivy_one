from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color


class GUI(BoxLayout):
    board = ObjectProperty(None)


class Board(Widget):
    pass


class TestApp(App):
    def build(self):
        gui = GUI()
        return gui


if __name__=="__main__":
    app = TestApp()
    app.run()