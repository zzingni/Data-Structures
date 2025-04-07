
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.link = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return "Stack is empty. Nothing to delete~"
        popped_node = self.top
        self.top = self.top.link
        return popped_node.data # 데이터 삭제가 자동으로 된 건가...?? 생각해보기...  뭐지 ㅇㅅㅇ
    # 티스토리에 포인터 활용한 c코드로 공부해서 올려보기 / 파이썬은 포인터가 없어서 참조형식으로 코드 짬


s1 = Stack()
print(s1.pop())

# 1번 push 후 pop 2번
#s1.push("자료구조")
#print(s1.pop())
#print(s1.pop())

s1.push("자료구조")
s1.push("데이터베이스")
# print(s1.pop()) # 데이터베이스부터 pop됨
# print(s1.pop())

for i in range(2): # index 벗어나면 스택이 비었기 때문에 에러 발생
    print(s1.pop())

