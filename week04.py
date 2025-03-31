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

    def __str__(self):
        node = self.head
        out_texts = ""
        while node is not None:
            # out_texts = out_texts + str(node.data) + " -> "
            out_texts = out_texts + f"{node.data} -> "
            node = node.link
        return out_texts + "end"

ll = LinkedList() # LinkedList 객체 만들기
ll.append(8)
ll.append(10)
ll.append(-9)

print(ll)