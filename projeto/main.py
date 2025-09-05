import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk(fg_color="#F2F2F2")
#dimensionar janela(alturaxlargura)
app.geometry("400x500")
app.title("Login - projeto integrador")

frame = ctk.CTkFrame(master = app,width=320,height=420,corner_radius=15,fg_color= "#ECF0F1")
frame.place(relx = 0.5,rely = 0.5,anchor = "center")

logo_image = ctk.CTkImage(light_image=Image.open("logo.png"),dark_image=Image.open("logo.png"),size=(120,120))
label_title = ctk.CTkLabel(master=frame,text= "Cinema",font = ("Arial",30,"bold"))
label_title.pack(pady = (20,10))
logo_label = ctk.CTkLabel(master=frame,image=logo_image,text="")
logo_label.pack(pady = (0,10))
# usuário
icone_user = ctk.CTkImage(
    light_image=Image.open("icone_user.png"),
    dark_image=Image.open("icone_user.png"),
    size=(35, 35)  # tamanho do ícone
)
icone_regist = ctk.CTkImage(
    light_image=Image.open("icone_regist.png"),
    dark_image=Image.open("icone_regist.png"),
    size=(35, 35)  # tamanho do ícone
)
icone_compra = ctk.CTkImage(
    light_image=Image.open("icone_compra.png"),
    dark_image=Image.open("icone_compra.png"),
    size=(35, 35)  # tamanho do ícone
)
btn_compra = ctk.CTkButton(master=frame,text="Comprar Agora",image=icone_compra,font = ("Arial",18,"bold"),width=220,height=40,corner_radius=15,fg_color="#E2952D",hover_color="#D35400",border_width=2,border_color="#D35400",text_color="#ECF0F1")
btn_compra.pack(pady=(5))

btn_user = ctk.CTkButton(master=frame,text="Log-In",image=icone_user,font = ("Arial",18,"bold"),width=220,height=40,corner_radius=15,fg_color="#E2952D",hover_color="#D35400",border_width=2,border_color="#D35400",text_color="#ECF0F1")
btn_user.pack(pady=(5))

btn_register = ctk.CTkButton(master=frame,text="Registre-Se",image=icone_regist,font = ("Arial",18,"bold"),width=220,height=40,corner_radius=15,fg_color="#E2952D",hover_color="#D35400",border_width=2,border_color="#D35400",text_color="#ECF0F1")
btn_register.pack(pady=(5))

footer = ctk.CTkFrame(master=app, height=50, corner_radius=0)
footer.pack(side="bottom", fill="x")
link_func = ctk.CTkLabel(master=footer, text="Para funcionários",
                         font=("Arial", 12, "underline"),
                         text_color="#3DA597",
                         cursor="hand2")  # muda o cursor para "mãozinha"
link_func.pack(pady=5)
app.mainloop()