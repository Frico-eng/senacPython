import customtkinter as ctk
from PIL import Image, ImageTk
import os
from datetime import datetime, timedelta
from tkcalendar import Calendar, DateEntry

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
    
    # Descrição curta
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
    
    # Frame para o calendário
    calendar_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    calendar_frame.pack(pady=10)
    
    # Criar calendário interativo
    hoje = datetime.now()
    data_minima = hoje
    data_maxima = hoje + timedelta(days=30)  # Permitir agendamento até 30 dias
    
    # Usar DateEntry para um calendário dropdown mais compacto
    data_var = ctk.StringVar(value=hoje.strftime("%d/%m/%Y"))
    
    def on_date_selected():
        atualizar_horarios_disponiveis()
    
    # Criar um frame para o DateEntry (necessário para integração com CustomTkinter)
    date_entry_frame = ctk.CTkFrame(calendar_frame, fg_color="white", width=150, height=30)
    date_entry_frame.pack_propagate(False)
    date_entry_frame.pack()
    
    # Criar o DateEntry dentro do frame
    date_entry = DateEntry(
        date_entry_frame,
        width=12,
        background='darkblue',
        foreground='white',
        borderwidth=2,
        mindate=data_minima,
        maxdate=data_maxima,
        date_pattern='dd/mm/yyyy',
        textvariable=data_var
    )
    date_entry.pack(fill="both", expand=True)
    date_entry.bind("<<DateEntrySelected>>", lambda e: on_date_selected())
    
    # Horários disponíveis
    ctk.CTkLabel(content_frame, text="Selecione o horário:", font=("Arial", 16)).pack(pady=(30, 10))
    
    horarios_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    horarios_frame.pack(pady=10)
    
    horario_var = ctk.StringVar()
    
    def atualizar_horarios_disponiveis():
        """Atualiza os horários disponíveis baseado na data selecionada"""
        # Limpar horários anteriores
        for widget in horarios_frame.winfo_children():
            widget.destroy()
        
        # Obter data selecionada
        try:
            data_selecionada = datetime.strptime(data_var.get(), "%d/%m/%Y")
        except:
            data_selecionada = datetime.now()
        
        # Horários base (poderia vir de um banco de dados)
        todos_horarios = ["14:00", "16:30", "19:00", "21:30"]
        horarios_disponiveis = []
        
        agora = datetime.now()
        
        for horario in todos_horarios:
            # Converter horário para datetime
            hora, minuto = map(int, horario.split(':'))
            horario_datetime = data_selecionada.replace(hour=hora, minute=minuto, second=0)
            
            # Verificar se o horário já passou (apenas para hoje)
            if data_selecionada.date() == agora.date() and horario_datetime <= agora:
                continue  # Pular horários que já passaram hoje
            
            horarios_disponiveis.append(horario)
        
        if not horarios_disponiveis:
            ctk.CTkLabel(
                horarios_frame, 
                text="Não há sessões disponíveis para esta data",
                text_color="red",
                font=("Arial", 12)
            ).pack()
            return
        
        # Criar botões de rádio para horários disponíveis
        for i, horario in enumerate(horarios_disponiveis):
            radio = ctk.CTkRadioButton(
                horarios_frame, 
                text=horario, 
                variable=horario_var, 
                value=horario,
                font=("Arial", 12)
            )
            radio.grid(row=0, column=i, padx=10)
        
        # Selecionar primeiro horário disponível
        horario_var.set(horarios_disponiveis[0])
    
    # Inicializar horários
    atualizar_horarios_disponiveis()
    
    # Botão para avançar para seleção de assentos
    def avancar_para_assentos():
        if not horario_var.get():
            # Mostrar mensagem de erro se nenhum horário estiver selecionado
            return
        
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

# Função para verificar e fechar sessões expiradas (usar em background)
def verificar_sessoes_expiradas():
    """Verifica periodicamente se alguma sessão já passou e a fecha"""
    # Esta função pode ser chamada periodicamente usando after()
    # Aqui você implementaria a lógica para fechar sessões no seu sistema
    
    # Exemplo: verificar a cada minuto
    # parent.after(60000, verificar_sessoes_expiradas)
    pass