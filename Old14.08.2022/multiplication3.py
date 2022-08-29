import random

from kivy.uix.switch import Switch
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from random import choice
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDSwitch


class MultiApp(MDApp):
    count_different_answers = []
    list_answers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27, 28, 30, 32, 35, 36, 40,
                    42, 45, 48, 49, 54, 56, 63, 64, 72, 81]

    def add_button(self, g2):
        self.multiplication_answers()
        btn1 = (Button(text=self.list[0], font_size=40, on_press=self.new_example))
        g2.add_widget(btn1)
        btn2 = (Button(text=self.list[1], font_size=40, on_press=self.new_example))
        g2.add_widget(btn2)
        btn3 = (Button(text=self.list[2], font_size=40, on_press=self.new_example))
        g2.add_widget(btn3)
        btn4 = (Button(text=self.list[3], font_size=40, on_press=self.new_example))
        g2.add_widget(btn4)
        btn5 = (Button(text=self.list[4], font_size=40, on_press=self.new_example))
        g2.add_widget(btn5)
        btn6 = (Button(text=self.list[5], font_size=40, on_press=self.new_example))
        g2.add_widget(btn6)
        return g2

    def multiplication_answers(self):
        random_choice = self.list_answers
        try:
            random_choice.remove(self.right_answer)
        except ValueError:
            pass
        random.shuffle(random_choice)
        random_choice.insert(0, self.right_answer)
        self.list = [str(random_choice[0]),
                     str(random_choice[1]),
                     str(random_choice[2]),
                     str(random_choice[3]),
                     str(random_choice[4]),
                     str(random_choice[5])]
        #self.list[0] = str(self.right_answer)
        random.shuffle(self.list)


    def new_example(self, button):
        if str(button.text) == str(self.right_answer):
            self.right_count = self.right_count + 1
            button.parent.parent.children[2].children[1].children[1].text = 'Правильных ответов: ' + str(self.right_count)
        else:
            self.not_right_count = self.not_right_count + 1
            button.parent.parent.children[2].children[1].children[0].text = 'Ошибок: ' + str(self.not_right_count)
        #print(button.parent.parent.children[2].children[1].children[0])
        print(button.parent.parent.children[2].children[0].children[0].active, 'вычитание')  # вычитание
        print(button.parent.parent.children[2].children[0].children[2].active, 'сложение')  # сложение
        print(button.parent.parent.children[2].children[0].children[4].active, 'деление')  # деление
        print(button.parent.parent.children[2].children[0].children[6].active, 'умножение')  # умножение
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
            self.right_answer = a * b
            self.multiplication_answers()
            for i in range(0, len(button.parent.children)):
                button.parent.children[i].text = self.list[i]
            button.parent.parent.children[1].text = str(a) + ' * ' + str(b) + ' = '
            #rand = random.randint(0, 5)
            #button.parent.children[rand].text = str(a * b)
            button.parent.parent.md_bg_color = [0, 0.65, 1, 1]
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
            self.right_answer = int(self.right_answer)
            l = list(range(1, 9))
            random.shuffle(l)
            number = 1
            not_in_list_number = 1
            for i in range(0, len(l)):
                number += 1
                if number not in l:
                    not_in_list_number = number
            for i in range(0, 6):
                if l[i] == self.right_answer:
                    l[i] = not_in_list_number
                button.parent.children[i].text = str(l[i])
            rand = random.randint(0, 5)
            button.parent.children[rand].text = str(self.right_answer)
            button.parent.parent.md_bg_color = [0, 0.9, 1, 1]
            #button.parent.parent.children[1].text_color = [1, 1, 0.5, 1]
            #print(button.parent.parent.children[1].text_color)

    def build(self):
        #self.theme_cls.theme_style = "Dark"
       # self.theme_cls.primary_palette = "Blue"
        g1 = MDGridLayout(rows=3, md_bg_color=self.theme_cls.bg_normal)
        self.right_count = 0
        self.not_right_count = 0
        #g1.add_widget(MDLabel(text='Очки: ' + str(self.count),
        #                      size_hint=[1, 0.3],
        #                      halign="center",
        #                      text_color=[1, 0, 0, 1],
        #                      font_style='H3'))
        g3 = MDGridLayout(cols=2, md_bg_color=self.theme_cls.bg_normal)
        g5 = MDGridLayout(rows=2, md_bg_color=self.theme_cls.bg_normal)
        g5.add_widget(MDLabel(text='Правильных ответов: ' + str(self.right_count),
                              size_hint=[1, 0.3],
                              halign="center",
                              text_color=[1, 0, 0, 1],
                              font_style='H4'))
        g5.add_widget(MDLabel(text='Ошибок: ' + str(self.not_right_count),
                              size_hint=[1, 0.3],
                              halign="center",
                              text_color=[1, 0, 0, 1],
                              font_style='H4'))
        g3.add_widget(g5)
        g4 = MDGridLayout(rows=4, cols=2, md_bg_color=self.theme_cls.bg_normal)
        g4.add_widget(MDLabel(text='Умножение', halign="center"))
        g4.add_widget(Switch(active=True))
        g4.add_widget(MDLabel(text='Деление', halign="center"))
        g4.add_widget(Switch(active=True))
        g4.add_widget(MDLabel(text='Сложение', halign="center"))
        g4.add_widget(Switch(active=False))
        g4.add_widget(MDLabel(text='Вычитание', halign="center"))
        g4.add_widget(Switch(active=False))
        g3.add_widget(g4)
        g1.add_widget(g3)
        #g1.add_widget(MDLabel(text='test'))
        self.a = random.randint(1, 9)
        self.b = random.randint(1, 9)
        self.right_answer = self.a * self.b
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
