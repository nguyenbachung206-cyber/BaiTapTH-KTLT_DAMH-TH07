# Nguyễn Bá Chung, mssv 245752021610143
S = input('nhap chuoi: ')
for ch in S:
    if ch not in [' ', '\t']:
        ch = ch.upper() #lệnh .upper là lệnh chuyển snag chữ in hoa
        print(ch)

        