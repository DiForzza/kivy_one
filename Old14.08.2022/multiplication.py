import random
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout


def get_multiplication():
    a = random.randint(1, 9)
    return a


def answer_to_button(a, b):
    return StringProperty(str(get_multiplication()) + str(get_multiplication()))


class MultiplicationTable(GridLayout):
    text_tugriki = StringProperty('0')
    new_primer1 = StringProperty(None)

    a = get_multiplication()
    b = get_multiplication()
    first_primer = StringProperty(str(a) + '*' + str(b) + '=')
    right_answer = str(a * b)

    list = ['1', '2', '3', '4', '5', '6']
    random.shuffle(list)
    print(list)
    for i in range(0, 6):
        if i == 1:
            vars()["answer" + str(list[i])] = right_answer
        else:
            vars()["answer" + str(list[i])] = answer_to_button(a, b)

    def win_or_not(self, widget):
        global right_answer_i
        if widget.text == self.right_answer:
            self.text_tugriki = str(int(self.text_tugriki) + 1)
            a = get_multiplication()
            b = get_multiplication()
            self.first_primer = str(a) + '*' + str(b) + '='
            self.right_answer = str(a * b)
            print(self.right_answer)
            list = [self.right_answer,
                    str(get_multiplication()) + str(get_multiplication()),
                    str(get_multiplication()) + str(get_multiplication()),
                    str(get_multiplication()) + str(get_multiplication()),
                    str(get_multiplication()) + str(get_multiplication()),
                    str(get_multiplication()) + str(get_multiplication())]
            random.shuffle(list)
            for i in range(1, len(list)+1):
                print(i)
                if self.right_answer == list[i-1]:
                    right_answer_i = i
            if right_answer_i == 1:
                widget.text = str(get_multiplication()) + str(get_multiplication())
            else:
                self.answer1 = list[0]
            if right_answer_i == 2:
                widget.text = str(get_multiplication()) + str(get_multiplication())
            else:
                self.answer2 = list[1]
            if right_answer_i == 3:
                widget.text = str(get_multiplication()) + str(get_multiplication())
            else:
                self.answer3 = list[2]
            if right_answer_i == 4:
                widget.text = str(get_multiplication()) + str(get_multiplication())
            else:
                self.answer4 = list[3]
            if right_answer_i == 5:
                widget.text = str(get_multiplication()) + str(get_multiplication())
            else:
                self.answer5 = list[4]
            if right_answer_i == 6:
                widget.text = str(get_multiplication()) + str(get_multiplication())
            else:
                self.answer6 = list[5]
        else:
            self.text_tugriki = str(int(self.text_tugriki) - 5)


class MultiplicationApp(App):
    pass


if __name__ == "__main__":
    app = MultiplicationApp()
    app.run()
