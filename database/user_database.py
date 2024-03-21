import mysql.connector

# Kết nối đến MySQL Server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="solar_system_protection"
)
cursor = conn.cursor()

# Tạo bảng users nếu chưa tồn tại
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) UNIQUE,
                    password VARCHAR(255),
                    highest_score INT DEFAULT 0
                    )''')

# Đăng ký một người chơi mới


def register_user(username, password):
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                   (username, password))
    conn.commit()

# Lấy thông tin người chơi dựa trên username


def get_user_info(username):
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    return cursor.fetchone()

# Cập nhật điểm cao nhất của người chơi


def update_highest_score(username, new_score):
    cursor.execute(
        "UPDATE users SET highest_score=%s WHERE username=%s", (new_score, username))
    conn.commit()

# Đóng kết nối tới cơ sở dữ liệu


def close_db_connection():
    conn.close()
