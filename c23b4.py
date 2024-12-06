print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Hàm đếm số chữ cái và chữ số
def count_characters_and_digits(sentence):
    letters = 0  # Biến đếm số chữ cái
    digits = 0   # Biến đếm số chữ số
    for char in sentence:
        if char.isalpha():  # Kiểm tra xem ký tự là chữ cái không
            letters += 1
        elif char.isdigit():  # Kiểm tra xem ký tự là chữ số không
            digits += 1
    return letters, digits

# Nhập câu từ người dùng
sentence = input("Nhập câu: ")

# Gọi hàm và nhận kết quả
letters, digits = count_characters_and_digits(sentence)

# In kết quả
print(f"Số chữ cái là: {letters}")
print(f"Số chữ số là: {digits}")
