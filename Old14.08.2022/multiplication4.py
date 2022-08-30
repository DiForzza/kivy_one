import random
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.switch import Switch
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel

KV = """
MDBoxLayout:
    MDGridLayout:
        cols: 2
        MDFlatButton:
            text: "Button"
        MDFlatButton:
            text: "Button"
    MDFlatButton:
        text: "Button"
    MDFlatButton:
        text: "Button"
"""


class MultiApp(MDApp):

    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    MultiApp().run()
