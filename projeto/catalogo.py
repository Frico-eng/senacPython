import customtkinter as ctk
from PIL import Image, ImageDraw

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x600")
app.title("Seleção de Filmes")

# ------- Criar placeholder de cartaz -------
def criar_placeholder():
    img = Image.new("RGB", (120, 180), color=(80, 80, 80))
    draw = ImageDraw.Draw(img)
    draw.text((20, 80), "Poster", fill=(200, 200, 200))
    return ctk.CTkImage(light_image=img, dark_image=img, size=(120, 180))

# ------- Lista de filmes -------
filmes = [
    "Matrix", "O Senhor dos Anéis", "Star Wars", "Vingadores", "Harry Potter",
    "Batman", "Homem-Aranha", "Avatar", "Interestelar", "Duna",
    "Gladiador", "O Rei Leão", "Toy Story", "Shrek", "Jurassic Park"
]

# ------- Frame rolável -------
scroll = ctk.CTkScrollableFrame(app, width=580, height=580)
scroll.pack(pady=10, padx=10, fill="both", expand=True)

# ------- Layout em grid (3 colunas) -------
colunas = 3
poster_img = criar_placeholder()

for i, filme in enumerate(filmes):
    # cada card é um botão (imagem + texto)
    btn_card = ctk.CTkButton(
        master=scroll,
        image=poster_img,
        text=filme,
        compound="top",           # imagem em cima, texto embaixo
        width=150,
        height=220,
        fg_color="#2b2b2b",
        hover_color="#444444",
        corner_radius=10,
        command=lambda f=filme: print(f"Selecionado: {f}")  # ação ao clicar
    )
    row = i // colunas
    col = i % colunas
    btn_card.grid(row=row, column=col, padx=10, pady=10)

app.mainloop()
