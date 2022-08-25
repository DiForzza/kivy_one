import random
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivy.uix.button import Button

from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel


class MultiApp(MDApp):
    btn1 = ObjectProperty()
    btn2 = ObjectProperty()
    btn3 = ObjectProperty()
    btn4 = ObjectProperty()
    btn5 = ObjectProperty()
    btn6 = ObjectProperty()
    count_different_answers = []
    list_answers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27, 28, 30, 32, 35, 36, 40,
                    42, 45, 48, 49, 54, 56, 63, 64, 72, 81]

    def add_button(self, g2):
        self.list = [self.multiplication_answers(),
                     self.multiplication_answers(),
                     self.multiplication_answers(),
                     self.multiplication_answers(),
                     self.multiplication_answers(),
                     self.multiplication_answers()]
        self.list[0] = str(self.right_answer)
        random.shuffle(self.list)
        self.answer = self.list[0]
        btn1 = (Button(text=self.answer, font_size=40, on_press=self.new_example))
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

    def multiplication_answers(self):
        rand = random.randint(0, 35)
        while rand in self.count_different_answers or self.list_answers[rand] == self.right_answer:
            rand = random.randint(0, 35)
        self.count_different_answers.append(rand)
        if len(self.count_different_answers) > 6:
            self.count_different_answers.clear()
            self.count_different_answers.append(rand)
        return str(self.list_answers[rand])

    def new_example(self, button):
        if button.text == self.right_answer:
            self.count = self.count + 1
        else:
            self.count = self.count - 50
        button.parent.parent.children[2].text = 'Очки: ' + str(self.count)
        choose_mult_or_division = random.randint(0, 1)
        if choose_mult_or_division == 0:
            # УМНОЖЕНИЕ
            cube = random.randint(0, 5)
            if cube == 0:
                a = random.randint(1, 9)
                b = random.randint(1, 9)
            else:
                a = random.randint(4, 9)
                b = random.randint(4, 9)
            self.right_answer = str(a * b)
            for i in range(0, len(button.parent.children)):
                button.parent.children[i].text = self.multiplication_answers()
            button.parent.parent.children[1].text = str(a) + ' * ' + str(b) + ' = '
            rand = random.randint(0, 5)
            button.parent.children[rand].text = str(a * b)
            button.parent.parent.md_bg_color = [1, 0, 1, 0]
        else:
            # ДЕЛЕНИЕ
            strength = random.randint(0, 5)
            if strength == 0:
                rand = random.randint(0, 35)
                b = random.randint(1, 9)
            else:
                rand = random.randint(15, 35)
                b = random.randint(1, 9)
            self.right_answer = (self.list_answers[rand]) / b
            while (self.list_answers[rand]) % b != 0 or self.right_answer >= 10:
                b = random.randint(1, 9)
                self.right_answer = (self.list_answers[rand]) / b
            button.parent.parent.children[1].text = str(self.list_answers[rand]) + ' / ' + str(b) + ' = '
            l = list(range(1, 9))
            random.shuffle(l)
            self.right_answer = int(self.right_answer)
            for i in range(0, len(button.parent.children)):
                button.parent.children[i].text = str(l[i])
            rand = random.randint(0, 5)
            button.parent.children[rand].text = str(self.right_answer)
            button.parent.parent.md_bg_color = [1, 1, 0, 1]

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
