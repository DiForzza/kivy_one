from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse, Rectangle,Line)
from kivy.config import Config
from kivy.uix.button import Button

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)


class PainterWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 1, 0, 1)
            rad = 30
            Ellipse(pos=(touch.x-rad/2, touch.y-rad/2), size=(rad, rad))
            touch.ud['line']=Line(points=(touch.x, touch.y), width=15)

    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)


class PaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = PainterWidget()
        parent.add_widget(self.painter)

        parent.add_widget(Button(text='Clear', on_press = self.clear_canvas, size=(100, 50)))

        return parent

    def clear_canvas(self, instance):
        self.painter.canvas.clear()


if __name__ == '__main__':
    PaintApp().run()