import kivy
kivy.require('1.8.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from common import GraphicUnitTest
from kivy.graphics import Ellipse, Color

class VertexInstructionTestCase(GraphicUnitTest):
	def test_ellipse(self):
		r = self.render
		# create a root widget
		wid = Widget()
        # put some graphics instruction on it
		with wid.canvas: 
			Color(1, 1, 1)
			self.e = Ellipse(pos=(100, 100), size=(200, 100)) 
		# render, and capture it directly
		r(wid)
		# as alternative, you can capture in 2 frames:
		r(wid, 2)
        # or in 10 frames
		r(wid, 10)

class MyW(Widget):
	pass

class e2App(App):
				
	def build(self):
		return MyW()

if __name__ == '__main__':
	e2App().run()
