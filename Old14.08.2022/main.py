from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout


class WidgetsExample(GridLayout):
    count = 1
    plus_or_minus = BooleanProperty(False)
    my_text = StringProperty(str(count))
    slider_to_label_value = StringProperty('50')
    text_validate_str = StringProperty('foo1')


class MultiplicationTable(GridLayout):
    text_tugriki = StringProperty('dada')


    def multiplication(self):
        self.text_tugriki = 'da'

    def on_text_validate(self, widget):
        self.text_validate_str = widget.text


    def on_value(self, value):
        pass
       # print(int(value.value))
       # self.slider_to_label_value = str(int(value.value))

    def on_active(self, state):
        print(state.active)

    def on_button_click(self):
        print(self.count)
        if self.plus_or_minus:
            self.count += 1
        else:
            self.count += 1
        self.my_text = str(self.count)

    def on_toggle_button_state(self, state):
        print(state.state)
        if state.state == 'normal':
            state.text = 'ENABLE'
            self.plus_or_minus = False
        else:
            state.text = 'DISABLE'
            self.plus_or_minus = True


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass


"""    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text='A')
        b2 = Button(text='B')
        b3 = Button(text='C')
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
        """


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


if __name__ == "__main__":
    app = TheLabApp()
    app.run()
