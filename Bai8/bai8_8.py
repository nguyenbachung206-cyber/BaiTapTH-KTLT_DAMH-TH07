# Nguyễn Bá Chung, mssv 245752021610143
"""8. Viết chương trình graphic sử dụng thư viện Tkinter thực hiện:
a) Xây dựng form hiển thị thôn tin cá nhân (họ tên, ngày tháng năm sinh, MSSV,
ngành học)
b) Xây dựng form có nội dung như hình ở dưới, khi bấm vào nút “Click Me”
thông tin nút radio button đang lựa chọn sẽ được chỉ ra (tương ứng với các số 1,
2, 3)"""
# Gọi thư viện lập trình giao diện
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()                 # tạo cửa sổ chính
root.title("Thông tin cá nhân")  # đặt tên cho cửa sổ
# Câu a

tk.Label(root, text="THÔNG TIN CÁ NHÂN ", font=("Time new roman", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
# Họ tên
tk.Label(root, text="Họ tên:").grid(row=1, column=0, sticky="w")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=1, column=1)

# Ngày sinh
tk.Label(root, text="Ngày sinh:").grid(row=2, column=0, sticky="w")
dob_entry = tk.Entry(root, width=30)
dob_entry.grid(row=2, column=1)

# MSSV
tk.Label(root, text="MSSV:").grid(row=3, column=0, sticky="w")
mssv_entry = tk.Entry(root, width=30)
mssv_entry.grid(row=3, column=1)

# Ngành học
tk.Label(root, text="Ngành học:").grid(row=4, column=0, sticky="w")
major_entry = tk.Entry(root, width=30)
major_entry.grid(row=4, column=1)

# Hàm hiển thị thông tin
def show_info():
    info = (
        f"Họ tên: {name_entry.get()}\n"
        f"Ngày sinh: {dob_entry.get()}\n"
        f"MSSV: {mssv_entry.get()}\n"
        f"Ngành học: {major_entry.get()}"
    )
    messagebox.showinfo("Thông tin cá nhân", info)

tk.Button(root, text="Hiển thị thông tin", command=show_info).grid(row=5, column=0, columnspan=2, pady=8)

#  PHẦN B – RADIO BUTTON

tk.Label(root, text="--- LỰA CHỌN RADIO BUTTON ---", font=("Arial", 12, "bold")).grid(row=6, column=0, columnspan=2, pady=10)

selected = tk.IntVar()
selected.set(1)

radio_frame = tk.Frame(root)
radio_frame.grid(row=7, column=0, columnspan=2)

tk.Radiobutton(radio_frame, text="First", value=1, variable=selected).pack(side="left", padx=5)
tk.Radiobutton(radio_frame, text="Second", value=2, variable=selected).pack(side="left", padx=5)
tk.Radiobutton(radio_frame, text="Third", value=3, variable=selected).pack(side="left", padx=5)

def show_selected():
    messagebox.showinfo("Kết quả", f"Bạn đã chọn nút số: {selected.get()}")

tk.Button(root, text="Click Me", command=show_selected).grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()
