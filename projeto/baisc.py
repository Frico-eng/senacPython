import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tela Inicial")
root.geometry("500x500")
root.configure(bg="#f5f5f5")

# estilo geral
style = ttk.Style()
style.configure("Main.TButton", font=("Segoe UI", 12), padding=10)

# estilo exclusivo só para o frame de registro
style.configure("Reg.TButton", font=("Segoe UI", 10), padding=(5,15))

frame = ttk.Frame(root, padding=30)
frame.pack(expand=True)

# botões principais
divider = ttk.Label(frame, text="────────  Entrada  ────────", foreground="gray")
divider.pack(pady=15)
btn_compra = ttk.Button(frame, text="🛒  Compra Rápida", style="Main.TButton")
btn_compra.pack(fill="x", pady=8)

btn_login = ttk.Button(frame, text="🔑  Login", style="Main.TButton")
btn_login.pack(fill="x", pady=8)

btn_login_adm = ttk.Button(frame, text="👨‍💼  Login Adm", style="Main.TButton")
btn_login_adm.pack(fill="x", pady=8)

divider = ttk.Label(frame, text="────────  Registro  ────────", foreground="gray")
divider.pack(pady=15)

# frame de registro
reg_frame = ttk.Frame(frame)
reg_frame.pack()

# botões de registro (usam estilo exclusivo Reg.TButton)
btn_reg = ttk.Button(reg_frame, text="👤 Cadastro de usuário", style="Reg.TButton")
btn_reg.pack(side="left", padx=5, ipadx=10)

btn_staff_reg = ttk.Button(reg_frame, text="🛠️ Cadastrar funcionário", style="Reg.TButton")
btn_staff_reg.pack(side="left", padx=5, ipadx=10)

root.mainloop()
