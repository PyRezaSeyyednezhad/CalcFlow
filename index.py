from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
import math

Window.size = (500, 700)
Config.set('graphics', 'resizable', False)
Builder.load_file("./kivyfile.kv")

class MyLayout(Widget):
    calculationText = ""
    def percent(self):
        if self.ids.calc_input.text in ["Syntax Error", "Zero Division Error", "Empty"]:
            self.ids.calc_input.text = ""
        elif self.ids.calc_input.text == "":
            self.ids.calc_input.text = "0"
        else:
            getuserInput = float(self.ids.calc_input.text)
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = str(getuserInput/100)
    
    def clear(self):
        self.ids.calc_input.text = ""
    
    def delete(self):
        if self.ids.calc_input.text in ["Syntax Error", "Zero Division Error", "Empty"]:
            self.ids.calc_input.text = ""
        elif self.ids.calc_input.text == "":
            self.ids.calc_input.text = ""
        else:
            getuserInput = self.ids.calc_input.text
            listCreate = list(getuserInput)
            newListCreate = listCreate[:-1]
            res = ''.join(newListCreate)
            self.ids.calc_input.text = res
    
    def para(self):
        prier = self.ids.calc_input.text
        if prier in ["Syntax Error", "Zero Division Error", "Empty"]:
            self.ids.calc_input.text = ""
            self.ids.calc_input.text += "("
        else:
            if prier.count("(") == prier.count(")"):
                self.ids.calc_input.text += "("
            elif prier.count("(") > prier.count(")"):
                self.ids.calc_input.text += ")"
            else:
                pass
    
    def add_number_to_input(self, num):
        if self.ids.calc_input.text in ["Syntax Error", "Zero Division Error", "Empty"]:
            self.ids.calc_input.text = ""
            self.ids.calc_input.text += str(num)
        else:
            self.ids.calc_input.text += str(num)
        
            
    def dot(self):
        prier = self.ids.calc_input.text
        if prier in ["Syntax Error", "Zero Division Error", "Empty"]:
            self.ids.calc_input.text = "0"
            self.ids.calc_input.text += "."
        else:
            self.ids.calc_input.text += "."
    
    def pm(self):
        if self.ids.calc_input.text in ["Syntax Error", "Zero Division Error", "Empty"]:
            self.ids.calc_input.text = ""
            self.ids.calc_input.text += "-"
        elif self.ids.calc_input.text == "":
            self.ids.calc_input.text += "-"
        else:
            if self.ids.calc_input.text[-1] == "-":
                getuserInput = self.ids.calc_input.text
                listCreate = list(getuserInput)
                newListCreate = listCreate[:-1]
                res = ''.join(newListCreate)
                self.ids.calc_input.text = f"{res}+"
            elif self.ids.calc_input.text[-1] == "+":
                getuserInput = self.ids.calc_input.text
                listCreate = list(getuserInput)
                newListCreate = listCreate[:-1]
                res = ''.join(newListCreate)
                self.ids.calc_input.text = f"{res}-"
            else:
                self.ids.calc_input.text += "-"
    
    def math_operator(self, sign):
        if self.ids.calc_input.text in ["Syntax Error", "Zero Division Error", "Empty"]:
            self.ids.calc_input.text = ""
            self.ids.calc_input.text += sign
            
        elif self.ids.calc_input.text[-1] in ["*","+","-","/","("]:
            getuserInput = self.ids.calc_input.text
            listCreate = list(getuserInput)
            newListCreate = listCreate[:-1]
            res = ''.join(newListCreate)
            self.ids.calc_input.text = f"{res}{sign}"
        else:
            self.ids.calc_input.text += sign

    def Number_Ordinal_Number(self):
        try:
            prier = self.ids.calc_input.text
            if prier in ["Syntax Error", "Zero Division Error", "Empty"]:
                self.ids.calc_input.text = ""
                self.ids.calc_input.text = "Syntax Error"
                
            elif prier[-1] in ["*","+","-","/"]:
                getuserInput = self.ids.calc_input.text
                listCreate = list(getuserInput)
                newListCreate = listCreate[:-1]
                res = ''.join(newListCreate)
                self.ids.calc_input.text = str(1/float(res))
            else:
                self.ids.calc_input.text = str(1/float(prier))
        except:
            self.ids.calc_input.text = "Syntax Error"
            
    def squared(self):
        try:
            prier = self.ids.calc_input.text
            if prier in ["Syntax Error", "Zero Division Error", "Empty"]:
                self.ids.calc_input.text = ""
                self.ids.calc_input.text = "Syntax Error"
                
            elif prier[-1] in ["*","+","-","/"]:
                getuserInput = self.ids.calc_input.text
                listCreate = list(getuserInput)
                newListCreate = listCreate[:-1]
                res = ''.join(newListCreate)
                self.ids.calc_input.text = str(math.pow(float(res),2))
            else:
                self.ids.calc_input.text = str(math.pow(float(prier),2))
        except:
            self.ids.calc_input.text = "Syntax Error"
            
    
    def square_root_x(self):
        try:
            prier = self.ids.calc_input.text
            if prier in ["Syntax Error", "Zero Division Error", "Empty"]:
                self.ids.calc_input.text = ""
                self.ids.calc_input.text = "Syntax Error"
                
            elif prier[-1] in ["*","+","-","/"]:
                getuserInput = self.ids.calc_input.text
                listCreate = list(getuserInput)
                newListCreate = listCreate[:-1]
                res = ''.join(newListCreate)
                self.ids.calc_input.text = str(math.sqrt(float(res)))
            else:
                self.ids.calc_input.text = str(math.sqrt(float(prier)))
        except:
            self.ids.calc_input.text = "Syntax Error"
    
    def equal(self):
        getCalculationText = self.ids.calc_input.text
        if getCalculationText == "":
            self.ids.calc_input.text = "Empty"
        else:
            try:
                result = eval(self.ids.calc_input.text)
            except ZeroDivisionError:
                self.ids.calc_input.text = "Zero Division Error"
            except:
                self.ids.calc_input.text = "Syntax Error"
            else:
                self.ids.calc_input.text = str(result)
    
            
class RexidorCalculator(App):
    def build(self):
        Config.set('graphics', 'resizable', False)
        self.title = "Rexidor Simple Calculator"
        self.icon = "./rexidor_icon.ico"
        Window.clearcolor = (237/255, 244/255, 194/255,)
        return MyLayout()


if __name__ == '__main__':
    RexidorCalculator().run()
