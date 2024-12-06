
print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Tạo danh sách các số nguyên tố nhỏ hơn 1 triệu
primes = [x for x in range(2, 1000000) if is_prime(x)]

# Chuyển danh sách thành tuple
P = tuple(primes)

# In ra tuple P
print("Tuple P chứa các số nguyên tố nhỏ hơn 1 triệu:", P)
