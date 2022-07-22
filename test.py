from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ColorProperty
from kivy.uix.boxlayout import BoxLayout

Builder.load_string(
"""

<CustomRoot>:
    canvas:
        Color:
            rgba: root.background_color
        Rectangle:
            pos: self.pos
            size: self.size

""")


class CustomRoot(BoxLayout):
    background_color = ColorProperty()  # The ListProperty will also work.


class MyApp(App):

    def build(self):
        return CustomRoot(background_color=(1, 0, 1, 1))


MyApp().run()
