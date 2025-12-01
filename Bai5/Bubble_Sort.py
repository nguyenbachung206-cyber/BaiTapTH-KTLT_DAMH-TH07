# Bubble_Sort.py
# Hàm sắp xếp nổi bọt (Bubble Sort)

def bubbleSort(nlist):
    n = len(nlist)
    for i in range(n - 1):  # lặp qua từng phần tử
        swapped = False
        for j in range(n - i - 1):  # so sánh phần tử kề nhau
            if nlist[j] > nlist[j + 1]:
                # hoán đổi vị trí
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                swapped = True
        # nếu không có hoán đổi nào => mảng đã được sắp xếp
        if not swapped:
            break
    return nlist
