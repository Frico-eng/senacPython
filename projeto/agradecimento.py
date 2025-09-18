import customtkinter as ctk
from PIL import Image, ImageTk

def mostrar_tela_agradecimento(parent, voltar_callback=None):
    """
    Mostra a tela de agradecimento dentro de um frame existente (não cria nova janela)
    
    Args:
        parent: CTkFrame onde o conteúdo será exibido
        voltar_callback: função a ser chamada ao clicar no botão "Voltar para o início"
    """
    # Limpar frame pai
    for widget in parent.winfo_children():
        widget.destroy()

    # Fundo
    parent.configure(fg_color="#22313F")

    # === LOGO CINEPLUS ===
    img_logo = Image.open("C:\\Users\\fredl\\OneDrive\\Área de Trabalho\\projects\\python\\senacPython\\projeto\\images\\logo_dark.png")
    img_logo = img_logo.resize((204, 204), Image.LANCZOS)
    logo_tk = ImageTk.PhotoImage(img_logo)
    
    logo_label = ctk.CTkLabel(parent, image=logo_tk, text="", fg_color="transparent")
    logo_label.image = logo_tk  # manter referência
    logo_label.pack(pady=20)

    # === Mensagem de agradecimento ===
    mensagem = (
        "Agradecemos seu pagamento ✅\n"
        "Qualquer dúvida estamos à disposição!\n\n"
        "🎬 Bom filme!"
    )
    ctk.CTkLabel(
        parent,
        text=mensagem,
        font=("Segoe UI", 16, "bold"),
        text_color="white",
        fg_color="transparent",
        justify="center"
    ).pack(pady=20)

    # Botão para voltar ao início
    ctk.CTkButton(
        parent,
        text="Voltar para o início",
        width=200,
        height=40,
        command=voltar_callback if voltar_callback else lambda: None,
        fg_color="#FFA94D",
        hover_color="#FFB84D",
        text_color="#22313F",
        font=("Segoe UI", 12, "bold")
    ).pack(pady=25)
