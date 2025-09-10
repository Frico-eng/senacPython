import customtkinter as ctk

def criar_tela_assentos(root, voltar_callback=None):
    """
    Cria e retorna o frame de seleção de assentos
    voltar_callback: função a ser chamada quando clicar no botão Voltar
    """
    
    # ================== CORES ==================
    COR_LIVRE       = "#BDC3C7"   # Cinza (livre)
    COR_SELECIONADO = "#27AE60"   # Verde (selecionado)
    COR_OCUPADO     = "#C0392B"   # Vermelho (ocupado)
    COR_TEXTO       = "#ECF0F1"
    COR_FUNDO       = "#1E1E1E"

    # Frame principal
    frame = ctk.CTkFrame(root, width=700, height=650, fg_color=COR_FUNDO)
    
    # ================== TÍTULO ==================
    label_titulo = ctk.CTkLabel(
        frame, 
        text="Selecione seu assento", 
        font=("Arial", 22, "bold"),
        text_color="white"
    )
    label_titulo.pack(pady=20)

    # ================== FRAME ASSENTOS ==================
    frame_assentos = ctk.CTkFrame(frame, width=400, height=400, corner_radius=15, fg_color=COR_FUNDO)
    frame_assentos.pack(pady=10)

    # ================== CONFIG ASSENTOS ==================
    linhas   = ["A", "B", "C", "D", "E"]  # Fileiras
    colunas = 5
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
        for j in range(colunas):
            codigo = f"{linha}{j}"

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
            botao.grid(row=i, column=j, padx=5, pady=5)

            # Guarda no dicionário
            assentos[codigo] = (botao, status)

    # ================== MENSAGEM ==================
    mensagem_label = ctk.CTkLabel(frame, text="", font=("Arial", 16, "bold"))
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
                text="Não há assentos ocupados para resetar", 
                text_color="red"
            )
            return
        
        for c in assentos_ocupados:
            botao, _ = assentos[c]
            botao.configure(fg_color=COR_LIVRE)
            assentos[c] = (botao, "livre")
        
        mensagem_label.configure(
            text="Assentos resetados", 
            text_color="green"
        )

    # Frame para os botões
    frame_botoes = ctk.CTkFrame(frame, fg_color="transparent")
    frame_botoes.pack(pady=10)

    btn_confirmar = ctk.CTkButton(
        frame_botoes, 
        text="Confirmar",
        font=("Arial", 18, "bold"),
        width=180, height=40,
        corner_radius=15,
        fg_color="#F6C148",
        hover_color="#E2952D",
        border_width=2,
        border_color="#E2952D",
        text_color="#1C2732",
        command=confirmar
    )
    btn_confirmar.pack(side="left", padx=10)

    btn_resetar = ctk.CTkButton(
        frame_botoes, 
        text="Resetar",
        font=("Arial", 18, "bold"),
        width=180, height=40,
        corner_radius=15,
        fg_color="#F6C148",
        hover_color="#E2952D",
        border_width=2,
        border_color="#E2952D",
        text_color="#1C2732",
        command=resetar
    )
    btn_resetar.pack(side="left", padx=10)

    # Botão Voltar
    if voltar_callback:
        btn_voltar = ctk.CTkButton(
            frame_botoes, 
            text="Voltar",
            font=("Arial", 18, "bold"),
            width=180, height=40,
            corner_radius=15,
            fg_color="#F6C148",
            hover_color="#E2952D",
            border_width=2,
            border_color="#E2952D",
            text_color="#1C2732",
            command=voltar_callback
        )
        btn_voltar.pack(side="left", padx=10)

    return frame