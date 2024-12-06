print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Hàm in n dòng của tam giác Pascal
def print_pascals_triangle(n):
    triangle = []  # Danh sách để lưu các dòng của tam giác Pascal

    # Tạo tam giác Pascal
    for i in range(n):
        row = [1] * (i + 1)  # Mỗi dòng có i+1 phần tử và tất cả đều là 1
        for j in range(1, i):
            # Các phần tử giữa đầu và cuối được tính là tổng của hai phần tử trên nó
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    # In ra tam giác Pascal
    for row in triangle:
        print(" ".join(map(str, row)))

# Nhập số n từ người dùng
n = int(input("Nhập số n: "))

# In n dòng đầu tiên của tam giác Pascal
print_pascals_triangle(n)
