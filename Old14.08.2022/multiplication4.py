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
                MDTopAppBar:
                    title: "Navigation Drawer"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open")]]
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
