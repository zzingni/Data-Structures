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

    def remove(self, target):
        if self.head.data == target: # self.head 는 객체라서 메모리주소를 가지고 있기 때문에 target 숫자와는 비교 안됨. self.head.data와 비교해야 함!!! 책의 코드로 하면 오류 생김
            self.head = self.head.link 
            return
        current = self.head
        previous = None
        while current:
            if current.data == target:
               previous.link = current.link
               current.link = None
            previous = current
            current = current.link

    def search(self, target):
        current = self.head
        # while current.link: .link 있으면 지운 데이터까지 돌게 됨 (지운숫자 -9로 테스트 ㄱㄱ)
        while current:
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

ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
ll.remove(8)
print(ll.search(-9))
print(ll)
# ll.remove(-9)
ll.remove(10)
print(ll)