
print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Nhập chuỗi các số nhị phân từ người dùng
input_string = input("Nhập chuỗi các số nhị phân, mỗi số cách nhau bằng dấu phẩy: ")

# Tách chuỗi thành danh sách các số nhị phân
binary_numbers = input_string.split(',')

# In ra từng giá trị số nhị phân
print("Các số nhị phân đã nhập:")
for binary in binary_numbers:
    print(binary)
