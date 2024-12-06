print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Hàm kiểm tra xem tất cả các chữ số của số có phải là số chẵn không
def check_even_digits(num):
    for digit in str(num):  # Chuyển số thành chuỗi và kiểm tra từng chữ số
        if int(digit) % 2 != 0:  # Nếu chữ số không phải chẵn
            return False
    return True

# Danh sách chứa các số thỏa mãn điều kiện
result = []

# Duyệt qua các số từ 1000 đến 3000
for num in range(1000, 3001):
    if check_even_digits(num):
        result.append(str(num))

# In ra các số tìm được, phân tách bằng dấu phẩy
print(",".join(result))
