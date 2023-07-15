from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel

class ImageForm(BoxLayout):
    def __init__(self, **kwargs):
        super(ImageForm, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = [10, 10, 10, 10]

        self.img_container = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, 0.8))
        self.add_widget(self.img_container)

        self.img_btn = MDRaisedButton(text="Select Image", on_release=self.open_file_manager)
        self.add_widget(self.img_btn)

    def open_file_manager(self, *args):
        file_manager = MDFileManager(
            select_path=self.select_path,
            ext=['.png', '.jpg', '.jpeg']
        )
        file_manager.show('/')

    def exit_file_manager(self, *args):
        self.file_manager.close()

    def select_path(self, path):
        self.exit_file_manager()
        self.display_image(path)

    def display_image(self, path):
        self.img_container.clear_widgets()
        image = Image(source=path, size=(300, 300))
        self.img_container.add_widget(image)

class App(MDApp):
    def build(self):
        return ImageForm()


App().run()