import random

from kivy.config import Config
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.switch import Switch
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 200)
Config.set('graphics', 'height', 500)

KV = """
MDBoxLayout:
    orientation: 'vertical'
    MDBoxLayout:
        md_bg_color: app.theme_cls.primary_light
        # MDFlatButton:
        #     size_hint: 1., 1.
        #     text: "Button"
        # MDFlatButton:
        #     size_hint: 1., 1.
        #     text: "Button"
    MDFlatButton:
        size_hint: 1., 1.
        text: "Button"
    MDFlatButton:
        size_hint: 1., 1.
        text: "Button"
"""


class MultiApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)


if __name__ == "__main__":
    MultiApp().run()
