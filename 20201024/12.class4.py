# class -> instance
# 생성자 __init__
# 소멸자 __del__  <- GC가 호출한다.garbage collector

class Node:
    def __init__(self):
        print("생성자 호출")
    
    def __del__(self):
        print("소멸자 호출")

print("시작")
node = Node()
#del node
print("진행중")
print("프로그램 종료")