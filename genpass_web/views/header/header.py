import reflex as rx

def header() -> rx.Component:
    return rx.vstack(  
        rx.text(
            "Generador de Contraseñas",    
            font_weight="bold",          
            color="white",               
            size="9",                   
            margin_bottom="20px",       
            align="center",              
            as_="p"    
        ) ,   
        rx.avatar(src="https://avatars.githubusercontent.com/u/152921785?s=400&u=41d4d91146dc3f79c5689f5cdde88f0c934a3f85&v=4",
                  size="5",
                  radius="full"  
                  
        ),
        rx.link(
                "@fabiansec",
                href="https://github.com/fabiansec",
                color="white",
                opacity=0.6,
                 _hover={"color":"white"},
                 underline="none"
                
                
        ) ,   
        width="100%",  
        height="100%", 
        justify="center", 
        align="center",    
        padding_y="20px"
    )
    