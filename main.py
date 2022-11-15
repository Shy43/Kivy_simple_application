# only layout is here.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class BoxlayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text='1')
        b2 = Button(text='2')
        self.add_widget(b1)
        self.add_widget(b2)



class MainWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.collide_point(100 ,200)
        self.on_size()
        
    def on_size(self, *args):
        # print(self.height)
        # print(self.width)
        pass




class MainApp(App):
    def build(self):
        # return MainWidget()
        pass


o1 = MainApp()
o1.run()

