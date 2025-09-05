import customtkinter as ctk
from PIL import Image
import menu

def abrir_menu():
    app.destroy()
    menu.abrir_menu()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
#dimensionar janela(alturaxlargura)
app.geometry("400x500")
app.title("Login - projeto integrador")

frame = ctk.CTkFrame(master = app,width=320,height=420,corner_radius=15)
frame.place(relx = 0.5,rely = 0.5,anchor = "center")

logo_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\59699816\\Desktop\\PythonSENAC\\aula12\\logo.png"),dark_image=Image.open("C:\\Users\\59699816\\Desktop\\PythonSENAC\\aula12\\logo.png"),size=(120,120))

logo_label = ctk.CTkLabel(master=frame,image=logo_image,text="")
logo_label.pack(pady = (20,10))

label_title = ctk.CTkLabel(master=frame,text= "Bem vindo",font = ("Arial",20,"bold"))
label_title.pack(pady = (0,10))
label_subtitle = ctk.CTkLabel(master=frame,text= "Faça login para continuar",font = ("Arial",13))
label_subtitle.pack(pady = (0,10))

# usuári


entry_user = ctk.CTkEntry(master=frame,placeholder_text="Usuário",width=250,height=40,corner_radius=10)
entry_user.pack(pady=10)

entry_pass = ctk.CTkEntry(master=frame,placeholder_text="Senha",show = "*",width=250,height=40,corner_radius=10)
entry_pass.pack(pady=10)
btn_login = ctk.CTkButton(master=frame,text="Entrar",width=250,height=40,corner_radius=15,fg_color="#85DA85",hover_color="#AEFFAE",border_width=2,border_color="#64A064",text_color="#181F18",command=abrir_menu)
btn_login.pack(pady=5)
btn_register = ctk.CTkButton(master=frame,text="Cadastrar",width=250,height=40,corner_radius=15,fg_color="#3053A0",hover_color="#6195F7",border_width=2,border_color="#2D199C",text_color="#19181F")
btn_register.pack(pady=(5))

app.mainloop()
