# Nguyễn Bá Chung, mssv 245752021610143
"""10.Xây dựng hàm “bubbleSort (nlist)” (giải thuật sắp xếp nổi bọt) dưới dạng module.
Viết chương trình nhập một nlist n phần tử từ bàn phím và sắp xếp.
Sample Data: [14,46,43,27,57,41,45,21,70]
Expected Result: [14, 21, 27, 41, 43, 45, 46, 57, 70]
"""
# Hàm sắp xếp nổi bọt
def bubbleSort(nlist):
    n = len(nlist)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nlist[j] > nlist[j + 1]:
                # Hoán đổi vị trí nếu phần tử sau nhỏ hơn phần tử trước
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
# Chương trình chính
if __name__ == "__main__":
    # Nhập danh sách từ bàn phím, ví dụ: 14,46,43,27,57,41,45,21,70
    nlist = [int(x) for x in input("Nhập các phần tử (cách nhau bởi dấu phẩy): ").split(',')]  
    bubbleSort(nlist)
    print("Danh sách sau khi sắp xếp tăng dần là:")
    print(nlist)
