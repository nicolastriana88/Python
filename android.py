from kivy.app import App
from kivy.uix.label import Label

class Simple_App(App):
    def build (self):
        return Label(text="Hello World")
    
Simple_App().run()