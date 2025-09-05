import customtkinter as ctk

def criar_janela(titulo="Janela", largura=400, altura=500, tema="dark", cor="blue"):
    # aplicar tema e cor
    ctk.set_appearance_mode(tema)
    ctk.set_default_color_theme(cor)

    # criar janela
    app = ctk.CTk()
    app.title(titulo)
    app.geometry(f"{largura}x{altura}")

    return app
def criar_botao(master, texto, comando=None, icone=None):
    return ctk.CTkButton(
        master=master,
        text=texto,
        image=icone,
        command=comando,
        font=("Arial", 18, "bold"),
        width=220,
        height=40,
        corner_radius=15,
        fg_color="#E2952D",
        hover_color="#D35400",
        border_width=2,
        border_color="#D35400",
        text_color="#ECF0F1"
    )
