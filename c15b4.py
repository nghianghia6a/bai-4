print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Nhập chuỗi đầu vào từ người dùng
input_string = input("Nhập chuỗi các từ tiếng Anh: ")

# Tách chuỗi thành các từ
words = input_string.split()

# Sắp xếp các từ theo thứ tự từ điển
words.sort()

# In ra các từ theo thứ tự từ điển
print("Các từ theo thứ tự từ điển:")
for word in words:
    print(word)
