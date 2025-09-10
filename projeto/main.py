import customtkinter as ctk
from PIL import Image
from abrir_cadastro import abrir_cadastro  # Importando sua função de cadastro
from seletor_assento import criar_tela_assentos
from login import criar_tela_login
# Escolha inicial de tema ("light" ou "dark")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela principal (desktop style)
app = ctk.CTk(fg_color="#1E1E1E")
app.geometry("1000x600")
app.title("menu - Projeto Integrador")

# Frame central (mantendo o layout original)
frame_menu = ctk.CTkFrame(
    master=app,
    width=600,
    height=400,
    corner_radius=15,
    fg_color="#1E1E1E"
)

# --- Left side (logo + título) ---
left_frame = ctk.CTkFrame(master=frame_menu, width=250, fg_color="transparent")
left_frame.pack(side="left", fill="y", padx=30, pady=30)

# Logo com suporte a dark/light theme (substitua pelos caminhos corretos)
try:
    logo_image = ctk.CTkImage(
        light_image=Image.open("logo_light.png"),   # Logo para fundo claro
        dark_image=Image.open("logo_dark.png"),     # Logo para fundo escuro
        size=(200, 200)
    )
    logo_label = ctk.CTkLabel(master=left_frame, image=logo_image, text="")
    logo_label.pack(pady=(30, 20))
except:
    # Fallback se as imagens não existirem
    ctk.CTkLabel(master=left_frame, text="CinePlus", font=("Arial", 24, "bold")).pack(pady=(30, 20))

# --- Right side (botões) ---
right_frame = ctk.CTkFrame(master=frame_menu, fg_color="transparent")
right_frame.pack(side="right", expand=True, fill="both", padx=30, pady=30)

# Ícones (substitua pelos caminhos corretos)
try:
    icone_user = ctk.CTkImage(
        light_image=Image.open("icone_user.png"),
        dark_image=Image.open("icone_user.png"),
        size=(30, 30)
    )
    icone_regist = ctk.CTkImage(
        light_image=Image.open("icone_regist.png"),
        dark_image=Image.open("icone_regist.png"),
        size=(30, 30)
    )
    icone_compra = ctk.CTkImage(
        light_image=Image.open("icone_compra.png"),
        dark_image=Image.open("icone_compra.png"),
        size=(30, 30)
    )
except:
    # Fallback se as imagens não existirem
    icone_user = icone_regist = icone_compra = None

# Botões com alto contraste (laranja sobre fundo escuro)
btn_compra = ctk.CTkButton(
    master=right_frame,
    text="Comprar Agora",
    image=icone_compra,
    font=("Arial", 18, "bold"),
    width=250,
    height=45,
    corner_radius=15,
    fg_color="#F6C148",
    hover_color="#E2952D",
    border_width=2,
    border_color="#E2952D",
    text_color="#1C2732"
)
btn_compra.pack(pady=15)

btn_user = ctk.CTkButton(
    master=right_frame,
    text="Log-In",
    image=icone_user,
    font=("Arial", 18, "bold"),
    width=250,
    height=45,
    corner_radius=15,
    fg_color="#F6C148",
    hover_color="#E2952D",
    border_width=2,
    border_color="#E2952D",
    text_color="#1C2732"
)
btn_user.pack(pady=15)
login_frame = criar_tela_login(app, lambda: mostrar_frame(frame_menu))
btn_user.configure(command=lambda: mostrar_frame(login_frame))
# Criar frame de cadastro
cadastro_frame, btn_voltar_cadastro = abrir_cadastro(app)

# Footer
footer = ctk.CTkFrame(master=app, height=40, corner_radius=0, fg_color="#121212")
link_func = ctk.CTkLabel(
    master=footer,
    text="Para funcionários",
    font=("Arial", 12, "underline"),
    text_color="#3DA597",
    cursor="hand2"
)
link_func.pack(pady=8)
copyright_label = ctk.CTkLabel(footer, text="CinePlus © 2025", text_color="gray")
copyright_label.pack(pady=8)

# Função para trocar entre frames
def mostrar_frame(frame_destino):
    # Esconder todos os frames
    for widget in app.winfo_children():
        if isinstance(widget, ctk.CTkFrame) and widget != footer:
            widget.place_forget()
    
    # Mostrar o frame desejado
    if frame_destino == frame_menu:
        frame_destino.place(relx=0.5, rely=0.5, anchor="center")
        footer.pack(side="bottom", fill="x")
        # Mostrar o link "Para funcionários" na tela de menu
        link_func.pack(pady=8)
    else:
        frame_destino.place(relx=0.5, rely=0.5, anchor="center")
        # Esconder apenas o link "Para funcionários" na tela de cadastro
        link_func.pack_forget()

btn_voltar_cadastro.configure(command=lambda: mostrar_frame(frame_menu))

btn_register = ctk.CTkButton(
    master=right_frame,
    text="Registre-Se",
    image=icone_regist,
    font=("Arial", 18, "bold"),
    width=250,
    height=45,
    corner_radius=15,
    fg_color="#F6C148",
    hover_color="#E2952D",
    border_width=2,
    border_color="#E2952D",
    text_color="#1C2732",
    command=lambda: mostrar_frame(cadastro_frame)
)
btn_register.pack(pady=15)
# Adicione um botão para acessar a tela de assentos (no frame_login)
assentos_frame = criar_tela_assentos(app, lambda: mostrar_frame(frame_menu))

btn_assentos = ctk.CTkButton(
    master=right_frame,
    text="Selecionar Assentos(teste)",
    font=("Arial", 18, "bold"),
    width=250,
    height=45,
    corner_radius=15,
    fg_color="#F6C148",
    hover_color="#E2952D",
    border_width=2,
    border_color="#E2952D",
    text_color="#1C2732",
    command=lambda: mostrar_frame(assentos_frame)
)
btn_assentos.pack(pady=15)
# Mostrar frame inicial
mostrar_frame(frame_menu)

app.mainloop()