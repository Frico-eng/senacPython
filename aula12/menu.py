import customtkinter as ctk
import cadastro_usuario



def abrir_menu():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    menu_app = ctk.CTk()
    menu_app.geometry("600x400")
    menu_app.title("Menu - Projeto integrador")
    def abrir_cadastro():
        menu_app.destroy()
        cadastro_usuario.abrir_cadastro()
    frame = ctk.CTkFrame(master=menu_app, width=500, height=350, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    label_title = ctk.CTkLabel(master=menu_app, text="Menu de opções", font=("Arial", 20, "bold"))
    label_title.pack(pady=(0, 10))

    btn_cadastro = ctk.CTkButton(master=menu_app, text="Cadastro de usuário",
                           width=250, height=40, corner_radius=15,
                           fg_color="#85DA85", hover_color="#AEFFAE",
                           border_width=2, border_color="#64A064",
                           text_color="#181F18", command=abrir_cadastro)
    btn_cadastro.pack(pady=5)

    btn_relatorio = ctk.CTkButton(master=menu_app, text="Relatorio",
                           width=250, height=40, corner_radius=15,
                           fg_color="#85DA85", hover_color="#AEFFAE",
                           border_width=2, border_color="#64A064",
                           text_color="#181F18", command=lambda: print("relatorio clicado"))
    btn_relatorio.pack(pady=5)

    btn_config = ctk.CTkButton(master=menu_app, text="Configurações",
                           width=250, height=40, corner_radius=15,
                           fg_color="#85DA85", hover_color="#AEFFAE",
                           border_width=2, border_color="#64A064",
                           text_color="#181F18", command=lambda: print("config clicado"))
    btn_config.pack(pady=5)

    btn_sair = ctk.CTkButton(master=menu_app, text="Sair",
                           width=250, height=40, corner_radius=15,
                           fg_color="#85DA85", hover_color="#AEFFAE",
                           border_width=2, border_color="#64A064",
                           text_color="#181F18", command=lambda: print("sair clicado"))
    btn_sair.pack(pady=5)

    menu_app.mainloop()
