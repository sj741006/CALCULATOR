from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

btnlist = [['(', ')', 'pi', '/'],
           ['7', '8', '9', '*'],
           ['4', '5', '6', '-'],
           ['1', '2', '3', '+'],
           ['C', '0', '.', '=']]

def onClick(textinput, btn):
    print("Clink Button:",btn.text)
    if(btn.text >= '0' and btn.text <= '9'):
        textinput.text += btn.text
    elif(btn.text in ['+', '-', '*', '/', '.', '(', ')']):
        textinput.text += btn.text
    elif(btn.text == 'C'):
        textinput.text = ''
    elif(btn.text == 'pi'):
        textinput.text += '*3.14'
    elif(btn.text == '='):
        try:
            textinput.text = str(eval(textinput.text))
        except:
            print("ERROR")
    
class MyApp(App):
    def build(self):
        self.title = "CALCULATOR"
        
        B = BoxLayout(orientation="vertical")
        T = TextInput(font_size=30, font_name='Tschichold Alt.ttf')
        B.add_widget(T)

        G = GridLayout(cols=4)
        for btnl in btnlist:
            for key in btnl:
                btn = Button(text=key, font_size=40, font_name='Tschichold Alt.ttf', background_color=[255,0,255,0])
                
                def cmd(btn = key):
                    onClick(T, btn)

                btn.bind(on_press=cmd)
                G.add_widget(btn)
        B.add_widget(G)
        return B
    
MyApp().run()
