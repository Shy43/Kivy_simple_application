import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle

class Show(Widget):
	rect = None
	def __init__(self, **kwargs):
		super(Show, self).__init__(**kwargs)
		self.draw_rectangle()		

	def on_size(self, *args):
		self.update()
		

	def draw_rectangle(self):
		with self.canvas:
			self.rect = Rectangle(size=(100, 100), pos=(100, 100))

	def update(self):
		self.rect.pos = (self.width/2-50, self.height /2-50)
		# 50 is the half of the position of the rectangle size.
		# subtract from both height and width.
		
class Myapp(App):
	def build(self):
		return Show()

if __name__ == "__main__":	
	Myapp().run()

# square at the center of the screen
# useing kivy 2.0.0

