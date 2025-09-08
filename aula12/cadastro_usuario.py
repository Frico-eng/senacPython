import customtkinter as ctk
from tkinter import messagebox

def abrir_cadastro():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    cadastro_app = ctk.CTk()
    cadastro_app.geometry("400x500")
    cadastro_app.title("cadastro de usuário")
    
    main_frame = ctk.CTkFrame(master = cadastro_app,width=320,height=420,corner_radius=15)
    main_frame.place(relx = 0.5,rely = 0.5,anchor = "center")
    label_title = ctk.CTkLabel(master=main_frame,text= "Bem vindo",font = ("Arial",20,"bold"))
    label_title.pack(pady = (0,10))
    entry_nome = ctk.CTkEntry(master=main_frame,placeholder_text="Nome",width=250,height=40,corner_radius=10)
    entry_nome.pack(pady=10)
    
    entry_email = ctk.CTkEntry(master=main_frame,placeholder_text="email",width=250,height=40,corner_radius=10)
    entry_email.pack(pady=10)
    
    entry_user = ctk.CTkEntry(master=main_frame,placeholder_text="usuário",width=250,height=40,corner_radius=10)
    entry_user.pack(pady=10)
    
    entry_senha = ctk.CTkEntry(master=main_frame,placeholder_text="senha",show = "*",width=250,height=40,corner_radius=10)
    entry_senha.pack(pady=10)
    
    entry_confsenha = ctk.CTkEntry(master=main_frame,placeholder_text="confirmar senha",show = "*",width=250,height=40,corner_radius=10)
    entry_confsenha.pack(pady=10)
    def salvar():
        nome = entry_nome.get()
        email = entry_email.get()
        user = entry_user.get()
        senha = entry_senha.get()
        confsenha = entry_confsenha.get()

        if not nome or not email or not user or not senha or not confsenha:
            messagebox.showwarning("atenção", "preencha todos os campos")
            return
        if senha != confsenha:
            messagebox.showerror("Erro", "senha diferente da confirmação")
            return
        
        messagebox.showinfo("Sucesso",f"Usuário {user} cadastrado com sucesso")
        
    btn_register = ctk.CTkButton(master=main_frame,text="Confirmar",width=250,height=40,corner_radius=15,fg_color="#3053A0",hover_color="#6195F7",border_width=2,border_color="#2D199C",text_color="#19181F",command=salvar)
    btn_register.pack(pady=(5))
    cadastro_app.mainloop()