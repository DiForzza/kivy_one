from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer
from kivy.config import Config
from kivy.uix.scatter import Scatter
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput


class BoxApp(App):
    def build(self):
        al = AnchorLayout()
        bl = BoxLayout(orientation='vertical', size_hint=[None, None], size=[300, 200])
        bl.add_widget(TextInput())
        bl.add_widget(TextInput())
        bl.add_widget(Button(text='X'))
        al.add_widget(bl)
        return al




if __name__ == '__main__':
    BoxApp().run()
