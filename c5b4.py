print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

ds = input('Danh sách: ').split()  # Nhập và tách danh sách thành các từ

# Đảo ngược thứ tự danh sách
ds_reverse = ds[::-1]  # Sử dụng slicing để đảo ngược danh sách

# In danh sách ngược lại
print(' '.join(ds_reverse))  # Kết hợp các từ ngược lại thành chuỗi
