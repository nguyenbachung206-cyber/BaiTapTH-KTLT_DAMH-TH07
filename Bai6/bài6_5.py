# Nguyễn Bá Chung, mssv 245752021610143
"""5. Viết chương trình Python dưới dạng class để đảo ngược chuỗi từ từng chữ.
Dữ liệu vào : 'hello .py'
Đầu ra : '.py hello'"""
# Khai báo lớp ReverseWords
class ReverseWords:
    def __init__(self, sentence):
        self.sentence = sentence
# Xây dựng phương thức reverse()
    def reverse(self):
        # Tách chuỗi thành các từ
        words = self.sentence.split()
        # Đảo ngược thứ tự các từ
        words.reverse()
        # Ghép lại thành chuỗi mới
        return ' '.join(words)
    
# sử dụng class
input_str = str(input('nhập chuỗi từ bàn phím: '))
reverser = ReverseWords(input_str)

print("Chuỗi ban đầu:", input_str)
print("Chuỗi sau khi đảo:", reverser.reverse())
