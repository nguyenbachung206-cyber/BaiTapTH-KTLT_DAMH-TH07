# search_module.py
# Nguyễn Bá Chung, MSSV: 245752021610143
# Module chứa hàm tìm kiếm tuyến tính (Sequential Search)

def Sequential_search(dlist , item):
    # hàm tìm kiếm tuyến tính trong danh sách
    for i in range(len(dlist)):
        if dlist[i] == item:
            return i  #trả về vị trí tìm thấy (index)
    return -1 #nếu ko tìm thấy
    
        
