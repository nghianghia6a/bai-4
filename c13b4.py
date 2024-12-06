print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Giả sử 'ds' là danh sách ban đầu
ds = ['x', 'y', 'abc', 'z', 'w']  # Ví dụ danh sách

# Tìm kiếm vị trí của phần tử 'abc' trong danh sách
try:
    position = ds.index('abc')
    print("Vị trí của chuỗi 'abc' là:", position)
except ValueError:
    print("Chuỗi 'abc' không có trong danh sách.")
