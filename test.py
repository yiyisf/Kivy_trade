from time import strftime

import kivy
from kivy.core.text import LabelBase

kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.button import Label
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

# LabelBase.register(name='Roboto',
#     fn_regular='Roboto-Thin.ttf',
#     fn_bold='Roboto-Medium.ttf')

class HelloKivyApp(App):
    def build(self):
        # return Label(text="Hello Kivy")
        return Label()

class ClockApp(App):
     def update_time(self, nap):
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')
     def on_start(self):
        Clock.schedule_interval(self.update_time, 1)
# hello = HelloKivyApp()
# hello.run()

clock = ClockApp()
clock.run()
