print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Nhập tên người từ bàn phím
full_name = input("Nhập họ và tên: ").strip()

# Tách họ và tên
parts = full_name.split()  # Tách chuỗi thành các từ dựa vào khoảng trắng
ho = parts[0]  # Phần họ (từ đầu tiên)
ten = parts[-1]  # Phần tên riêng (từ cuối cùng)

# In kết quả
print("Họ:", ho)
print("Tên:", ten)
