from kivy.app import App
from kivy.graphics import Line, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
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

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.line = Line(points=(100, 100, 300, 400))
            Line(circle=(400, 100, 300), width=2)


class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(10)
        self.vy = dp(10)
        with self.canvas:
            self.ball = Ellipse(pos=(100,100), size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/60)

   # def on_size(self, *args):
        #print(str(self.width), str(self.height))
        #self.ball.pos = (self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)

    def update(self, dt):
        #print('updated')
        x, y = self.ball.pos

        x += self.vx
        y += self.vy

        if y + self.ball_size > self.height:
            y = self.height - self.ball_size
            self.vy = - self.vy
        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = - self.vx
        if y < 0:
            y = 0
            self.vy = -self.vy
        if x < 0:
            x = 0
            self.vx = -self.vx

        self.ball.pos = (x, y)

    def on_button_a_click(self):
        x1, y1, x2, y2 = self.line.points
        x2 += dp(50)
        if x2 > self.width:
            x2 = 0
        self.line.points = (300, 100, x2, 400)


class CanvasExample6(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class CanvasExample7(BoxLayout):
    pass

if __name__ == "__main__":
    app = TheLabApp()
    app.run()
