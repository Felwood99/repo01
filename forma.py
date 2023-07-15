# Importamos las bibliotecas necesarias de Kivy y KivyMD
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

# Se define el código de la aplicación usando el lenguaje de marcado Kivy
app_kv = '''
BoxLayout:
    orientation: 'vertical'

    MDTopAppBar:
        title: 'Seleccionar y Guardar Imagen'

    MDRaisedButton:
        text: 'Seleccionar imagen'
        on_release: app.show_file_manager()

    Image:
        id: imagen_preview
        source: ''

    MDRaisedButton:
        text: 'Guardar imagen'
        on_release: app.guardar_imagen()

'''


# Se crea la clase de la aplicación
class ImageApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path
        )

    # Método para mostrar el administrador de archivos
    def show_file_manager(self):
        self.file_manager.show('/')

    # Método llamado al seleccionar una ruta de archivo
    def select_path(self, path):
        # Actualizar la vista previa de la imagen
        self.root.ids.imagen_preview.source = path
        self.exit_file_manager()

    # Método para cerrar el administrador de archivos
    def exit_file_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    # Método para guardar la imagen seleccionada
    def guardar_imagen(self):
        # Verificar si se seleccionó una imagen
        if self.root.ids.imagen_preview.source:
            # Mostrar un cuadro de diálogo para confirmar la acción
            dialog = MDDialog(
                title="Guardar imagen",
                text="¿Está seguro de que desea guardar la imagen?",
                buttons=[
                    MDFlatButton(
                        #text="Cancelar", text_color=self.theme_cls.primary_color, on_release=dialog.dismiss
                    ),
                    MDFlatButton(
                        text="Guardar", text_color=self.theme_cls.primary_color, on_release=self.guardar_imagen_confirmado
                    ),
                ],
            )
            dialog.open()            

    # Método llamado al confirmar la acción de guardar la imagen
    def guardar_imagen_confirmado(self, *args):
        # Obtener la ruta de la imagen seleccionada
        ruta_imagen = self.root.ids.imagen_preview.source

        # Guardar la imagen en la ubicación deseada
        # Aquí puedes escribir tu código para guardar la imagen

        # Mostrar un mensaje para confirmar que se guardó la imagen
        self.root.ids.imagen_preview.source = ''
        dialog = MDDialog(
            title="Imagen guardada",
            text="La imagen ha sido guardada exitosamente.",
            buttons=[
                MDFlatButton(
                    #text="Cerrar", text_color=self.theme_cls.primary_color, on_release=dialog.dismiss
                )
            ],
        )
        dialog.open()
        print(ruta_imagen)

    def build(self):
        return Builder.load_string(app_kv)


# Se ejecuta la aplicación
if __name__ == '__main__':
    ImageApp().run()
