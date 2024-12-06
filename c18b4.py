print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")


# Hàm tạo dãy Fibonacci nhỏ hơn n
def fibonacci_less_than_n(n):
    fibonacci_list = []
    a, b = 0, 1
    while a < n:
        fibonacci_list.append(a)
        a, b = b, a + b  # Cập nhật các số Fibonacci
    return fibonacci_list

# Nhập số nguyên n từ người dùng
n = int(input("Nhập số nguyên n: "))

# Tạo danh sách các số Fibonacci nhỏ hơn n
fibonacci_numbers = fibonacci_less_than_n(n)

# In kết quả
print("Danh sách các số Fibonacci nhỏ hơn", n, "là:", fibonacci_numbers)
