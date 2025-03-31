import random

class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head: # 링크드리스트가 비어있는 상태면 (node가 하나도 없는 상태)
            self.head = Node(data) # 새 노드를 head에 연결
            return
        current = self.head
        while current.link:
            current = current.link # 다음 노드로 이동
        current.link = Node(data)

    def search(self, target):
        current = self.head
        while current.link:
            if current.data == target:
                return f"{target}을(를) 찾았습니다."
            else:
                current = current.link # 다음 노드로 이동
        return f"{target}은(는) 링크드리스트 안에 존재하지 않습니다."

    def __str__(self):
        node = self.head
        out_texts = ""
        while node is not None:
            # out_texts = out_texts + str(node.data) + " -> "
            out_texts = out_texts + f"{node.data} -> "
            # join 함수로 하는 것도 코드 생각해보기
            node = node.link
        return out_texts + "end"

# ll = LinkedList() # LinkedList 객체 만들기
# ll.append(8)
# ll.append(10)
# ll.append(-9)

# print(ll)
# print(ll.search(100))
# print(ll.search(10))


ll= LinkedList()
for _ in range(20):
    ll.append(random.randint(1, 30))

print(ll)
print(ll.search(10))