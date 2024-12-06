print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Hàm tính số tiền thực của tài khoản ngân hàng từ nhật ký giao dịch
def calculate_balance():
    balance = 0  # Khởi tạo số dư ban đầu là 0
    while True:
        transaction = input("Nhập giao dịch (hoặc nhấn Enter để kết thúc): ")
        if not transaction:
            break  # Dừng lại khi không còn giao dịch nào nhập vào
        # Tách giao dịch thành loại giao dịch và số tiền
        action, amount = transaction.split()
        amount = int(amount)  # Chuyển số tiền thành số nguyên
        if action == "D":  # Nếu là giao dịch gửi tiền
            balance += amount
        elif action == "W":  # Nếu là giao dịch rút tiền
            balance -= amount
    return balance

# Tính số tiền thực của tài khoản sau các giao dịch
final_balance = calculate_balance()

# In kết quả
print(f"Số tiền thực của tài khoản là: {final_balance}")
