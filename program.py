from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import (Ellipse,Line,Color)
from kivy.core.window import Window
from random import random
class PainterWidget(Widget):
    def on_touch_down(self,touch):
        with self.canvas:
            Color(random(),random(),random(),1)
            Ellipse(pos = (touch.x-10,touch.y-10),size = (20,20))
            touch.ud['line'] = Line(points =(touch.x,touch.y),width = 10)
    def on_touch_move(self,touch):
        touch.ud['line'].points += (touch.x,touch.y)

class MyApp(App):
    def build(self):
        parent = Widget()
        self.painter = PainterWidget()
        bt = Button(text = "Clear",on_press = self.clear,size_hint = (.01,.01))
        sv = Button(text = 'Save', on_press = self.save, size_hint = (.01,.01),pos =(200,0))
        parent.add_widget(bt)
        parent.add_widget(self.painter)
        parent.add_widget(sv)
        return parent
    def clear(self,instance):
        self.painter.canvas.clear()
    def save(self,instance):
        self.painter.size = (Window.size[0],Window.size[1])
        self.painter.export_to_png('image.png')
if __name__ == "__main__":
    MyApp().run()
