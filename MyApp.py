import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class Show(Widget):
	def __init__(self, **kwargs):
		super(Show, self).__init__(**kwargs)



class Myapp(App):
	def build(self):
		return Show()
if __name__ == "__main__":	
	Myapp().run()
