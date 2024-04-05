import re
from constants.setup import *
import tkinter as tk
from tkinter import messagebox
import sys
sys.path.append('./database')
import user_database

# Biến global để theo dõi trạng thái hiện tại của giao diện (đăng nhập hoặc đăng ký)
current_mode = "login"


def toggle_login_register():
    global current_mode
    if current_mode == "login":
        label_username.grid(row=0, column=0, padx=(70, 10), pady=(200, 5), sticky="e")
        entry_username.grid(row=0, column=1, padx=10, pady=(200, 5))
        label_password.grid(row=1, column=0, padx=(70, 10), pady=5, sticky="e")
        entry_password.grid(row=1, column=1, padx=10, pady=5)
        label_confirm_password.grid(row=2, column=0, padx=(70, 10), pady=5, sticky="e")
        entry_confirm_password.grid(row=2, column=1, padx=10, pady=5)
        button_auth.grid(row=3, column=0, columnspan=2,
                        padx=(70, 10), pady=10, sticky="we")
        button_toggle.grid(row=4, column=0, columnspan=2,
                        padx=(70, 10), pady=(5, 10), sticky="we")
        button_toggle.config(text="Already have an account? Login here!",
                             command=toggle_login_register, bg="red", fg="white")
        button_auth.config(text="Register", command=register)
        current_mode = "register"
    elif current_mode == "register":
        # Ẩn label và entry của confirm password
        label_confirm_password.grid_forget()
        entry_confirm_password.grid_forget()

        # Định vị lại các widget cho chế độ login
        label_username.grid(row=0, column=0, padx=(70, 10), pady=(200, 5), sticky="e")
        entry_username.grid(row=0, column=1, padx=10, pady=(200, 5))
        label_password.grid(row=1, column=0, padx=(70, 10), pady=5, sticky="e")
        entry_password.grid(row=1, column=1, padx=10, pady=5)
        button_auth.grid(row=2, column=0, columnspan=2,
                        padx=(70, 10), pady=10, sticky="we")
        button_toggle.config(text="Don't have an account? Register here!",
                             command=toggle_login_register, bg="red", fg="white")
        button_auth.config(text="Login", command=login)
        current_mode = "login"


def register():
    username = entry_username.get()
    password = entry_password.get()

    # Kiểm tra nếu người dùng đã tồn tại
    existing_user = user_database.get_user_info(username)
    if existing_user:
        messagebox.showerror("Registration Failed", "Username already exists.")
    elif not username.strip():  # Kiểm tra nếu username chỉ chứa khoảng trắng
        messagebox.showerror("Registration Failed",
                             "Username cannot be empty or contain only spaces.")
    # Kiểm tra nếu username chứa ký tự không hợp lệ
    elif not re.match(r'^[a-zA-Z0-9_]+$', username):
        messagebox.showerror(
            "Registration Failed", "Username can only contain letters, numbers, and underscores.")
    else:
        # Đăng ký người dùng mới
        user_database.register_user(username, password)
        messagebox.showinfo("Registration Successful",
                            "Account created successfully.")


def login():
    username = entry_username.get()
    password = entry_password.get()

    # Kiểm tra thông tin đăng nhập
    user = user_database.get_user_info(username)
    if user and user[2] == password:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")

        # Đóng cửa sổ đăng nhập
        root.destroy()

        # Lấy thông tin hiện tại của người dùng
        current_user_info = user_database.get_user_info(username)

        # Import module main và chạy giao diện game ở đây
        import start
        start.current_username = username
        from start import game_start_loop
        game_start_loop()

    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


# Tạo cửa sổ đăng nhập và đăng ký
root = tk.Tk()
root.title("Login or Register")

# Khóa kích thước cửa sổ để không thể phóng to
root.resizable(width=False, height=False)

# Thiết lập hình nền
background_image = tk.PhotoImage(
    file="resources/images/Game_Loop_Background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Kích thước của cửa sổ
window_width = 400
window_height = 600

# Lấy kích thước màn hình và tính toán vị trí của cửa sổ đăng nhập
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Thiết lập vị trí và kích thước của cửa sổ
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Load hình ảnh cho các nút
login_image = tk.PhotoImage(file="resources/images/game_play_button.png")
register_image = tk.PhotoImage(file="resources/images/game_play_button.png")

label_username = tk.Label(root, text="Username:",width=15)
label_password = tk.Label(root, text="Password:",width=15)
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")
label_confirm_password = tk.Label(root, text="Confirm Password:",width=15)
entry_confirm_password = tk.Entry(root, show="*")
button_auth = tk.Button(root, text="Login",
                        command=login, highlightthickness=0)
button_toggle = tk.Button(root, text="Don't have an account? Register here!",
                          command=toggle_login_register, highlightthickness=0, bg="red", fg="white")
button_auth.config(font=("Helvetica", 8, "bold"),width=10,height=3,borderwidth=2, relief="solid")  
button_toggle.config(font=("Helvetica", 8, "bold"),width=10,height=3,borderwidth=2, relief="solid",wraplength=150)  


# Định vị các widgets
label_username.grid(row=0, column=0, padx=(70, 10), pady=(200, 5), sticky="e")
label_password.grid(row=1, column=0, padx=(70, 10), pady=5, sticky="e")
entry_username.grid(row=0, column=1, padx=10, pady=(200, 5))
entry_password.grid(row=1, column=1, padx=10, pady=5)
button_auth.grid(row=2, column=0, columnspan=2,
                 padx=(70, 10), pady=10, sticky="we")
button_toggle.grid(row=3, column=0, columnspan=2,
                   padx=(70, 10), pady=(5, 10), sticky="we")
root.mainloop()
