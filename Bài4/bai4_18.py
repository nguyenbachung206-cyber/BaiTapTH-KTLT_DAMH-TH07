# Nguyễn Bá Chung, mssv 245752021610143 
# Bài 18: Hãy nhập số nguyên n,tạo một list gồm các số fibonacci nhỏ hơn n và in ra

n = int(input("Nhập số nguyên n: "))
# Khởi tạo hai số đầu tiên của dãy Fibonacci
a, b = 0, 1
fibo = []  # Tạo list rỗng để chứa các số Fibonacci
# Tạo dãy Fibonacci nhỏ hơn n
while a < n:
    fibo.append(a)
    a, b = b, a + b  # cập nhật giá trị mới: a = b, b = a + b
# In ra kết quả
print("Dãy Fibonacci nhỏ hơn", n, "là:")
print(fibo)
