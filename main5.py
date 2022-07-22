from kivy.app import App
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window


window_width=640
window_height=960
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', window_width)
Config.set('graphics', 'height', window_height)


class ImgShow(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            print('down')

    def on_touch_move(self, touch):
        print('move')
        self.width += .1

class MyApp(App):
    def build(self):
        #Window.clearcolor = (1, 1, 1, 1)
        parent = Widget()
        self.dadada = ImgShow()
        parent.add_widget(self.dadada)
        gl = GridLayout(rows=2, spacing=3, size_hint=(None, None), size=[window_width, window_height])
        bl_up = BoxLayout(orientation='vertical')
        bl_up.add_widget(Button(text='dada', on_press=self.click_button))
        bl_down = BoxLayout(orientation='vertical')
        bl_down.add_widget(Button(text='dad2a', on_press=self.click_button))
        gl.add_widget(bl_up)
        gl.add_widget(bl_down)
        parent.add_widget(gl)
        return parent


    def click_button(self, i):
        print('dada')


if __name__ == '__main__':
    MyApp().run()


  #      self.img = Image(source='mytopkid-labirint-4-5-38.jpg', size_hint=(1, .5),
                         # pos_hint={'center_x': .5, 'center_y': .5})