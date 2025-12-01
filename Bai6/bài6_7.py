# Nguyễn Bá Chung, mssv 245752021610143
"""7. Viết một class Python có tên Circle được xây dựng theo bán kính và hai phương
thức sẽ tính diện tích và chu vi của hình tròn."""
import math  # dùng để lấy giá trị PI chính xác

class Circle:
    def __init__(self, radius):
        self.radius = radius  # khởi tạo bán kính

    def area(self):
        # Công thức: S = π * r²
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        # Công thức: C = 2 * π * r
        return 2 * math.pi * self.radius

# Sử dụng clas
r = float(input("Nhập bán kính hình tròn: "))
circle = Circle(r)

print(f"Diện tích hình tròn là: {circle.area():.2f}")
print(f"Chu vi hình tròn là: {circle.perimeter():.2f}")
