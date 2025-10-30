# Nguyễn Bá Chung, mssv 245752021610143
# Bai6. Nhập một tên người từ bàn phím, hãy tách phần họ và tên riêng của người đó và in chúng ra màn hình

ho_ten = input('nhập từ bàn phím: ')
# tách chuỗi
ds = ho_ten.split()
# lấy phần tự tên
ten = ds[-1]
# lấy phần tử họ
ho = ' '.join(ds[0:2])

print('ho là: ', ho)
print('tên là:', ten)