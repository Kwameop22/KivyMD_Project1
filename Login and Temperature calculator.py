from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

KV='''
MDScreenManager:
    Login:
    WelcomeScreen:
<Login>:
    name:"Login"
    MDCard:
        orientation:"vertical"
        size_hint:.5,.8
        pos_hint:{"center_x":.5,"center_y":.5}
        padding:dp(30)
        spacing:dp(20)
        MDLabel:
            id:label
            text:"Login"
            halign:"center"
            bold:True
            font_size:dp(32)
        MDTextField:
            id:text1
            mode:"fill"
            hint_text:"Username"
            icon_right:"account"
     
    
        MDTextField:
            id:text2
            mode:"fill"
            hint_text:"Password"
            icon_right:"eye-off"
            password:True
        MDRaisedButton:
            id:button
            text:"Submit"
            size_hint_x:1
            on_release:app.button_click()
        MDLabel:
            id:label2
            text:""
            halign:"center"
            font_size:dp(15)
<WelcomeScreen>:
    name:"Welcome"
    
    
    
    MDBoxLayout:
        orientation:"vertical"
        
        
        MDLabel:
            pos_hint:{"top":1}
            size_hint_y:.3
            text:"WELCOME BACK"
            bold:True
            font_size:dp(32)
            halign:"center"
        MDTextField:
            id:value
            mode:"fill"
            size_hint_x:.8
            input_filter:"float"
            pos_hint:{"center_x":.5}
            halign:"left"
            hint_text:"Enter value"
        MDBoxLayout:
            size_hint:.6,.3
            spacing:dp(20)
            pos_hint:{"center_x":.5} 
            
                     
            MDRaisedButton:
                text:"To Celsius"
                pos_hint:{"top":.8}
                size_hint:.3,.4
                on_release:app.celsius()
            MDRaisedButton:
                text:"To Fahrenheit"  
                pos_hint:{"top":.8}
                size_hint:.3,.4
                on_release:app.fahrenheit()
            
        
        MDBoxLayout:
            orientation:"vertical"
            MDLabel:
                halign:"center"
                bold:True
                font_size:dp(32)
                id:message
                text:""
            
            MDRaisedButton:
                text:"Secure logout"
                pos_hint:{"center_x":.5}
                on_release:app.logout()
'''

class Login(MDScreen):
    pass

class WelcomeScreen(MDScreen):
    pass

class LoginScreen(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Pink"
        return Builder.load_string(KV)
    def celsius(self):
        try:
            login_screen=self.root.get_screen("Welcome")
            num = float(login_screen.ids.value.text)
            ans=login_screen.ids.message.text=f"{str(round((num - 32)/1.8,2))}°C"
            login_screen.ids.message.color=(0,1,0,1)

        except ValueError:
            login_screen.ids.message.text="Enter a value"
            login_screen.ids.message.color = (1, 0, 0, 1)


    def fahrenheit(self):
        try:
            login_screen=self.root.get_screen("Welcome")
            num = float(login_screen.ids.value.text)
            ans=login_screen.ids.message.text=f"{str(round((num*1.8)+32,2))}°F"
            login_screen.ids.message.color = (0, 0, 1, 1)
        except ValueError:
            login_screen.ids.message.text = "Enter a value"
            login_screen.ids.message.color = (1, 0, 0, 1)




    def logout(self):
        self.root.current="Login"
        login_screen = self.root.get_screen("Login")
        if self.root.current == "Login":

            login_screen.ids.text1.text= ""
            login_screen.ids.text2.text = ""
            login_screen.ids.label2.text = ""
    def button_click(self):
        login_screen = self.root.get_screen("Login")
        username = login_screen.ids.text1.text.strip().lower()
        password = login_screen.ids.text2.text

        if username =="admin" and password =="1234":
            login_screen.ids.label2.text ="Success"
            login_screen.ids.label2.color=(0,1,0,1)
            self.theme_cls.theme_style = "Dark"
            self.root.current = "Welcome"
            print("Access granted")
        elif username=="" and password == "":
            login_screen.ids.label2.text = "Enter Username or Password"
            login_screen.ids.label2.color = (1, 0, 0, 1)
            print("Access denied")
        else:
            login_screen.ids.label2.text = "Incorrect Username or Password"
            login_screen.ids.label2.color=(1,0,0,1)
            print("Access denied")



LoginScreen().run()