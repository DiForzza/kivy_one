import kivy
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
kivy.require('1.9.0')


class SquareWidget(Widget):
    pass


class ScatterWidget(Scatter):
    pass


class Scatter_App(RelativeLayout):
    pass


class ScatterApp(App):
    def build(self):
        return Scatter_App()


if __name__ == '__main__':
    ScatterApp().run()
