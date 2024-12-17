import reflex as rx
from genpass_web.state.PageState import PageState  # Importa el estado donde está la lógica

def cuerpo() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text(
                "Introduce la longitud de la contraseña",
                color="white",
                opacity=0.9,
                size="4",
                as_="label",
                margin_bottom="20px",
                width="100%",
                text_align="center"
            ),
            # Campo para ingresar la longitud
            rx.input(
                bg="white",
                type="number",
                width="100%",
                max_width="500px",
                min_width="200px",
                margin_top="20px",
                padding="5px",
                border_radius="8px",
                color="black",
                value=PageState.longitud,  # Conecta con el estado
                on_change=lambda e: PageState.set_longitud(e),  # Actualiza la longitud con el valor del evento

            ),
            # Botón para generar la contraseña
            rx.button(
                "Aceptar",
                bg="blue",
                color="white",
                padding="12px 24px",
                border_radius="8px",
                width="100%",
                max_width="500px",
                min_width="200px",
                margin_top="20px",
                margin_left="auto",
                margin_right="auto",
                on_click=PageState.generar_contrasena,  # Llama al método para generar la contraseña
                disabled=PageState.boton_aceptar_disabled,
                
            ),
            # Campo para mostrar la contraseña generada
            rx.box(
                rx.input(
                    value=PageState.contrasena,  # Conecta al estado de la contraseña
                    placeholder="Contraseña generada...",
                    color="black",
                    type="text",
                    disabled=True,
                    width="100%",
                    max_width="500px",
                    min_width="200px",
                    border_radius="8px",
                    margin_top="20px",
                ),
                # Botón para copiar la contraseña
                rx.button(
                    rx.icon(
                        "copy",
                        size=18,
                        color=rx.color("indigo", 11)
                    ),
                    background="transparent",  # Sin fondo para que solo se vea el ícono
                    border="none",  # Sin borde
                    padding="0",  # Sin relleno
                    position="absolute",  # Posicionar el ícono dentro del input
                    right="-25px",  # Alinearlo a la derecha del campo de entrada
                    top="50%",  # Centrado verticalmente
                    transform="translateY(-50%)",  # Ajuste de alineación vertical
                    on_click=PageState.copiar_contrasena,  # Llama al método para copiar
                    bg="#000"
                ),
                position="relative",  # Hace que el box contenedor del ícono sea relativo al input
                width="100%",
                max_width="500px",
                text_align="center"
            ),
            # Mensaje de éxito o error
            rx.text(
                PageState.mensaje,  # Conecta al mensaje del estado
                color=rx.cond(PageState.mensaje.contains("éxito"), "#4feed0", "#ee5d66"),
                size="3",
                margin_top="10px",
            ),
        ),
        width="100%",
        height="100%",
        justify="center",
        align="center",
        padding_y="20px"
    )
