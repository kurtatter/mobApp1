from random import randint

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (320, 240)
Window.clearcolor = (255 / 255, 186 / 255, 3 / 255, 1)
Window.title = 'Конвертер'


class MyApp(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text="Введите километры")
        self.miles = Label(text='Мили: 0')
        self.metres = Label(text='Метры: 0')
        self.sm = Label(text='Сантиметры: 0')
        self.input_data = TextInput(hint_text='Введите значение (км)', multiline=False)

    def btn_press(self, *args):
        self.label.color = (randint(0, 255)/255, randint(0,255)/255, randint(0,255)/255, 1)

    def build(self):
        box = BoxLayout(orientation='vertical')
        btn = Button(text="Click!")
        btn.bind(on_press=self.btn_press)
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.miles)
        box.add_widget(self.metres)
        box.add_widget(self.sm)
        self.input_data.bind(text=self.on_text)

        return box

    def on_text(self, *args):
        data = self.input_data.text
        if data.isnumeric():
            self.miles.text = 'Мили: ' + str(float(data) * 0.62)
            self.metres.text = 'Метры: ' + str(float(data) * 1000)
            self.sm.text = 'Сантиметры: ' + str(float(data) * 100000)
        else:
            self.input_data.text = ''
            self.miles.text = 'Мили: 0'
            self.metres.text = 'Метры: 0'
            self.sm.text = 'Сантиметры: 0'


if __name__ == '__main__':
    MyApp().run()
