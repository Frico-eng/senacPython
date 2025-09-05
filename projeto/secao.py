import customtkinter as ctk
dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
horarios = ["10:00 - 12:00", "13:00 - 15:00", "16:00 - 18:00", "19:00 - 21:00", "22:00 - 00:00"]
# --------- Aparência e tema ---------
ctk.set_appearance_mode("dark")  # modo escuro elegante
ctk.set_default_color_theme("blue")  # mantemos o tema base, mas sobrescrevemos cores

# --------- Janela principal ---------
app = ctk.CTk()
app.geometry("400x500")
app.title("Informações do Filme")
app.configure(fg_color="#2C3E50")  # fundo principal escuro elegante

# ------- Informações do filme -------
filme_nome = "Matrix"
sinopse_texto = "Aqui vai a sinopse do filme. Breve descrição do enredo e informações relevantes."

label_titulo = ctk.CTkLabel(
    app, 
    text=filme_nome, 
    font=ctk.CTkFont(size=20, weight="bold"),
    text_color="#ECF0F1"  # texto primário claro
)
label_titulo.pack(pady=20)

label_sinopse = ctk.CTkLabel(
    app, 
    text=sinopse_texto, 
    wraplength=350, 
    justify="left",
    text_color="#ECF0F1"  # texto primário claro
)
label_sinopse.pack(pady=10)

# ------- Escolha de dia -------
frame_dia = ctk.CTkFrame(app, fg_color="#2C3E50")
frame_dia.pack(pady=10, fill="x", padx=20)

label_dia = ctk.CTkLabel(frame_dia, text="Dias:", font=ctk.CTkFont(size=16), text_color="#ECF0F1")
label_dia.pack(side="left", padx=(0,10))

var_dia = ctk.StringVar(value=dias[0])
combo_dia = ctk.CTkComboBox(
    frame_dia, 
    values=dias, 
    variable=var_dia, 
    width=200,
    fg_color="#2C3E50",
    button_color="#E2952D",
    button_hover_color="#D35400",
    dropdown_fg_color="#ECF0F1",
    dropdown_hover_color="#BDC3C7",
    text_color="#ECF0F1"
)
combo_dia.pack(side="left")

# ------- Escolha de horário -------
frame_horario = ctk.CTkFrame(app, fg_color="#2C3E50")
frame_horario.pack(pady=10, fill="x", padx=20)

label_horario = ctk.CTkLabel(frame_horario, text="Horários:", font=ctk.CTkFont(size=16), text_color="#ECF0F1")
label_horario.pack(side="left", padx=(0,10))

var_horario = ctk.StringVar(value=horarios[0])
combo_horario = ctk.CTkComboBox(
    frame_horario, 
    values=horarios, 
    variable=var_horario, 
    width=200,
    fg_color="#2C3E50",
    button_color="#E2952D",
    button_hover_color="#D35400",
    dropdown_fg_color="#ECF0F1",
    dropdown_hover_color="#BDC3C7",
    text_color="#ECF0F1"
)
combo_horario.pack(side="left")


# ------- Botão de confirmação -------
def confirmar():
    print(f"Filme: {filme_nome}")
    print(f"Dia: {var_dia.get()}")
    print(f"Horário: {var_horario.get()}")

btn_confirmar = ctk.CTkButton(
    master=app,
    text="Confirmar",
    font=("Arial", 18, "bold"),
    width=220,
    height=40,
    corner_radius=15,
    fg_color="#E2952D",  # cor de destaque
    hover_color="#D35400",  # hover
    border_width=2,
    border_color="#BDC3C7",  # acento suave para borda
    text_color="#ECF0F1"
)
btn_confirmar.configure(command=confirmar)
btn_confirmar.pack(pady=20)

app.mainloop()
