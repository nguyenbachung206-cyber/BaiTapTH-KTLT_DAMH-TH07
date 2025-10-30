# Nguyễn Bá Chung, mssv 245752021610143
# bài 8 BT thktlt
import math
pos = [0,0]
while True:
 s = input('nhập lệnh (ví dụ: UP 5 hoặc enter để dùng): ')
 if not s:
  break
 movement = s.split(" ")
 direction = movement[0]
 steps = int(movement[1])
 if direction=="UP":
  pos[0]+=steps
 elif direction=="DOWN":
  pos[0]-=steps
 elif direction=="LEFT":
  pos[1]-=steps
 elif direction=="RIGHT":
  pos[1]+=steps
 else:
  pass
######################
distance =  (int(round(math.sqrt(pos[1]**2+pos[0]**2))))
print('khoang cach là: ', distance)