# Importamos las bibliotecas necesarias de Kivy y KivyMD
from kivy.lang import Builder
from kivymd.app import MDApp

# Se define el código del formulario usando el lenguaje de marcado Kivy
formulario_kv = '''
BoxLayout:
    orientation: 'vertical'

    # Etiqueta para indicar al usuario que ingrese una imagen
    MDLabel:
        text: 'Ingrese una imagen:'
        halign: 'center'
        font_style: 'Subtitle1'
        
    # Campo de entrada para el nombre del archivo de imagen
    MDTextField:
        id: imagen_input
        hint_text: "Nombre de la imagen"
        multiline: False
        max_text_length: 30
    
    MDFlatButton:
        text: 'Cargar imagen'
        on_release: app.cargar_imagen()

    # Vista previa de la imagen cargada
    Image:
        id: imagen_preview
        source: ''
'''

# Se crea la clase de la aplicación
class FormularioApp(MDApp):

    # Método para cargar una imagen
    def cargar_imagen(self):
        # Se obtiene el nombre del archivo ingresado por el usuario
        nombre_imagen = self.root.ids.imagen_input.text

        # Se carga la imagen y se actualiza la vista previa
        if nombre_imagen:
            ruta_imagen = nombre_imagen + '.jpg'  # Suponiendo que es una imagen PNG
            self.root.ids.imagen_preview.source = ruta_imagen
        else:
            self.root.ids.imagen_preview.source = ''

    def build(self):
        return Builder.load_string(formulario_kv)

# Se ejecuta la aplicación

FormularioApp().run()