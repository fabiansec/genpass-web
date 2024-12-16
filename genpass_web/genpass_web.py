
import reflex as rx
from genpass_web.views.header.header import header
from genpass_web.views.cuerpo.cuerpo import cuerpo
from rxconfig import config


class State(rx.State):
    pass

    


def index() -> rx.Component:
    return rx.vstack(
        header(),
        cuerpo(),
    
      rx.box(
    position="absolute",  # Posicionamiento absoluto
    top="0",              # Parte superior
    left="0",             # Parte izquierda
    z_index="-2",         # Z-index, detrás de otros elementos
    height="100vh",       # Altura completa de la ventana
    width="100vw",        # Ancho completo de la ventana
    background="radial-gradient(ellipse 80% 80% at 50% -20%, rgba(120,119,198,0.3), rgba(255,255,255,0))", 
    background_color="neutral-950"  # Color de fondo adicional (neutral 950)
    )

    )
    


app = rx.App()
app.add_page(index)
