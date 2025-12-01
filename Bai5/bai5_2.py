# Nguyễn Bá Chung, mssv 245752021610143
# bài 2:Sử dụng thư viện tiêu chuẩn của python (datetime)
# định dạng mở thư viện thời gian
from datetime import datetime, timedelta
# Lấy thời gian hiện tại
now = datetime.now()
print("Hiện tại:", now.strftime("%H:%M:%S - %d/%m/%Y"))

# Cộng 7 ngày
next_week = now + timedelta(days=7)
print("Sau 7 ngày:", next_week.strftime("%d/%m/%Y"))

# Tính số ngày giữa 2 thời điểm
ngay1 = datetime(2025, 10, 1)
ngay2 = datetime(2025, 10, 30)
hieu = ngay2 - ngay1
print("Số ngày chênh lệch:", hieu.days)

