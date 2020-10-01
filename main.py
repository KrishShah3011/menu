from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.label import MDLabel
from kivy.uix.widget import Widget
from kivymd.uix.list import MDList, OneLineIconListItem
from kivy.uix.image import Image

navigation_helper = '''
Screen:
    NavigationLayout:
        ScreenManager:
            Screen :
                BoxLayout :
                    orientation : 'vertical'
                    MDToolbar:
                        title : 'Application'
                        left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 8
                    
                    Widget:
                        
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                spacing:'8dp'
                padding:'8dp'
                orientation : 'vertical'
                Image:
                    source: "IMG.png"
                MDLabel:
                    text: "    Krish Shah"
                    font_style: "Subtitle1"
                    size_hint_y:None
                    height:self.texture_size[1]
                MDLabel:
                    text: "     shahkrish3011@gmail.com"
                    font_style: "Caption"
                    size_hint_y:None
                    height:self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:"Profile"
                            IconLeftWidget:
                                icon:"face-profile"
                        OneLineIconListItem:
                            text:"Upload"
                            IconLeftWidget:
                                icon:"file-upload"
                        OneLineIconListItem:
                            text:"Logout"
                            IconLeftWidget:
                                icon:"logout"
                            
                                    
'''


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        screen = Builder.load_string(navigation_helper)
        return screen


DemoApp().run()
