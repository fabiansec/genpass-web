import reflex as rx
import string
import random
import pyperclip  # Asegúrate de tener esta librería instalada

class PageState(rx.State):
    # Estados de la aplicación
    longitud: int = 0  # Longitud de la contraseña por defecto
    contrasena: str = ""  # Contraseña generada
    mensaje: str = ""  # Mensaje de éxito o error
    boton_aceptar_disabled: bool = False  # Estado que controla si el botón está deshabilitado

    def generar_contrasena(self):
        """Genera una contraseña segura según la longitud especificada."""
        try:
            if self.longitud <= 0:
                self.mensaje = "La longitud debe ser mayor que 0."
                return

            caracteres = string.ascii_letters + string.digits + string.punctuation + "ñÑ"
            self.contrasena = "".join(random.choice(caracteres) for _ in range(self.longitud))
            self.mensaje = ""  # Limpia cualquier mensaje previo
        except ValueError:
            self.mensaje = "Por favor, ingresa un número válido para la longitud."

    def copiar_contrasena(self):
        """Copia la contraseña generada al portapapeles."""
        if self.contrasena:
            try:
                pyperclip.copy(self.contrasena)  # Copia al portapapeles
                self.mensaje = "¡Contraseña copiada con éxito!"
            except Exception as e:
                self.mensaje = f"Error al copiar: {e}"
        else:
            self.mensaje = "No hay ninguna contraseña para copiar."

    def set_longitud(self, value: str):
        """Establece la longitud de la contraseña con validaciones y controla el estado del botón."""
        try:
            # Convertimos el valor de 'value' de str a int
            value = int(value)
            
            if value <= 0:
                self.mensaje = "Debe ser mayor que 0."
                self.boton_aceptar_disabled = True  # Deshabilitar el botón
            elif value < 20:
                self.mensaje = "Debe ser de al menos 20 caracteres."
                self.boton_aceptar_disabled = True  # Deshabilitar el botón
            else:
                self.longitud = value
                self.mensaje = ""  # Limpiamos cualquier mensaje previo
                self.boton_aceptar_disabled = False  # Habilitar el botón
        except ValueError:
            self.mensaje = "Ingresa un número válido para la longitud."
            self.boton_aceptar_disabled = True  # Deshabilitar el botón

