from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
# import sample
import facerecogfkivy
import os

class MyGrid (Widget):
    name1 = ObjectProperty(None)
    jumlah1 = ObjectProperty(None)

    def btn(self):
        print("Nama: ",self.name1.text)
        print("Jumlah: ",self.jumlah1.text)
        facerecogfkivy.main(self.name1.text,int(self.jumlah1.text))
        self.name1.text = ""
        self.jumlah1.text = ""
    
    def btn2(self):
        print("Nama: ",self.name1.text)
        print("Jumlah: ",self.jumlah1.text)
        facerecogfkivy.main2(self.name1.text,int(self.jumlah1.text))
        self.name1.text = ""
        self.jumlah1.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()



MyApp().run()
