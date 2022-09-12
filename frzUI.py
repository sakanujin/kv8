from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.togglebutton import ToggleButton # for toggle
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
################################################# 
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '480')
 
class Display(BoxLayout):
    pass
 
class Screen_One(Screen):
    pass
 
class Screen_Two(Screen):
    pass
 
#class SM02App(App):
#    def build(self):
#        return Display()

################################################
class Screen_AGI(Screen):
    renzokku = 1
    danzok   = 0

    def __init__(self, **kwargs):
        super(Screen_AGI, self).__init__(**kwargs)

    pass
################################################

class TextWidget(Screen):
    text1 = StringProperty()
    text2 = StringProperty()
    text3 = StringProperty()
    text4 = StringProperty()
    temp_now =   StringProperty()
    temp_set =   StringProperty()
    set_num  = 0   

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text1 = 'オフ'
        self.text2 = 'UP'
        self.text3 = 'DOWN'
        self.text4 = 'オフ'
        self.temp_now = str(25)
        self.temp_set = self.temp_now
        self.set_num  = int(self.temp_set)

    def buttonClicked(self):  

        if self.text4 == "オン":

            self.text4 = "オフ"
            print(self.text4)

        elif self.text4 == "オフ":
            self.text4 = "オン"
            print(self.text4)


    def btc2(self): #UP  
        self.set_num = self.set_num + 1
        self.temp_set  = str(self.set_num)

    def btc3(self):  
        self.set_num = self.set_num - 1
        self.temp_set  = str(self.set_num)

class TestApp(App):

    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'freezer UI/UX'

    def build(self):
        return TextWidget()


class SM02App(App):
    def build(self):
        return Display()

if __name__ == "__main__":
    #TestApp().run()
    SM02App().run()

