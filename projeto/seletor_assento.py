import customtkinter as ctk

# ================== CORES ==================
COR_LIVRE       = "#BDC3C7"   # Cinza (livre)
COR_SELECIONADO = "#27AE60"   # Verde (selecionado)
COR_OCUPADO     = "#C0392B"   # Vermelho (ocupado)
COR_TEXTO       = "#ECF0F1"

# ================== CONFIG JANELA ==================
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("700x650")
app.title("Cinema - Seleção de Assentos")

# ================== TÍTULO ==================
label_titulo = ctk.CTkLabel(
    app, 
    text="Selecione seu assento", 
    font=("Arial", 22, "bold")
)
label_titulo.pack(pady=20)

# ================== FRAME ASSENTOS ==================
frame_assentos = ctk.CTkFrame(app, width=400, height=400, corner_radius=15)
frame_assentos.pack(pady=10)

# ================== CONFIG ASSENTOS ==================
linhas   = ["A", "B", "C"]  # Fileiras
ocupados = {}           # Assentos já ocupados no início

# Dicionário: { "A1": (botao, status) }
assentos = {}

def toggle_assento(codigo: str):
    """Alterna estado do assento (livre <-> selecionado)"""
    botao, status = assentos[codigo]

    if status == "ocupado":
        mensagem_label.configure(
            text=f"O assento {codigo} já está ocupado.", 
            text_color="red"
        )
        return

    if status == "livre":
        botao.configure(fg_color=COR_SELECIONADO)
        assentos[codigo] = (botao, "selecionado")

    elif status == "selecionado":
        botao.configure(fg_color=COR_LIVRE)
        assentos[codigo] = (botao, "livre")

# Criando os botões no grid
for i, linha in enumerate(linhas):
        codigo = f"{linha}{0}"

        # Define cor e status inicial
        if codigo in ocupados:
            cor, status = COR_OCUPADO, "ocupado"
        else:
            cor, status = COR_LIVRE, "livre"

        # Cria botão
        botao = ctk.CTkButton(
            frame_assentos, 
            text=codigo,
            width=50, height=40,
            fg_color=cor,
            text_color=COR_TEXTO,
            font=("Arial", 14, "bold"),
            corner_radius=10,
            command=lambda c=codigo: toggle_assento(c)
        )
        botao.grid(row=i, column=0, padx=5, pady=5)

        # Guarda no dicionário
        assentos[codigo] = (botao, status)

# ================== MENSAGEM ==================
mensagem_label = ctk.CTkLabel(app, text="", font=("Arial", 16, "bold"))
mensagem_label.pack(pady=10)

# ================== BOTÃO CONFIRMAR ==================
def confirmar():
    """Confirma seleção e marca como ocupado"""
    selecionados = [
        c for c, (_, status) in assentos.items() if status == "selecionado"
    ]

    if not selecionados:
        mensagem_label.configure(
            text="Nenhum assento selecionado.", 
            text_color="red"
        )
        return

    # Atualiza todos os selecionados para ocupados
    for c in selecionados:
        botao, _ = assentos[c]
        botao.configure(fg_color=COR_OCUPADO)
        assentos[c] = (botao, "ocupado")

    mensagem_label.configure(
        text=f"Assentos confirmados: {', '.join(selecionados)}", 
        text_color="green"
    )
def resetar():
    assentos_ocupados = [
        c for c, (_, status) in assentos.items() if status == "ocupado"
    ]
    if not assentos_ocupados:
        mensagem_label.configure(
            text="não funcionou", 
            text_color="red"
        )
        return
    print(assentos_ocupados)
    for c in assentos_ocupados:
        botao, _ = assentos[c]
        botao.configure(fg_color=COR_LIVRE)
        assentos[c] = (botao, "livre")
    mensagem_label.configure(
        text=f"Assentos resetados", 
        text_color="green"
    )

btn_confirmar = ctk.CTkButton(
    app, 
    text="Confirmar",
    font=("Arial", 18, "bold"),
    width=220, height=40,
    corner_radius=15,
    fg_color="#E2952D",
    hover_color="#D35400",
    border_width=2,
    border_color="#D35400",
    text_color=COR_TEXTO,
    command=confirmar
)
btn_confirmar.pack(pady=20)
btn_voltar = ctk.CTkButton(
    app, 
    text="Resetar",
    font=("Arial", 18, "bold"),
    width=220, height=40,
    corner_radius=15,
    fg_color="#E2952D",
    hover_color="#D35400",
    border_width=2,
    border_color="#D35400",
    text_color=COR_TEXTO,
    command=resetar
)
btn_voltar.pack(pady=20)
# ================== LOOP PRINCIPAL ==================
app.mainloop()
