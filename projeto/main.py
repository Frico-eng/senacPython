import customtkinter as ctk
from PIL import Image
import os

from abrir_cadastro import abrir_cadastro
from seletor_assento import criar_tela_assentos
from login import criar_tela_login

# --- Configuração inicial ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk(fg_color="#1E1E1E")
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Ajustar janela para ocupar toda a tela (sem remover a barra do Windows)
app.geometry(f"{screen_width+20}x{screen_height-80}-10+0")
app.title("menu - Projeto Integrador")

# --- Fundo com imagem ---
def carregar_fundo(frame, path):
    if os.path.exists(path):
        original_image = Image.open(path)

        def atualizar_fundo(event):
            largura, altura = event.width, event.height
            img_resized = original_image.resize((largura, altura))
            fundo_ctk = ctk.CTkImage(img_resized, size=(largura, altura))
            fundo_label.configure(image=fundo_ctk)
            fundo_label.image = fundo_ctk  # evitar GC

        fundo_label = ctk.CTkLabel(frame, text="", fg_color="transparent")
        fundo_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        frame.bind("<Configure>", atualizar_fundo)
        return fundo_label
    else:
        return ctk.CTkLabel(frame, text="CinePlus", font=("Arial", 40, "bold"), fg_color="transparent")

# --- Frame inicial ---
tela_inicial = ctk.CTkFrame(app, fg_color="transparent")
tela_inicial.place(relx=0, rely=0, relwidth=1, relheight=1)

fundo_label = carregar_fundo(tela_inicial, "left_banner.jpg")

# --- Área de botões (flutuante) ---
right_frame = ctk.CTkFrame(master=tela_inicial, fg_color="transparent")
right_frame.place(relx=0.65, rely=0, relwidth=0.25, relheight=1)

# --- Logo ---
def carregar_logo(master):
    if os.path.exists("logo_light.png") and os.path.exists("logo_dark.png"):
        logo_image = ctk.CTkImage(
            light_image=Image.open("logo_light.png"),
            dark_image=Image.open("logo_dark.png"),
            size=(200, 200)
        )
        return ctk.CTkLabel(master=master, image=logo_image, text="", fg_color="transparent")
    return ctk.CTkLabel(master=master, text="CinePlus", font=("Arial", 24, "bold"), fg_color="transparent")

logo_label = carregar_logo(right_frame)
logo_label.pack(pady=(30, 20))

# --- Ícones ---
def carregar_icone(path, size=(30, 30)):
    return ctk.CTkImage(Image.open(path), size=size) if os.path.exists(path) else None

icone_user = carregar_icone("icone_user.png")
icone_regist = carregar_icone("icone_regist.png")
icone_compra = carregar_icone("icone_compra.png")

# --- Criar telas secundárias ---
login_frame = criar_tela_login(app, lambda: mostrar_frame(None))
cadastro_frame, btn_voltar_cadastro = abrir_cadastro(app)
assentos_frame = criar_tela_assentos(app, lambda: mostrar_frame(None))
btn_voltar_cadastro.configure(command=lambda: mostrar_frame(None))

# --- Função para criar botões ---
def criar_botao(master, texto, comando=None, icone=None):
    return ctk.CTkButton(
        master=master,
        text=texto,
        image=icone,
        font=("Arial", 18, "bold"),
        width=250,
        height=45,
        corner_radius=15,
        fg_color="#F6C148",
        hover_color="#E2952D",
        border_width=2,
        border_color="#E2952D",
        text_color="#1C2732",
        command=comando
    )

# --- Função para trocar frames ---
def mostrar_frame(frame_destino):
    # Esconde todos os frames filhos de app exceto footer
    for widget in app.winfo_children():
        if isinstance(widget, ctk.CTkFrame) and widget not in (footer,):
            widget.place_forget()
    # Mostrar o frame destino ou voltar para tela inicial
    if frame_destino:
        frame_destino.place(relx=0.5, rely=0.5, anchor="center")
    else:
        tela_inicial.place(relx=0, rely=0, relwidth=1, relheight=1)

# --- Botões principais ---
criar_botao(right_frame, "Comprar Agora", icone=icone_compra).pack(pady=15)
criar_botao(right_frame, "Log-In", lambda: mostrar_frame(login_frame), icone_user).pack(pady=15)
criar_botao(right_frame, "Registre-Se", lambda: mostrar_frame(cadastro_frame), icone_regist).pack(pady=15)
criar_botao(right_frame, "Selecionar Assentos (teste)", lambda: mostrar_frame(assentos_frame)).pack(pady=15)

# --- Footer tela inicial ---
footer_inicial = ctk.CTkFrame(master=app, height=40, corner_radius=0, fg_color="#121212")
footer_inicial.place(relx=0, rely=1, relwidth=1, anchor="sw")

# Left e right
footer_left = ctk.CTkFrame(footer_inicial, fg_color="transparent")
footer_left.pack(side="left", padx=20, pady=5)
ctk.CTkLabel(footer_left, text="Contato | Sugestão", text_color="gray").pack()

footer_right = ctk.CTkFrame(footer_inicial, fg_color="transparent")
footer_right.pack(side="right", padx=20, pady=5)
ctk.CTkLabel(footer_right, text="CinePlus © 2025", text_color="gray").pack()

# --- Footer das outras telas ---
footer_secundario = ctk.CTkFrame(master=app, height=40, corner_radius=0, fg_color="#121212")
ctk.CTkLabel(footer_secundario, text="CinePlus © 2025", text_color="gray").pack(pady=8)
# --- Função para trocar frames ---
def mostrar_frame(frame_destino):
    # Esconde todos os frames filhos de app exceto footers
    for widget in app.winfo_children():
        if isinstance(widget, ctk.CTkFrame) and widget not in (footer_inicial, footer_secundario):
            widget.place_forget()
    
    # Mostrar frame destino ou voltar para inicial
    if frame_destino:
        frame_destino.place(relx=0.5, rely=0.5, anchor="center")
        footer_inicial.place_forget()
        footer_secundario.place(relx=0.5, rely=1, relwidth=1, anchor="s")
    else:
        tela_inicial.place(relx=0, rely=0, relwidth=1, relheight=1)
        footer_secundario.place_forget()
        footer_inicial.place(relx=0, rely=1, relwidth=1, anchor="sw")



app.mainloop()
