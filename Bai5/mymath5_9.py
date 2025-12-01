# mymath5_9.py
# Hàm tìm kiếm nhị phân

def mymath5_9(lst, value):
    """
    lst: danh sách (đã sắp xếp)
    value: giá trị cần tìm
    Trả về True nếu tìm thấy, False nếu không
    """
    lower = 0
    upper = len(lst) - 1

    while lower <= upper:
        mid = lower + (upper - lower) // 2

        if lst[mid] == value:
            return True
        elif lst[mid] < value:
            lower = mid + 1
        else:
            upper = mid - 1

    return False
