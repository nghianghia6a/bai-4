print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Nhập danh sách các số từ người dùng
input_numbers = input("Nhập danh sách các số (cách nhau bởi dấu phẩy): ")

# Chuyển chuỗi nhập vào thành danh sách các số nguyên
numbers = [int(x) for x in input_numbers.split(',')]

# Lọc các số lẻ
odd_numbers = [num for num in numbers if num % 2 != 0]

# In kết quả
print(",".join(map(str, odd_numbers)))
