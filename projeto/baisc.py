import tkinter as tk
from tkinter import font

root = tk.Tk()
root.geometry("400x400")
root.configure(bg="#f4f6f9")

title_font = font.Font(family="Segoe UI", size=14, weight="bold")
button_font = font.Font(family="Segoe UI", size=11)
link_font = font.Font(family="Segoe UI", size=8, underline=True)

# frame principal de compra

# frame do usuários
frame_user = tk.Frame(root, bg="#f4f6f9")
frame_user.pack(expand=True, pady=50)  # expands vertically & horizontally, centers
botao_compra = tk.Button(frame_user,
                        text="Comprar agora",
                        font=button_font,
                        bg="#0078D7",
                        fg="white",
                        activebackground="#005A9E",
                        pady=15,
                        relief="flat", 
                        cursor="hand2")
botao_compra.pack(pady=15)
botao_user_login = tk.Button(frame_user,
                            text="Login",
                            font=button_font,
                            width=12,
                            bg="#e1e5ea",
                            relief="flat",
                            cursor="hand2")
botao_user_login.pack(pady=15)
botao_user_register = tk.Button(frame_user,
                                text="Registro",
                                font=button_font,
                                width=12,
                                bg="#e1e5ea",
                                relief="flat",
                                cursor="hand2")
botao_user_register.pack(pady=15)
# frame do funcionário
frame_func = tk.Frame(root, bg="#f4f6f9")
frame_func.pack(expand=True, fill="both", pady=10)
link_func = tk.Label(
    frame_func,
    text="Funcionários",
    font=link_font,
    fg="blue",
    bg="#f4f6f9",
    cursor="hand2"
)
link_func.pack(side="bottom")


root.mainloop()