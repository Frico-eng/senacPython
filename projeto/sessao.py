import customtkinter as ctk
from PIL import Image, ImageTk
import os
from datetime import datetime, timedelta

def criar_tela_sessoes(parent, filme_selecionado, callback_voltar, callback_avancar):
    """Cria tela de seleção de data e sessão para um filme"""
    frame = ctk.CTkFrame(parent, fg_color="#1E1E1E", width=800, height=600)
    
    # Header com título e botão voltar
    header_frame = ctk.CTkFrame(frame, fg_color="transparent")
    header_frame.pack(pady=20, fill="x")
    
    btn_voltar = ctk.CTkButton(
        header_frame, 
        text="← Voltar", 
        command=callback_voltar,
        width=100,
        height=30,
        fg_color="#F6C148",
        hover_color="#E2952D",
        text_color="#1C2732"
    )
    btn_voltar.pack(side="left", padx=20)
    
    titulo_label = ctk.CTkLabel(
        header_frame, 
        text=f"Selecionar Sessão: {filme_selecionado['titulo']}", 
        font=("Arial", 20, "bold")
    )
    titulo_label.pack(side="left", padx=20)
    
    # Conteúdo principal
    content_frame = ctk.CTkFrame(frame, fg_color="transparent")
    content_frame.pack(pady=40, fill="both", expand=True)
    
    # Frame para imagem e informações
    info_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    info_frame.pack(pady=10, fill="x")
    
    # Exibir imagem do filme
    try:
        if os.path.exists(filme_selecionado["imagem"]):
            img = Image.open(filme_selecionado["imagem"])
            img = img.resize((150, 225), Image.LANCZOS)
            foto = ImageTk.PhotoImage(img)
            img_label = ctk.CTkLabel(info_frame, image=foto, text="")
            img_label.image = foto  # Manter referência
            img_label.pack(side="left", padx=20)
    except:
        pass
    
    # Informações do filme
    info_text_frame = ctk.CTkFrame(info_frame, fg_color="transparent")
    info_text_frame.pack(side="left", fill="both", expand=True, padx=20)
    
    ctk.CTkLabel(
        info_text_frame, 
        text=filme_selecionado["titulo"], 
        font=("Arial", 16, "bold")
    ).pack(anchor="w", pady=(0, 10))
    
    # Descrição curta (primeiras 100 caracteres)
    descricao_curta = filme_selecionado["descricao"][:100] + "..." if len(filme_selecionado["descricao"]) > 100 else filme_selecionado["descricao"]
    ctk.CTkLabel(
        info_text_frame, 
        text=descricao_curta, 
        font=("Arial", 12),
        wraplength=400,
        justify="left"
    ).pack(anchor="w")
    
    # Separador
    ctk.CTkFrame(content_frame, height=2, fg_color="#333").pack(fill="x", pady=20)
    
    # Calendário para seleção de data
    ctk.CTkLabel(content_frame, text="Selecione a data:", font=("Arial", 16)).pack(pady=10)
    
    # Gerar datas disponíveis (próximos 7 dias)
    datas_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    datas_frame.pack(pady=10)
    
    hoje = datetime.now()
    datas_disponiveis = []
    for i in range(7):
        data = hoje + timedelta(days=i)
        datas_disponiveis.append(data.strftime("%d/%m/%Y"))
    
    data_var = ctk.StringVar(value=datas_disponiveis[0])
    
    for i, data in enumerate(datas_disponiveis):
        radio = ctk.CTkRadioButton(
            datas_frame, 
            text=data, 
            variable=data_var, 
            value=data,
            font=("Arial", 12)
        )
        radio.grid(row=0, column=i, padx=10)
    
    # Horários disponíveis
    ctk.CTkLabel(content_frame, text="Selecione o horário:", font=("Arial", 16)).pack(pady=(30, 10))
    
    horarios_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    horarios_frame.pack(pady=10)
    
    # Horários disponíveis (poderia variar por dia)
    horarios_disponiveis = ["14:00", "16:30", "19:00", "21:30"]
    horario_var = ctk.StringVar(value=horarios_disponiveis[0])
    
    for i, horario in enumerate(horarios_disponiveis):
        radio = ctk.CTkRadioButton(
            horarios_frame, 
            text=horario, 
            variable=horario_var, 
            value=horario,
            font=("Arial", 12)
        )
        radio.grid(row=0, column=i, padx=10)
    
    # Botão para avançar para seleção de assentos
    def avancar_para_assentos():
        data_selecionada = data_var.get()
        horario_selecionado = horario_var.get()
        callback_avancar(filme_selecionado, data_selecionada, horario_selecionado)
    
    btn_avancar = ctk.CTkButton(
        content_frame, 
        text="Selecionar Assentos →", 
        command=avancar_para_assentos,
        width=200,
        height=40,
        fg_color="#4CAF50",
        hover_color="#45a049",
        text_color="white",
        font=("Arial", 14, "bold")
    )
    btn_avancar.pack(pady=30)
    
    return frame