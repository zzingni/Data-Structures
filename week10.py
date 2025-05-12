from idlelib.search import SearchDialog


class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

def pre_order(node):
    if node is None:
        return
    print(node.data, end="->")
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data, end="->")
    in_order(node.right)


def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end='-')



def insert(root, value):
    new_node = TreeNode()
    new_node.data = value

    if root is None:  # 첫 번째 노드일때 처리
        return new_node

    current = root
    while True:
        if value < current.data:
            if current.left is None:
                current.left = new_node
                break
            current = current.left  # move
        else:
            if current.right is None:
                current.right = new_node
                break
            current = current.right  # move
    return root

# 첫번째 버전 : search 매개변수 없음. search 함수 안에서 숫자 찾고 출력까지
# 두번째 버전 : search 매개변수, 함수 안에서 입력 받기
# 세번째 버전 : 출력. search에서는 boolean 값 받기

def search(value):
    current = root
    while True:
        if value == current.data:
            return True
        elif find_number < current.data:
            if current.left is None:
                return False
            current = current.left
        else:
            if current.right is None:
               return False
            current = current.right

if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    for number in numbers:
        root = insert(root, number)

    print("BST 구성 완료")
    post_order(root)  # 3 9 8 15 10
    print()
    in_order(root)
    print()
    pre_order(root)
    print()

    find_number = int(input("찾고자 하는 값 : "))
    search(find_number)
    if search(find_number) == True:
        print(f"{find_number}을(를) 찾았습니다")
    else:
        print(f"{find_number}가 존재하지 않습니다.")
