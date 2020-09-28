from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager


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
                    source: "myimg.png"
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
