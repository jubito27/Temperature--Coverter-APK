from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDIconButton

class Temeratureapp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Amber"

        self.screen = MDScreen()

        self.layout = MDBoxLayout(
            orientation="vertical",
            padding="10dp",
            spacing="20dp",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.8, 0.8)
        )

        self.gridlayout = MDGridLayout(cols=4 , spacing=80 ,padding = 110 , size_hint_y = 0.6 , )

        self.label = MDLabel(
            text= "Temperature Converter",
            halign="center",
            font_style="H4",
            pos_hint = {"center_y":0.8},
            theme_text_color="Primary",
            text_color=(1, 1, 1, 1),
            size_hint_y=0.1,
            height="100dp"
        )

        self.desc_button = MDIconButton(
            icon="information",
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            size_hint=(None, None),
            text="You can convert temperature from one unit to another. For example, Celcius to Fehrenheit, Fehrenheit to Kelvin etc.\nonly give input in one field and select the unit from the dropdown menu.You will get the output in the other field.\nClick on the text (Celcius or Fehrenhiet on left of text box) to change temperature Unit. ",
            halign="center",
            font_style="Subtitle1",
            theme_text_color="Secondary",
            size_hint_y=None,
            height="10dp"
        )

        self.desc_button.bind(on_release=lambda x: self.show_dialog("Description", self.desc_button.text))


        self.temp_options = [
            {"text": "Celcius"}, 
            {"text": "Fehrenheit"},
            {"text": "Kelvin"}
        ]
        self.temp_list = ["Celcius" , "Fehrenheit" , "Kelvin"]

        print(self.temp_list[0])
        print(self.temp_list[1])
        print(self.temp_list[2])

        
        self.textfield1 = MDTextField(

            hint_text="Enter Your value",
            mode="rectangle",
            size_hint_x=0.5,
            halign = "left",
            pos_hint={"center_x": 0.3 ,"center_y":0.5},
            background_color = "red",
            font_size = 20
        )
        self.flatbutton1 = MDFlatButton(
            text="Celcius",
            pos_hint={"center_x": 0.3 , "center_y":0.5},
            size_hint_x=0.5,
        )
        self.temp_menu1 = MDDropdownMenu(
            caller=self.flatbutton1 ,
            items=[
                {
                    "text": item["text"],
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=item["text"]: self.set_temp1(x),
                } for item in self.temp_options
            ],
            width_mult=3
        )
        self.flatbutton1.bind(on_release = lambda *args: self.temp_menu1.open())
        

        self.textfield2 = MDTextField(
            hint_text="your output",
            mode="rectangle",
            size_hint_x=0.5,
            halign = "left",
            pos_hint={"center_x": 0.5 ,"center_y":0.5},
            font_size = 20
        )

        self.flatbutton2 = MDFlatButton(
            text="Fehrenheit",
            pos_hint={"center_x": 0.6 , "center_y":0.5},
            size_hint_x=0.5
        )
        self.temp_menu2 = MDDropdownMenu(
            caller=self.flatbutton2,
            items=[
                {
                    "text": item["text"],
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=item["text"]: self.set_temp2(x),
                } for item in self.temp_options
            ],
            width_mult=3
        )

        self.flatbutton2.bind(on_release = lambda *args: self.temp_menu2.open())


        self.button = MDRaisedButton(
            text="Convert",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
            md_bg_color=self.theme_cls.primary_color,
            on_release = self.temperature_converter,
            #on_press = lambda x : print(p , type(t))
        )
        #self.button.bind(on_release=self.hell)

        # if self.flatbutton1.text==self.temp_list[0]:
        #     print("True")
        # else:
        #     print("False")

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.desc_button)
        self.gridlayout.add_widget(self.textfield1)
        self.gridlayout.add_widget(self.flatbutton1)
        self.gridlayout.add_widget(self.textfield2)
        self.gridlayout.add_widget(self.flatbutton2)
        self.screen.add_widget(self.gridlayout)
        self.layout.add_widget(self.button)
        
        
        self.screen.add_widget(self.layout)
        return self.screen
    
    def set_temp1(self, temp_text):
        self.selected_temp = temp_text
        self.flatbutton1.text = f"{temp_text}"
        self.temp_menu1.dismiss()

    def set_temp2(self, temp_text):
        self.selected_temp = temp_text
        self.flatbutton2.text = f"{temp_text}"
        self.temp_menu2.dismiss()

    def temperature_converter(self , instance):
        try:
            txt1 = self.textfield1.text
            txt = txt1.isdigit()
            for i in range(len(self.temp_list)):
                for j in range(len(self.temp_list)):
                    if not txt1:
                        self.show_dialog("Error", "Please enter a Value.")
                        return
                    else:
                        if txt:
                            txt1 = float(txt1)
                            if self.flatbutton1.text == self.temp_list[i] and self.flatbutton2.text==self.temp_list[j]:
                                if i == 0 and j == 0 :
                                    txt1 = str(txt1)
                                    tt1 = f"{txt1} Celcius"
                                    self.textfield2.set_text(text=tt1 , instance_text_field="hii")

                                if i == 0 and j == 1 :
                                    txt2 = (txt1 * 9/5) + 32
                                    txt2 = round(txt2, 2)
                                    
                                    txt2 = str(txt2)
                                    tt2 = f"{txt2} Fehrenheit"
                                        
                                    self.textfield2.set_text(text=tt2 , instance_text_field="hii")
                                    

                                if i == 0 and j == 2 :
                                

                                    txt3 = txt1 + 273
                                    txt3 = round(txt3, 2)
                                    txt3 = str(txt3 )
                                    tt3 = f"{txt3} Kelvin"
                                    self.textfield2.set_text(text=tt3 , instance_text_field="hii")
                                    
                                        
                                if i == 1 and j == 0 :
                                    txt4 = (txt1 - 32) * 5/9
                                    txt4 = round(txt4, 2)
                                    txt4 = str(txt4 )
                                    tt4 = f"{txt4} Celcius"
                                    self.textfield2.set_text(text=tt4 , instance_text_field="hii")

                                if i == 1 and j == 1 :
                                    txt1 = str(txt1)
                                    tt1 = f"{txt1} Fehrenheit"
                                    self.textfield2.set_text(text=tt1 , instance_text_field="hii")

                                if i == 1 and j == 2 :
                                    txt5 = (txt1 - 32) * 5/9 + 273
                                    txt5 = round(txt5, 2)
                                    txt5 = str(txt5)
                                    ttt5 = f"{txt5} Kelvin"
                                    self.textfield2.set_text(text=ttt5 , instance_text_field="hii")

                                if i == 2 and j == 0 :
                                    txt6 = txt1 - 273
                                    txt6 = round(txt6, 2)
                                    txt6 = str(txt6)
                                    tt6 = f"{txt6} Celcius"
                                    self.textfield2.set_text(text=tt6 , instance_text_field="hii")

                                if i == 2 and j == 1 :
                                    txt7 = (txt1 - 273) * 9/5 + 32
                                    txt7 = round(txt7, 2)
                                    txt7 = str(txt7)
                                    tt7 = f"{txt7} Fehrenheit"
                                    self.textfield2.set_text(text=tt7 , instance_text_field="hii")

                                if i == 2 and j == 2 :
                                    txt1 = str(txt1 )
                                    tt1 = f"{txt1} Kelvin"
                                    self.textfield2.set_text(text=tt1 , instance_text_field="hii")
                        else:
                            self.show_dialog("Error", "Please enter a valid number like a Integer.")
        except Exception as e:
            self.show_dialog("Error" , f"Error Occured\n{e}")    
            print(e)                
                        
                        
                        

    def show_dialog(self, title, text):
        self.dialog = MDDialog(
            title=title,
            text=text,
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: self.dialog.dismiss()
                )
            ]
        )
        self.dialog.open()

    
    

if __name__ == "__main__":
    Temeratureapp().run()
