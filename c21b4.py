
print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Hàm kiểm tra các số nhị phân chia hết cho 5
def check_divisible_by_5(binary_numbers):
    result = []
    for binary in binary_numbers:
        # Chuyển đổi số nhị phân thành thập phân
        decimal = int(binary, 2)
        # Kiểm tra xem số thập phân có chia hết cho 5 không
        if decimal % 5 == 0:
            result.append(binary)
    # In ra các số nhị phân chia hết cho 5, phân tách bằng dấu phẩy
    return ",".join(result)

# Nhập chuỗi các số nhị phân từ người dùng
input_data = input("Nhập chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy: ")

# Chia chuỗi thành các số nhị phân
binary_numbers = input_data.split(',')

# Kiểm tra và in ra các số nhị phân chia hết cho 5
output = check_divisible_by_5(binary_numbers)
print(output)
