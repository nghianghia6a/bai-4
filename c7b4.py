print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Nhập một chuỗi từ bàn phím
chuoi = input("Nhập chuỗi: ")

# Loại bỏ các chữ số
chuoi_moi = ''.join(ch for ch in chuoi if not ch.isdigit())

# In chuỗi mới
print("Chuỗi sau khi loại bỏ chữ số:", chuoi_moi)
