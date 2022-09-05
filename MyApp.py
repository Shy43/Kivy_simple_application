import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle

class Show(Widget):
	def __init__(self, **kwargs):
		super(Show, self).__init__(**kwargs)
	
	def on_size(self, *args):
		pass
	
	def draw_square(self):
		with self.canvas:
			rect = Rectangle(size=(500, 500))

class Myapp(App):
	def build(self):
		return Show()
	
if __name__ == "__main__":	
	Myapp().run()

# square at the center of the screen
# useing kivy 2.0.0
