import random
from kivymd.app import MDApp
from kivy.properties import StringProperty, ObjectProperty, get_color_from_hex
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel


class MultiApp(MDApp):
    btn1 = ObjectProperty()
    btn2 = ObjectProperty()
    btn3 = ObjectProperty()
    btn4 = ObjectProperty()
    btn5 = ObjectProperty()
    btn6 = ObjectProperty()


    def add_button(self, g2):
        self.list = [str(self.right_answer),
                str(random.randint(1, 99)),
                str(random.randint(1, 99)),
                str(random.randint(1, 99)),
                str(random.randint(1, 99)),
                str(random.randint(1, 99))]
        random.shuffle(self.list)
        self.answer = self.list[0]
        btn1 = (Button(text=self.answer, font_size=40, on_press=self.new_example, padding=5))
        g2.add_widget(btn1)
        self.answer = self.list[1]
        btn2 = (Button(text=self.answer, font_size=40, on_press=self.new_example))
        g2.add_widget(btn2)
        self.answer = self.list[2]
        btn3 = (Button(text=self.answer, font_size=40, on_press=self.new_example))
        g2.add_widget(btn3)
        self.answer = self.list[3]
        btn4 = (Button(text=self.answer, font_size=40, on_press=self.new_example))
        g2.add_widget(btn4)
        self.answer = self.list[4]
        btn5 = (Button(text=self.answer, font_size=40, on_press=self.new_example))
        g2.add_widget(btn5)
        self.answer = self.list[5]
        btn6 = (Button(text=self.answer, font_size=40, on_press=self.new_example))
        g2.add_widget(btn6)
        return g2

    def new_example(self, button):
        if button.text == self.right_answer:
            self.count = self.count + 1
        else:
            self.count = self.count - 50
        button.parent.parent.children[2].text = 'Очки: ' + str(self.count)
        cube = random.randint(0, 5)
        if cube == 0:
            a = random.randint(1, 9)
            b = random.randint(1, 9)
        else:
            a = random.randint(4, 9)
            b = random.randint(4, 9)
        self.right_answer = str(a * b)
        for i in range(0, len(button.parent.children)):
            button.parent.children[i].text = str(random.randint(1, 9)) + str(random.randint(1, 9))
        button.parent.parent.children[1].text = str(a) + ' * ' + str(b) + ' = '
        rand = random.randint(0, 5)
        button.parent.children[rand].text = str(a * b)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        g1 = MDGridLayout(rows=3, md_bg_color=self.theme_cls.bg_normal)
        self.count = 0
        g1.add_widget(MDLabel(text='Очки: ' + str(self.count),
                              size_hint=[1, 0.3],
                              halign="center",
                              font_style='H3'))
        self.a = random.randint(1, 9)
        self.b = random.randint(1, 9)
        self.right_answer = str(self.a * self.b)
        print(self.right_answer)
        g1.add_widget(MDLabel(text=str(self.a) + ' * ' + str(self.b) + ' = ',
                              halign="center",
                              theme_text_color="Custom",
                              text_color=[1, 0, 0, 1],

                              font_style='H1'))
        g2 = MDGridLayout(cols=3, rows=3)
        self.add_button(g2)
        g1.add_widget(g2)
        return g1


if __name__ == "__main__":
    MultiApp().run()