
class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0


    def enqueue(self, data):
        self.size = self.size + 1
        node = Node(data)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue is empty!")
        self.size = self.size - 1
        temp = self.front
        self.front = self.front.link
        if self.front is None:
            self.rear = None
        temp.link = None # 공부하면서 이 문장 다시 생각해보기
        return temp.data

q = Queue()
q.enqueue("데이터베이스")
q.enqueue("자료구조")
print(q.size, q.front.data, q.rear.data)

q.dequeue()
q.dequeue()
print(q.size, q.front.link, q.rear.link)