from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.properties import StringProperty, NumericProperty, BooleanProperty



class WidgetExample(GridLayout):
    my_text = StringProperty('1')
    text_input = StringProperty('Foo')
    count = 1
    count_enabled = BooleanProperty(False)
    # slider_value = StringProperty('Value')
    
    def on_button_click(self):
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)
            
    def on_toggle_state(self, widget):
        if widget.state == 'normal':
            widget.text = 'OFF'
            self.count_enabled = False
        else:
            widget.text = 'ON'
            self.count_enabled = True
            
    def on_switch_active(self, widget):
        print('Switch: ' + str(widget.active))
        
    def on_slider_value(self, widget):
        print('Slider: ' + str(int(widget.value)))
        # self.slider_value = str(int(widget.value))
        
    def on_text_validate(self, widget):
        self.text_input = widget.text


class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical '
        b1 = Button(text='A')
        b2 = Button(text='B')
        
        self.add_widget(b1)
        self.add_widget(b2)



class MainWidget(Widget):
    pass

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass


class CanvasExample3(Widget):
    pass



class TheLabApp(App):
    pass



TheLabApp().run()