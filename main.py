# pip install --upgrade --force-reinstall Kivy_examples-2.1.0-py2.py3-none-any.whl
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class Container(GridLayout):
    pass


class MyApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MyApp().run()