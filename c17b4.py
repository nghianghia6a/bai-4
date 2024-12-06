
print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Hàm tính tổng các ước số của một số
def sum_of_divisors(x):
    sum_div = 0
    # Tính các ước số từ 1 đến x
    for i in range(1, x):
        if x % i == 0:  # Nếu i là ước số của x
            sum_div += i
    return sum_div

# Nhập số n từ người dùng
n = int(input("Nhập số n: "))

# Duyệt qua các số từ 1 đến n-1
print(f"Các số nguyên dương nhỏ hơn {n} có tổng các ước số lớn hơn chính nó là:")
for i in range(1, n):
    if sum_of_divisors(i) > i:
        print(i)
