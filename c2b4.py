print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

S = input('Nhap chuoi:')
for ch in S:
    if ch not in [' ', '\t']:  # Kiểm tra nếu ký tự không phải là space hoặc tab
        print(ch)


