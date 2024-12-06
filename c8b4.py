
print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Nhập một dãy các từ từ bàn phím
chuoi = input("Nhập dãy các từ: ")

# Tách chuỗi thành danh sách các từ
tu_danh_sach = chuoi.split()

# Tìm độ dài của từ dài nhất
do_dai_max = max(len(tu) for tu in tu_danh_sach)

# Lấy tất cả các từ có độ dài bằng độ dài lớn nhất
tu_dai_nhat = [tu for tu in tu_danh_sach if len(tu) == do_dai_max]

# In kết quả
print("Từ dài nhất:", ', '.join(tu_dai_nhat))
print("Độ dài:", do_dai_max)
