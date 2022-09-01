from kivy.config import Config
from kivymd.uix.boxlayout import MDBoxLayout

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 800)

import random
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.switch import Switch
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel



KV = """
MDScreen:
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:
                MDBoxLayout:
                    MDFlatButton:
                        text: 'test'
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)
        
            ContentNavigationDrawer:
                MDFlatButton:
"""

class ContentNavigationDrawer(MDBoxLayout):
    pass

class MultiApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)


if __name__ == "__main__":
    MultiApp().run()
