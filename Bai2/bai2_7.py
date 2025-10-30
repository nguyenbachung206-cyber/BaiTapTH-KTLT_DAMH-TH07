# Nguyễn Bá Chung , msv 245752021610143
# bài tập 7 sgk
n=int(input("Nhập vào một số:"))
d=dict() #Tạo một từ điển (dictionary) rỗng có tên là d.
for i in range(1,n+1):
     #Vòng lặp for duyệt qua các số từ 1 đến n
     # do đề bài yêu cầu lấy cả 1 và n nên phải n+1 
     # vì in range chỉ lấy đến n-1 
    d[i]=i*i #Mỗi lần lặp, gán khóa là i và giá trị là i*i.
print (d) #in toàn bộ nội dung của từ điển d ra màn hình