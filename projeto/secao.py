import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("Informações do Filme")

# ------- Informações do filme -------
filme_nome = "Matrix"
sinopse_texto = "Aqui vai a sinopse do filme. Breve descrição do enredo e informações relevantes."

label_titulo = ctk.CTkLabel(app, text=filme_nome, font=ctk.CTkFont(size=20, weight="bold"))
label_titulo.pack(pady=20)

label_sinopse = ctk.CTkLabel(app, text=sinopse_texto, wraplength=350, justify="left")
label_sinopse.pack(pady=10)

# ------- Escolha de dia -------
label_dia = ctk.CTkLabel(app, text="Dias:", font=ctk.CTkFont(size=16))
label_dia.pack(pady=10)

dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
var_dia = ctk.StringVar(value=dias[0])
combo_dia = ctk.CTkComboBox(app, values=dias, variable=var_dia, width=200)
combo_dia.pack(pady=5)

# ------- Escolha de horário -------
label_horario = ctk.CTkLabel(app, text="Horários:", font=ctk.CTkFont(size=16))
label_horario.pack(pady=10)

# horários formatados com início e fim
horarios = ["10:00 - 12:00", "13:00 - 15:00", "16:00 - 18:00", "19:00 - 21:00", "22:00 - 00:00"]
var_horario = ctk.StringVar(value=horarios[0])
combo_horario = ctk.CTkComboBox(app, values=horarios, variable=var_horario, width=200)
combo_horario.pack(pady=5)

# ------- Botão de confirmação -------
def confirmar():
    print(f"Filme: {filme_nome}")
    print(f"Dia: {var_dia.get()}")
    print(f"Horário: {var_horario.get()}")

btn_confirmar = ctk.CTkButton(app, text="Confirmar", command=confirmar)
btn_confirmar.pack(pady=20)

app.mainloop()
