print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")


# Hàm đếm số chữ hoa và chữ thường
def count_upper_lower(sentence):
    upper_case = 0  # Biến đếm số chữ hoa
    lower_case = 0  # Biến đếm số chữ thường
    for char in sentence:
        if char.isupper():  # Kiểm tra xem ký tự là chữ hoa không
            upper_case += 1
        elif char.islower():  # Kiểm tra xem ký tự là chữ thường không
            lower_case += 1
    return upper_case, lower_case

# Nhập câu từ người dùng
sentence = input("Nhập câu: ")

# Gọi hàm và nhận kết quả
upper_case, lower_case = count_upper_lower(sentence)

# In kết quả
print(f"Chữ hoa: {upper_case}")
print(f"Chữ thường: {lower_case}")
